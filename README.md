# Image Enhancement with ESRGAN

This project enhances images using the ESRGAN model. It consists of a React frontend and a Flask backend.

## Prerequisites
- Python 3.8+
- Node.js 16+
- Git

## Setup

### Backend
1. Navigate to the `backend` folder:
   ```bash
   cd backend
2. Create a virtual environment:
    ```bash
    python -m venv venv
3. Activate the virtual environment:
    ```bash
    source venv/Scripts/activate
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
5. Run the Flask server:
    ```bash
    python esrgan_api.py


## Frontend
1. Navigate to the `frontend` folder:
    ```bash
    cd frontend
2. Install dependencies:
    ```bash
    pnpm install
3. Run the development server:
    ```bash
    pnpm run dev