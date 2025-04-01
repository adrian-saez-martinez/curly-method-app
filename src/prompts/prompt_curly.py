from pydantic import BaseModel, Field
from typing import List

class CurlyCheckOutput(BaseModel):
    """Análisis del producto en base a los ingredientes y el método curly"""

    valid: bool = Field(..., description="True si el producto es apto para el método Curly Girl")
    ingredients: List[str] = Field(..., description="Lista de ingredientes detectados")
    analysis: str = Field(..., description="Análisis completo del producto, incluyendo aquellos ingredientes no aptos, si los hubiera.")

def curly_prompt():
    return [
        ("system", "Eres un experto en el método Curly Girl."),
        ("user", "Analiza la etiqueta del producto y devuelve el resultado en el formato estructurado.")
    ]