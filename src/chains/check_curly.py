from langchain_openai import ChatOpenAI
from src.prompts.prompt_curly import curly_prompt, CurlyCheckOutput
from src.utils.utils import image_to_base64

# Initialize the LLM
def initialize_llm():
    return ChatOpenAI(
        model="gpt-4o",
        temperature=0,
        max_tokens=2048,
    )

def analyze_product(uploaded_image):
    base64_image = image_to_base64(uploaded_image)
    image_content = {
        "type": "image_url",
        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
    }

    # Initialize the chat model with structured output
    llm = initialize_llm()
    structured_llm = llm.with_structured_output(CurlyCheckOutput)

    # Prepare messages
    messages = curly_prompt()
    messages[-1] = (messages[-1][0], [messages[-1][1], image_content])

    # Invoke the model and parse the structured output
    parsed = structured_llm.invoke(messages)

    return parsed