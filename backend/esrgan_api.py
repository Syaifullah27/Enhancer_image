from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import io
import torch
import torch.nn.functional as F
from archs.RRDBNet_arch import RRDBNet

app = Flask(__name__)
CORS(app)

# Load model x2
model_path = "models/RealESRGAN_x2plus.pth"

# Instansiasi model dengan num_in_ch=12 karena checkpoint mengharapkan 12 channel (3 x 2^2)
model = RRDBNet(num_in_ch=12, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=2)

try:
    # Coba muat checkpoint dengan weights_only=True jika didukung
    state_dict = torch.load(model_path, map_location=torch.device('cpu'), weights_only=True)
except RuntimeError:
    print("Warning: Falling back to weights_only=False. Ensure the model is from a trusted source.")
    state_dict = torch.load(model_path, map_location=torch.device('cpu'), weights_only=False)

# Jika checkpoint menyimpan state dict di key 'params_ema', gunakan itu; jika tidak, gunakan langsung.
loaded_state = state_dict['params_ema'] if 'params_ema' in state_dict else state_dict

model.load_state_dict(loaded_state, strict=True)
model.eval()

@app.route('/enhance', methods=['POST'])
def enhance():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    if file.content_length > 5 * 1024 * 1024:
        return jsonify({"error": "File size exceeds 5MB limit"}), 400

    # Buka dan konversi gambar
    img = Image.open(file.stream).convert('RGB')
    # Ubah ke numpy array dan transposisi ke format [C, H, W]
    img = np.array(img).transpose(2, 0, 1).astype(np.float32) / 255.0
    img = torch.from_numpy(img).unsqueeze(0)  # shape: [1, 3, H, W]

    # Pilihan A: Cropping untuk memastikan ukuran habis dibagi 2
    _, _, h, w = img.shape
    new_h = (h // 2) * 2
    new_w = (w // 2) * 2
    if new_h != h or new_w != w:
        img = img[:, :, :new_h, :new_w]

    # Pilihan B (alternatif): Padding agar ukuran menjadi habis dibagi 2
    # Uncomment kode berikut jika ingin menggunakan padding daripada cropping
    # pad_h = (2 - h % 2) % 2
    # pad_w = (2 - w % 2) % 2
    # img = F.pad(img, (0, pad_w, 0, pad_h), mode='reflect')

    # Terapkan pixel unshuffle untuk mengubah 3 channel menjadi 12 channel
    img = F.pixel_unshuffle(img, downscale_factor=2)  # shape: [1, 12, H/2, W/2]

    with torch.no_grad():
        output = model(img)

    output = output.squeeze().clamp(0, 1).numpy().transpose(1, 2, 0) * 255.0
    result = Image.fromarray(output.astype(np.uint8))

    byte_io = io.BytesIO()
    result.save(byte_io, 'JPEG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(port=5000)
