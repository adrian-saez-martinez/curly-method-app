# Usa una imagen oficial de Python
FROM python:3.12-slim

# Crea el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expón el puerto de Streamlit
EXPOSE 8501

# Comando para arrancar Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
