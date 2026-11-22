# LaTeX OCR – AI-Powered Mathematical Equation Extractor

An AI-powered image-to-LaTeX application that extracts mathematical equations from images using a vision-language model.

Built with Python, Streamlit, and Groq API.

## Overview

LaTeX OCR converts mathematical equations from images into LaTeX code.

Users can upload an image through an interactive Streamlit interface. The application processes the image, sends it to a vision-language model through the Groq API, and returns the extracted LaTeX expression.

The extracted expression can also be rendered directly in the application for easy preview.

## Features

- **Image Upload:** Upload images containing mathematical equations.
- **Image Validation:** Validate image paths and supported image formats.
- **Base64 Encoding:** Encode images for API transmission.
- **AI-Powered OCR:** Use a vision-language model to recognize mathematical expressions.
- **LaTeX Extraction:** Convert recognized equations into LaTeX code.
- **Equation Preview:** Render extracted LaTeX directly in the Streamlit interface.

## Tech Stack

- Python
- Streamlit
- Groq API
- Vision-Language Models
- OpenAI Python SDK
- Base64
- python-dotenv

## Project Structure

```text
Latex-OCR/
│
├── app.py              # Streamlit frontend
├── config.py           # API configuration
├── image_util.py       # Image validation and encoding
├── latex_ocr.py        # AI-powered LaTeX extraction
├── main.py             # Standalone backend testing
├── equation.png        # Sample equation image
├── requirements.txt    # Project dependencies
├── .gitignore
└── README.md
```

## How It Works

1. The user uploads an image through the Streamlit interface.
2. The image is validated for supported formats.
3. The image is converted into Base64 encoding.
4. The encoded image is sent to the Groq API.
5. The vision-language model analyzes the image and extracts mathematical expressions.
6. The generated LaTeX code is displayed in the application.
7. Streamlit renders the mathematical expression for preview.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Dev-L66/Latex-OCR.git

cd Latex-OCR
```

### 2. Create a virtual environment

Using uv:

```bash
uv venv
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Get your API key from [Groq Console](https://console.groq.com/).

### 5. Run the application

```bash
uv run streamlit run app.py
```

Open the application in your browser:

```text
http://localhost:8501
```

## Usage

1. Launch the Streamlit application.
2. Upload an image containing a mathematical equation.
3. Click the **Extract LaTeX** button.
4. View the extracted LaTeX code.
5. Preview the rendered mathematical expression.

## Environment Variables

| Variable | Description
