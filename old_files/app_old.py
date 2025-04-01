import streamlit as st
import base64
from openai import OpenAI
from io import BytesIO

# Initialize OpenAI client
client = OpenAI()

import streamlit as st
import base64
from openai import OpenAI
from io import BytesIO

# Initialize OpenAI client
client = OpenAI()

st.title("Verificador Curly")

# File uploader con etiqueta personalizada
uploaded_image = st.file_uploader("Sube una imagen de la etiqueta del producto en la que se lean los ingredientes", type=["jpg", "jpeg", "png"])

if uploaded_image:
    st.image(uploaded_image, use_container_width=True)

    if st.button("Verificar producto"):
        with st.spinner("Analizando..."):
            image_bytes = uploaded_image.read()
            base64_image = base64.b64encode(image_bytes).decode("utf-8")

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "Extrae y enumera los ingredientes que aparecen en esta imagen de etiqueta de producto. Luego dime si es apto para el método Curly Girl, explicando por qué"
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                        },
                    ],
                }],
                max_tokens=1000
            )

            result = response.choices[0].message.content
            st.subheader("Resultado del análisis:")
            st.write(result)
