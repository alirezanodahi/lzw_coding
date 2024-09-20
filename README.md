# LZW Image Compression and Decompression

This project implements an image compression and decompression tool using the **LZW (Lempel-Ziv-Welch)** algorithm. It reads an image file, compresses it using LZW, and then decompresses it back to its original form. Additionally, it provides a comparison of the compression efficiency.

## Features
- **LZW Encoding**: Compresses image data using LZW algorithm.
- **LZW Decoding**: Decompresses the encoded data back into an image.
- **File Saving**: Saves the original and encoded data to `.txt` files.
- **Efficiency Comparison**: Compares the original image size with the compressed size to calculate efficiency.

## Installation

1. Clone the repository:
   - You can clone the repository by using a version control tool like `git` or download the project manually from GitHub.
   
2. Install the required dependencies:
   - This project uses `PIL` (Pillow) for image processing and `numpy` for handling arrays. You can install the dependencies via `pip`:
     ```python
     pip install Pillow numpy
     ```

## Usage

1. **Load the Image**: 
   Replace the image file in the code with your own image file (e.g., `your_image.png`).
   ```python
   original_image = Image.open("your_image.png")
