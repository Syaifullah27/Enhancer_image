from flask import Flask, request, send_file
from flask_cors import CORS  # <-- Tambahkan ini
import numpy as np
from PIL import Image
import io
import torch
from archs.RRDBNet_arch import RRDBNet

app = Flask(__name__)
CORS(app)  # <-- Tambahkan ini untuk mengaktifkan CORS

# Load model
model_path = "models/RealESRGAN_x4plus.pth"
model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)

# Load state dict
state_dict = torch.load(model_path, map_location=torch.device('cpu'))
model.load_state_dict(state_dict['params_ema'] if 'params_ema' in state_dict else state_dict, strict=True)
model.eval()

@app.route('/enhance', methods=['POST'])
def enhance():
    file = request.files['image']
    img = Image.open(file.stream).convert('RGB')
    
    # Preprocess
    img = np.array(img).transpose(2, 0, 1).astype(np.float32) / 255.0
    img = torch.from_numpy(img).unsqueeze(0)
    
    # Inference
    with torch.no_grad():
        output = model(img)
    
    # Postprocess
    output = output.squeeze().clamp(0, 1).numpy().transpose(1, 2, 0) * 255.0
    result = Image.fromarray(output.astype(np.uint8))
    
    # Return hasil
    byte_io = io.BytesIO()
    result.save(byte_io, 'JPEG')
    byte_io.seek(0)
    return send_file(
        byte_io,
        mimetype='image/jpeg',
        as_attachment=False,
        download_name='enhanced.jpg'
    )

if __name__ == '__main__':
    app.run(port=5000)