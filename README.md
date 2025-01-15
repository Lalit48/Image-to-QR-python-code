# Image Upload and QR Code Generator

This Python project allows you to upload an image to **ImgBB**, generate a hosted URL for the image, and create a QR code pointing to the hosted image URL. Scanning the QR code opens the image in a browser.

---

## Features

- Uploads images to **ImgBB**.
- Generates a public URL for the uploaded image.
- Creates a QR code pointing to the hosted image.
- Saves the QR code as an image file.
- Displays the QR code for easy scanning.

---

## Prerequisites

- Python 3.7 or later
- An active **ImgBB API key** (Sign up for free at [ImgBB API](https://imgbb.com/)).

---

## Installation

1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/your-username/image-upload-qr-generator.git
   cd image-upload-qr-generator
   ```

2. Install required Python libraries:
   ```bash
   pip install requests qrcode pillow
   ```

---

## Usage

1. Open the script (`image_qr_generator.py`) in any code editor.

2. Replace the placeholder `YOUR_CLIENT_API_KEY` with your actual ImgBB API key:
   ```python
   API_KEY = "YOUR_CLIENT_API_KEY"
   ```

3. Set the path to the image you want to upload:
   ```python
   IMAGE_PATH = "path_to_your_image.jpg"
   ```

4. Run the script:
   ```bash
   python image_qr_generator.py
   ```

5. Output:
   - The uploaded image URL will be displayed in the terminal.
   - The QR code will be saved as `image_qr_code.png` in the current directory.
   - The QR code will be displayed on your screen for scanning.

---

## Example Output

- **Image:**  
  ![path_to_your_image](https://github.com/user-attachments/assets/dde98056-d15f-48be-9cf9-493897e2d1ef)



- **Generated QR Code:**  
  ![image_qr_code](https://github.com/user-attachments/assets/d97dcf43-ae77-444f-896a-8c4ff4d04dd6)


---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [ImgBB](https://imgbb.com/) for providing a free image hosting API.
- [qrcode](https://pypi.org/project/qrcode/) and [Pillow](https://pillow.readthedocs.io/) for QR code generation and image manipulation.

