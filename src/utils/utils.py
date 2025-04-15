import base64
import dotenv

dotenv.load_dotenv()

def image_to_base64(image_file):
    return base64.b64encode(image_file.read()).decode("utf-8")