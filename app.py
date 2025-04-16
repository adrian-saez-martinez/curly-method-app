import streamlit as st
from src.chains.check_curly import analyze_product
import dotenv

dotenv.load_dotenv()

st.title("Verificador curly")

# File uploader for image
uploaded_image = st.file_uploader("Subee una imagen con l etiqueta del producto en la que see lean los ingredientes", type=["jpg", "jpeg", "png"])

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
