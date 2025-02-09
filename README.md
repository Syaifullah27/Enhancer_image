# 📷 Aplikasi Peningkat Kualitas Gambar dengan ESRGAN

Aplikasi ini menggunakan **React (Frontend) + Flask (Backend) + ESRGAN Model** untuk meningkatkan kualitas gambar.

## ✨ Fitur:
- Upload gambar via drag & drop
- Proses peningkatan kualitas gambar secara real-time
- Tampilkan hasil sebelum & sesudah

---

## 📋 Daftar Isi
- [🛠️ Prasyarat Sistem](#-prasyarat-sistem)
- [📥 Instalasi](#-instalasi)
- [🚀 Menjalankan Aplikasi](#-menjalankan-aplikasi)
- [📂 Struktur Proyek](#-struktur-proyek)
- [🔧 Troubleshooting](#-troubleshooting)
- [🤝 Kontribusi](#-kontribusi)
- [📜 Lisensi](#-lisensi)
- [💡 Catatan Tambahan](#-catatan-tambahan)

---

## 🛠️ Prasyarat Sistem
Sebelum mulai, pastikan komputer Anda sudah terinstal:

| Komponen | Versi Minimal | Cara Cek |
|----------|--------------|----------|
| Python   | 3.8          | `python --version` |
| Node.js  | 16.x         | `node --version` |
| npm      | 8.x          | `npm --version` |
| Git      | 2.x          | `git --version` |

---

## 📥 Instalasi

### 1️⃣ Clone Repositori
```bash
git clone https://github.com/username-anda/enhance-image.git
cd enhance-image
```

### 2️⃣ Setup Backend
```bash
# Masuk ke folder backend
cd backend

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Untuk Windows:
venv\Scripts\activate
# Untuk Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Setup Frontend
```bash
# Kembali ke root folder
cd ..

# Masuk ke folder frontend
cd frontend

# Install dependencies
npm install
```

---

## 🚀 Menjalankan Aplikasi

### 1️⃣ Jalankan Backend (Flask)
```bash
cd backend
venv\Scripts\activate  # Pastikan virtual environment aktif
python esrgan_api.py
```
**Output yang diharapkan:**
```bash
* Serving Flask app 'esrgan_api'
* Running on http://127.0.0.1:5000
```

### 2️⃣ Jalankan Frontend (React)
```bash
cd frontend
npm run dev
```
**Output yang diharapkan:**
```bash
  VITE v5.0.12  ready in 321 ms

  ➜  Local:   http://localhost:5173/
```

---

## 📂 Struktur Proyek
```
enhance-image/
├── backend/            # Server Flask
│   ├── models/         # Folder untuk model ESRGAN
│   ├── archs/          # Arsitektur model
│   ├── esrgan_api.py   # API endpoint
│   └── requirements.txt
│
├── frontend/           # Aplikasi React
│   ├── src/
│   │   └── components/ # Komponen React
│   └── package.json
│
├── .gitignore
└── README.md           # File ini
```

---

## 🔧 Troubleshooting

### 1️⃣ Error "Port 5000 sudah digunakan"
```bash
# Cari proses yang menggunakan port 5000
lsof -i :5000

# Hentikan proses
kill -9 <PID>
```

### 2️⃣ `ModuleNotFoundError` di Python
```bash
# Pastikan virtual environment aktif
deactivate
venv\Scripts\activate

# Update dependencies
pip install -r requirements.txt
```

### 3️⃣ CORS Error di Browser
```bash
# Pastikan di backend sudah terinstall flask-cors
pip install flask-cors
```

---

## 🤝 Kontribusi
1. **Fork** repositori ini
2. **Buat branch fitur baru**
```bash
git checkout -b fitur-saya
```
3. **Commit perubahan**
```bash
git commit -m "Tambahkan fitur baru"
```
4. **Push ke branch**
```bash
git push origin fitur-saya
```
5. **Buat Pull Request**

---

## 📜 Lisensi
Proyek ini dilisensikan di bawah **MIT License**.

---

## 💡 Catatan Tambahan

### **Model ESRGAN**:
- File model **(RealESRGAN_x4plus.pth)** tidak termasuk dalam repositori karena ukurannya besar
- **Download dari [Link ini](#)**
- Simpan di **`backend/models/`**

### **Optimasi Performa**:
- **Untuk GPU**: Ganti `map_location=torch.device('cpu')` menjadi `cuda`
- **Untuk gambar besar (>5MB)**, tambahkan warning di frontend

### **Environment Variables**:
Buat file **`.env`** di root folder dengan konten berikut:
```ini
FLASK_ENV=development
REACT_APP_API_URL=http://localhost:5000
```

---

🚀 **Selamat menggunakan Aplikasi Peningkat Kualitas Gambar dengan ESRGAN!** 🎉
