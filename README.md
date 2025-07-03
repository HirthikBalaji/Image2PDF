# 🖼️ Image to PDF Converter | Streamlit Web App

A simple and elegant web application that allows users to upload multiple images and instantly convert them into a downloadable PDF. Built with **Python**, **Streamlit**, **Pillow**, and **img2pdf**, this tool showcases rapid prototyping, file handling, and a sleek interactive UI using modern Python web technologies.

---

## 🚀 Features

- 📤 Upload multiple `.jpg`, `.jpeg`, `.png` images
- 🖼️ Live preview of uploaded images
- 🧠 Automatic conversion to RGB and PDF formatting
- 📄 Download the final PDF in one click
- ⚡ Fast, secure, and lightweight

---

## 📦 Tech Stack

- [Streamlit](https://streamlit.io/) – UI & Web framework
- [img2pdf](https://pypi.org/project/img2pdf/) – Image to PDF conversion
- [Pillow](https://python-pillow.org/) – Image processing (RGB, formatting)
- [Python 3.8+](https://www.python.org/) – Core language

---

## 🔧 Installation

Make sure Python 3.8+ is installed on your system.

1. **Clone the repository**

```bash
git clone https://github.com/HirthikBalaji/Image2PDF.git
cd Image2PDF
````

2. **Create and activate a virtual environment** (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install streamlit img2pdf pillow
```

---

## ▶️ Running the App

Start the Streamlit server with:

```bash
streamlit run main.py
```

Then open the provided localhost URL in your browser (usually `http://localhost:8501`).

---

## 💼 Why This Project?

This project demonstrates:

* Building modern UI with minimal code using **Streamlit**
* Handling multimedia file inputs
* Image-to-PDF logic using `img2pdf` with in-memory I/O
* Clean, professional user interface

Ideal for showcasing Python skills, app deployment, and full-stack prototyping in technical interviews or your portfolio.

---

## 🛠️ Future Improvements

* Add drag-and-drop upload
* Support more formats (e.g., TIFF, BMP)
* Rearrange image order before PDF generation
* Password-protect PDF files

---

## 🤝 License

This project is licensed under the MIT License.

---

⭐ If you like this project, consider giving it a star!

