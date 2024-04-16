import cv2
import pytesseract

# Configure Tesseract OCR
custom_config = r'--oem 3 --psm 6 outputbase digits'

# Function to extract 4 letters from a PNG image
def extract_letters(image_path):
    # Load image and convert to grayscale
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text
    extracted_text = pytesseract.image_to_string(gray_image, config=custom_config)

    # Process extracted text to get 4 letters
    extracted_letters = extracted_text[:4]

    return extracted_letters

# Test the function with an example PNG image
image_path = 'path_to_your_image.png'
letters = extract_letters(image_path)
print(f'Extracted letters: {letters}')
