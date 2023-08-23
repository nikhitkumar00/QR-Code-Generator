# QR Code Generator

This script allows you to generate QR codes for a given input data using the `qrcode` Python library.

## Prerequisites

- Python 3.x
- `qrcode` library (you can install it using `pip install qrcode[pil]`)

## Installation

1. Clone or download this repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory.

   ```bash
   cd qr-code-generator
   ```

3. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script using Python.

   ```bash
   python generate_qr_code.py
   ```

2. Enter the data for which you want to generate a QR code when prompted.

   ```bash
   Enter the data for the QR code: <your-data-here>
   ```

3. The script will generate a QR code and save it as `qrcode.png` in the same directory.

4. A success message will be displayed.

   ```bash
   QR code saved as qrcode.png
   ```

## Customization

You can customize the QR code generation by modifying the parameters in the script:

- `version`: The version of the QR code (1-40), affecting the size and data capacity.
- `error_correction`: The error correction level (constants from `qrcode.constants`).
- `box_size`: The size of each box (module) in the QR code.
- `border`: The size of the border around the QR code.
- `fill_color`: The color of the QR code modules.
- `back_color`: The background color of the QR code.

Refer to the `qrcode` library documentation for more information on available options.
