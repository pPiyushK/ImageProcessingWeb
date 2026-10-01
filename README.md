🖼️ Image Processing Tool

A simple web-based Image Processing Tool built using Python, Flask, NumPy, and Pillow.

This project allows users to upload an image and perform different image-processing operations such as grayscale conversion, brightness adjustment, rotation, flipping, resizing, and cropping.

---

🚀 Features

- 📤 Upload an image
- 🖤 Convert image to grayscale
- ☀️ Increase or decrease brightness
- 🎨 Adjust image contrast
- 🔄 Rotate image
- ↔️ Flip image
- 📏 Resize image
- ✂️ Crop image
- 💾 Save/download processed images
- 🌐 Simple and user-friendly web interface

---

🛠️ Technologies Used

- Python – Main programming language
- Flask – Web framework
- NumPy – Numerical and pixel-level image operations
- Pillow (PIL) – Image reading, processing, and saving
- HTML – Web page structure
- CSS – Website design
- JavaScript – Frontend interactions

---

📁 Project Structure

ImageProcessingTool/
│
├── app.py
├── requirements.txt
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── script.js
│   │
│   └── uploads/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── processing/
│   ├── __init__.py
│   └── image_operations.py
│
└── README.md

---

⚙️ Installation

1. Clone the repository

git clone https://github.com/yourusername/ImageProcessingTool.git

2. Open the project folder

cd ImageProcessingTool

3. Create a virtual environment

python -m venv venv

4. Activate the virtual environment

Windows:

venv\Scripts\activate

Linux/macOS:

source venv/bin/activate

5. Install required libraries

pip install -r requirements.txt

---

▶️ Run the Project

Start the Flask application:

python app.py

You should see something similar to:

Running on http://127.0.0.1:5000/

Open your browser and visit:

http://127.0.0.1:5000/

---

🧠 How It Works

The application follows this process:

User
  ↓
Upload Image
  ↓
Flask Application
  ↓
Image Processing Functions
  ↓
NumPy + Pillow
  ↓
Processed Image
  ↓
Display / Download

NumPy in the Project

Images are represented as arrays of pixel values.

For example:

import numpy as np

image_array = np.array(image)

For an RGB image, the array generally has three channels:

Red
Green
Blue

NumPy is then used to perform operations on these pixel values.

---

📸 Example Operations

Grayscale

Converts a color image into a black-and-white/gray image.

Brightness

Changes the intensity of pixels.

bright = image_array + 40

Flip

Flips the image horizontally or vertically.

Resize

Changes the dimensions of the image.

Rotate

Rotates the image by a specified angle.

Crop

Extracts a selected portion of the image.

---

📦 Requirements

The main Python packages are:

Flask
NumPy
Pillow

You can install them using:

pip install -r requirements.txt

---

🔮 Future Improvements

The project can be extended with:

- 🌓 Dark/Light mode
- 🎚️ Interactive brightness and contrast sliders
- 🔍 Image preview before processing
- 📱 Mobile-friendly UI
- 🎨 More image filters
- 🤖 AI-based image enhancement
- ☁️ Cloud image storage
- 📊 Image information such as resolution and file size
- 🗑️ Automatic deletion of temporary uploaded files

---

🎯 Learning Objectives

This project helps in learning:

- Python programming
- NumPy arrays
- Image processing
- Pillow library
- Flask web development
- HTML/CSS/JavaScript
- File handling
- Backend and frontend integration
- Basic project structure

---

👨‍💻 Author

Piyush Kumar

B.Tech CSE Student
