import requests
import base64
import qrcode
from PIL import Image

def upload_image_to_imgbb(api_key, image_path, expiration=600):
    """
    Uploads an image to ImgBB and returns the hosted image URL.
    :param api_key: ImgBB API key
    :param image_path: Path to the image file
    :param expiration: Expiration time in seconds (default: 600)
    :return: Hosted image URL
    """
    url = "https://api.imgbb.com/1/upload"
    
    # Convert the image to Base64
    with open(image_path, "rb") as img_file:
        base64_image = base64.b64encode(img_file.read()).decode("utf-8")
    
    # Prepare the request payload
    payload = {
        "key": api_key,
        "expiration": expiration,
        "image": base64_image,
    }
    
    # Send the POST request to ImgBB
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.json()["data"]["url"]
    else:
        raise Exception(f"Error uploading image: {response.json()}")

def generate_qr_code(data, output_path="qr_code.png"):
    """
    Generates a QR code for the given data and saves it to a file.
    :param data: Data for the QR code (e.g., URL)
    :param output_path: Path to save the QR code image
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create and save the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_path)
    print(f"QR code saved to {output_path}")

def main():
    # Your ImgBB API key
    API_KEY = "YOUR_CLIENT_API_KEY"
    
    # Path to the image you want to upload
    IMAGE_PATH = "path_to_your_image.jpg"
    
    try:
        # Step 1: Upload image to ImgBB
        print("Uploading image to ImgBB...")
        image_url = upload_image_to_imgbb(API_KEY, IMAGE_PATH)
        print(f"Image uploaded successfully: {image_url}")
        
        # Step 2: Generate QR code for the image URL
        print("Generating QR code...")
        generate_qr_code(image_url, "image_qr_code.png")
        print("QR code generation complete.")
        
        # Step 3: Display the QR code
        qr_img = Image.open("image_qr_code.png")
        qr_img.show()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
