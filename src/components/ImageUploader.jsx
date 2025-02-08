import { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const ImageUploader = () => {
  const [original, setOriginal] = useState(null);
  const [enhanced, setEnhanced] = useState(null);
  const [loading, setLoading] = useState(false);

  const { getRootProps, getInputProps } = useDropzone({
    accept: 'image/*',
    multiple: false,
    onDrop: (files) => {
      setOriginal(URL.createObjectURL(files[0])); // Preview the original image
      handleEnhance(files[0]); // Send the image to the backend
    },
  });

  const handleEnhance = async (file) => {
    setLoading(true);
    const formData = new FormData();
    formData.append('image', file); // Append the file to FormData

    try {
      // Send the image to the backend
      const res = await axios.post('http://localhost:5000/enhance', formData, {
        responseType: 'blob', // Important: Receive the image as a blob
      });

      // Convert the response to a URL for display
      const enhancedImageUrl = URL.createObjectURL(res.data);
      setEnhanced(enhancedImageUrl);
    } catch (err) {
      console.error('Error enhancing image:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <div {...getRootProps()} className="dropzone">
        <input {...getInputProps()} />
        <p>Drop image here or click to upload</p>
      </div>

      <div className="preview-container">
        {original && <img src={original} alt="Original" style={{ maxWidth: '100%' }} />}
        {enhanced && <img src={enhanced} alt="Enhanced" style={{ maxWidth: '100%' }} />}
      </div>

      {loading && <div className="loading">Processing...</div>}
    </div>
  );
};

export default ImageUploader;