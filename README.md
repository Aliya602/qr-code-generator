# qr-code-generator 📱
A simple Python application that generates QR codes from text or URLs and saves them as PNG images

## Features
- 📝 Encode any text or URL
- 🎨 Customizable colors and size
- 💾 Save as PNG file
- 🚀 Automatically opens the generated image from your operating system

## Requirements
- Python 3.x
- qrcode
- pillow
- colorama 

## Example Output
Enter text or URL: https://github.com
Enter filename: github_qr
✅ QR code saved as github_qr.png
📱 Scan it with your phone to see https://github.com...

## How to Run
```bash
pip install qrcode pillow colorama
python qr_code_generator.py
