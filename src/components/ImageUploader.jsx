import { useState } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

const ImageUploader = () => {
  const [original, setOriginal] = useState(null);
  const [enhanced, setEnhanced] = useState(null);
  const [loading, setLoading] = useState(false);
  const [progress, setProgress] = useState(0);

  const { getRootProps, getInputProps } = useDropzone({
    accept: 'image/*',
    multiple: false,
    maxSize: 5 * 1024 * 1024, // Batasi ukuran file maksimal 5MB
    onDrop: (files) => {
      if (files[0].size > 5 * 1024 * 1024) {
        alert('File size exceeds 5MB limit');
        return;
      }
      setOriginal(URL.createObjectURL(files[0]));
      handleEnhance(files[0]);
    },
  });

  const handleEnhance = async (file) => {
    setLoading(true);
    setProgress(0);

    const formData = new FormData();
    formData.append('image', file);

    try {
      const res = await axios.post('http://localhost:5000/enhance', formData, {
        responseType: 'blob',
        onUploadProgress: (progressEvent) => {
          const percentCompleted = Math.round((progressEvent.loaded * 100) / progressEvent.total);
          setProgress(percentCompleted);
        },
      });
      setEnhanced(URL.createObjectURL(res.data));
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

      {loading && (
        <div>
          <p>Processing... {progress}%</p>
          <progress value={progress} max="100" />
        </div>
      )}
    </div>
  );
};

export default ImageUploader;