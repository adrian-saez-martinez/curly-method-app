import streamlit as st
from src.chains.check_curly import analyze_product
from src.utils.utils import image_to_base64
import dotenv

dotenv.load_dotenv()

st.title("Verificador curly")

# File uploader for image
uploaded_image = st.file_uploader("Sube una imagen con la etiqueta del producto en la que se lean los ingredientes", type=["jpg", "jpeg", "png"])

# Camera input for image
camera_image = st.camera_input("O toma una foto de la etiqueta del producto")

# Use the uploaded image or the camera image
image_to_analyze = uploaded_image or camera_image

if image_to_analyze and st.button("Verificar producto"):
    with st.spinner("Analizando..."):
        result = analyze_product(image_to_analyze)
        if not result.product:
            st.subheader("⚠️ IMAGEN NO VÁLIDA ⚠️")
        elif result.valid:
            st.subheader("✅ APTO ✅")
        else:
            st.subheader("❌ NO APTO ❌")
        st.write(result.analysis)
        if result.ingredients:
            st.write("Listado completo de ingredientes detectados:")
            st.write(", ".join(result.ingredients))
