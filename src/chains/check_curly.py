from langchain_openai import ChatOpenAI
from src.prompts.prompt_curly import curly_prompt, CurlyCheckOutput
from src.utils.utils import image_to_base64, extract_text_with_ocr
import dotenv

dotenv.load_dotenv()

# Initialize the LLM
def initialize_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=2048,
    )

def analyze_product(uploaded_image):
    """Analyze the product using OCR and OpenAI."""
    try:
        # Convert image to base64
        base64_image = image_to_base64(uploaded_image)  # Ensure this is the file-like object

        # Step 1: Extract text using Mistral OCR
        extracted_text = extract_text_with_ocr(base64_image)
        if not extracted_text.strip():
            raise ValueError("No se detectó texto en la imagen.")

        # Step 2: Use ChatOpenAI with structured output to analyze the extracted ingredients
        llm = initialize_llm()
        structured_llm = llm.with_structured_output(CurlyCheckOutput)

        # Prepare messages
        messages = curly_prompt()
        user_query = f"{messages[-1][1]} Texto detectado en la imagen: {extracted_text}"
        messages[-1] = (messages[-1][0], user_query)

        # Invoke the model and parse the structured output
        parsed = structured_llm.invoke(messages)

        return parsed
    except ValueError as ve:
        raise RuntimeError(f"Validation error during analysis: {str(ve)}")
    except Exception as e:
        raise RuntimeError(f"Unexpected error during analysis: {str(e)}")