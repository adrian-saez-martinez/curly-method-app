# 🔠 Curly Verifier

Curly Verifier is an AI-powered app that helps users determine whether a hair product is suitable for the **Curly Girl Method**. By scanning the ingredient list, the app identifies disallowed substances like silicones, drying alcohols, and sulfates.

The app is designed to simplify ingredient analysis and empower users to make better hair care decisions.

## ✨ Features

- ✅ Check product ingredients for Curly Girl Method compatibility
- 📷 Upload a **photo** of the ingredient list for instant analysis
- 🔍 Uses **OpenAI Vision API** for and ingredient extraction and evaluation
- ☁️ Deployed on **Azure App Service**
- ⚙️ Built with **Streamlit** for the frontend

## 💡 Tech Stack

- **Streamlit** — Web interface
- **Azure App Service** — Deployment platform
- **OpenAI API** — Language model + Vision API for ingredients extraction and analysis
- **Python** — Core logic and backend

## 🚀 Live App

Try it out here: [https://your-deployed-url.azurewebsites.net](https://your-deployed-url.azurewebsites.net)

## 🔍 How It Works

1. User uploads a **photo** of a product's ingredient list.
2. The app uses the **OpenAI Vision API** to extract text (OCR).
3. It preprocesses the ingredients and filters known disallowed substances.
4. The app constructs a prompt combining ingredients and user input (if any).
5. The **OpenAI API** generates a final assessment: **Curly-friendly or not**.

## 🧪 Future Ideas

- Integrate RAG for enhanced contextual retrieval
- Barcode scanning for automatic ingredient lookup
- Chatbot integration for personalized haircare advice
- Community rating and reviews
- Custom dataset for improved accuracy in ingredient classification

## 📬 Contact

For feedback or collaboration opportunities:

- LinkedIn: [Adrián Sáez Martínez](https://www.linkedin.com/in/adrian-saez-martinez/)
- Email: adriansaezmartinez@email.com

