import streamlit as st
from src.chains.check_curly import analyze_product

st.title("Verificador método Curly")

# File uploader for image
uploaded_image = st.file_uploader("Sube una imagen de la etiqueta del producto en la que se lean los ingredientes", type=["jpg", "jpeg", "png"])

# Camera input for image
camera_image = st.camera_input("O toma una foto de la etiqueta del producto")

# Use the uploaded image or the camera image
image_to_analyze = uploaded_image or camera_image

if image_to_analyze and st.button("Verificar producto"):
    with st.spinner("Analizando..."):
        result = analyze_product(image_to_analyze)
        st.subheader("✅ APTO ✅" if result.valid else "❌ NO APTO ❌")
        st.write(result.analysis)
