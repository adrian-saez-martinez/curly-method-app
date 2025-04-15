from pydantic import BaseModel, Field
from typing import List
import dotenv

dotenv.load_dotenv()

class CurlyCheckOutput(BaseModel):
    """Análisis del producto en base a los ingredientes y el método curly"""

    product: bool = Field(..., description="True si aparece un producto en la imagen")
    valid: bool = Field(..., description="True si el producto es apto para el método Curly Girl")
    #ingredients: List[str] = Field(..., description="Lista de ingredientes detectados")
    analysis: str = Field(..., description="Análisis completo del producto, incluyendo aquellos ingredientes no aptos, si los hubiera.")

def curly_prompt():
    return [
        ("system", "Eres un experto en el método Curly Girl. Tendrás que analizar una imagen y en base a los ingredientes decidir si el producto es apto o no para el método Curly."),
        ("user", "Analiza la etiqueta del producto y devuelve el resultado en el formato estructurado.")
    ]