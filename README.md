# 🎮 DAT to PNG Converter

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Working-brightgreen?style=for-the-badge)

---

## 📌 Overview

A simple and fast Python tool that extracts embedded PNG images from `.dat` files.

Perfect for game assets, avatar files, or any binary container that stores images.

---

## ✨ Features

- 🖼️ Extracts PNG images from `.dat` files  
- 📂 Batch support (process multiple files at once)  
- ⏱️ Automatic timestamp filenames (no overwrite)  
- ⚡ Fast and lightweight  
- 🧠 No external libraries needed  

---

## 🚀 Usage

### ▶️ Run the script

python main.py

---

### 📁 Enter your folder

Example:

C:\Users\YourName\Desktop\dat_files

---

### ✅ Done

All images will be extracted automatically.

---

## 📦 Output

Files will look like this:

avatar_2026-04-21_17-10-03_0.png  
avatar_2026-04-21_17-10-03_1.png  
avatar_2026-04-21_17-10-03_2.png  

---

## ⚙️ How it works

The tool scans raw binary data and detects PNG images using signatures:

Header: 89 50 4E 47  
Footer: 49 45 4E 44  

Once detected, the image is extracted and saved.

---

## 📋 Requirements

- Python 3.x

---

## ⚠️ Notes

- Not every `.dat` file contains images  
- Some files may contain multiple PNGs  
- Corrupted or incomplete data may still extract partially  

---

## 💡 Example Use Cases

- 🎮 Game asset extraction  
- 👤 Avatar recovery  
- 📦 Binary file analysis  

---

## 📜 License

Free to use, modify, and distribute.

---

## ⭐ Support

If you like this project, consider giving it a star ⭐
