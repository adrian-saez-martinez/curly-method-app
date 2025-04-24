from pydantic import BaseModel, Field
from typing import List
import dotenv
from src.data.forbidden_ingredients import FORBIDDEN_INGREDIENTS

dotenv.load_dotenv()

class CurlyCheckOutput(BaseModel):
    """Análisis del producto en base a los ingredientes y el método curly"""

    product: bool = Field(..., description="True si aparece una lista de ingredientes")
    valid: bool = Field(..., description="True si el producto es apto para el método Curly Girl")
    ingredients: List[str] = Field(..., description="Lista de ingredientes detectados")
    forbidden_ingredients: List[str] = Field(..., description="Ingredientes no aptos detectados")
    analysis: str = Field(..., description="Análisis completo.")

def curly_prompt():
    forbidden_list = ", ".join(FORBIDDEN_INGREDIENTS)
    return [
        (
            "system",
            (
                "Eres un experto en el método Curly Girl.\n\n"
                "Tu tarea es analizar un texto que ha sido obtenido de una imagen. "
                "Con base en los ingredientes proporcionados, debes decidir si el producto es apto o no para el método Curly Girl.\n\n"
                "Para ello, utiliza únicamente la siguiente lista como ingredientes no aptos:\n"
                f"{forbidden_list}\n\n"
                "No hagas referencia a la lista proporcionada, utilizala como si fuera parte de tu conocimiento.\n\n"
                "Si el texto no contiene ninguno de estos ingredientes, el producto es apto. "
                "De lo contrario, el producto No es apto, e indica cuáles son los ingredientes no aptos encontrados."
                "Si el usuario no proporciona una lista de ingredientes a analizar, responde indicando que la imagen no es válida o que no se pueden analizar los ingredientes."
            ),
        ),
        ("user", "Analiza la siguiente lista de ingredientes."),
    ]