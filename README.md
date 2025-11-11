# 🧩 Image Spritesheet Generator

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Pillow](https://img.shields.io/badge/Pillow-Enabled-green?logo=python)](https://python-pillow.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Output Format](https://img.shields.io/badge/Output-PNG-lightblue)](#)
[![Input Type](https://img.shields.io/badge/Input-JPG%2FPNG-orange)](#)

---

A simple, reliable Python tool that stitches multiple sequential images into a **single horizontal spritesheet** — perfect for animations, GIF creation, or frame previews.

---

## ✨ Features

* 🖼 **Automatic Frame Detection** – Finds and sorts all images (`.png`, `.jpg`, `.jpeg`) in a folder.
* 📏 **Dynamic Sizing** – Calculates total width and max height automatically.
* ⚙️ **Clean Output** – Exports a single, neatly aligned spritesheet.
* 💾 **One-Line Run** – Just point to a folder of frames and let it handle the rest.

---

## 🚀 Quick Start

### 1. Place Your Frames

Put all your frame images (e.g. `0001.png`, `0002.png`, `0003.png`, …) in one folder.

### 2. Run the Script

```bash
python main.py
```

You’ll be prompted to enter the path to your folder:

```
Path to images folder: ./frames
```

After that, your spritesheet will be saved as:

```
spritesheet.png
```

---

## 🧩 Example

| Input Frames                                                                                                                 | Output Spritesheet                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| ![Frames](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Sprite_sheet_example.png/256px-Sprite_sheet_example.png) | ![Sheet](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Sprite_sheet_sample_output.png/512px-Sprite_sheet_sample_output.png) |

---

## ⚙️ Requirements

Install dependencies manually (if needed):

```bash
pip install pillow
```

---

## 📂 How It Works

1. Reads all valid images in the specified directory.
2. Sorts them numerically (e.g. `0001`, `0002`, `0003` …).
3. Opens them using Pillow and calculates combined dimensions.
4. Pastes them sequentially into a new canvas.
5. Saves the final composite as `spritesheet.png`.

---

## 🧠 Notes

* Works best with **equal-sized frames**.
* The order is **based on filename sorting**, so numbering matters (`001`, `002`, …).
* Supports **PNG transparency** automatically.

---

## ⚡ License

**MIT License © 2025 Moksh Verma**
You’re free to modify or reuse this tool in any of your animation, game, or visual projects.

---

Would you like me to make it automatically display the output sheet’s resolution in a fancy Markdown code block example (like `Spritesheet saved as 5120x1024`) for better GitHub visual flow?
