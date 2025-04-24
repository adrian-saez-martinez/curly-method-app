import base64
import dotenv
from mistralai import Mistral

dotenv.load_dotenv()

def image_to_base64(image_file):
    try:
        # Check if the file-like object is valid
        if image_file is None:
            raise ValueError("The provided image file is None.")
        
        # Check if the file has a `read` method
        if not hasattr(image_file, "read"):
            raise ValueError("The provided image file is not a valid file-like object.")

        # Convert to base64
        base64_string = base64.b64encode(image_file.read()).decode("utf-8")
 
        return base64_string
    except Exception as e:
        raise ValueError(f"Failed to convert image to base64: {e}")
    
def extract_text_with_ocr(image_base64):
    """Call the Mistral OCR API to extract text from the image."""
    api_key = dotenv.get_key(".env", "MISTRAL_API_KEY")
    client = Mistral(api_key=api_key)

    if not image_base64.strip():
        raise ValueError("The base64 image string is empty or invalid.")

    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "image_url",
            "image_url": f"data:image/jpeg;base64,{image_base64}"
        }
    )

    # Extract text from the OCR response
    extracted_text = ""
    if hasattr(ocr_response, "pages") and ocr_response.pages:
        for page in ocr_response.pages:
            if hasattr(page, "markdown"):
                extracted_text += page.markdown + "\n"

    if not extracted_text.strip():
        raise ValueError("No text could be extracted from the OCR response.")

    return extracted_text.strip()