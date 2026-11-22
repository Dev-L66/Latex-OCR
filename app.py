import streamlit as st
from image_util import image_path
from latex_ocr import extract_latex

st.title("Latex OCR")
st.write("Convert mathematical images into LaTeX.")

uploaded_file = st.file_uploader("Upload an image to extract the Latex code", type=["png", "jpg", "jpeg", "webp"])

if uploaded_file:

    st.image(uploaded_file, caption="Uploaded equation")

    if st.button("Extract Latex"):
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getvalue())
        encoded_image, mime_type = image_path(uploaded_file.name)

        with st.spinner("Extracting Latex from image .."):
            result = extract_latex(encoded_image, mime_type)

            if result.strip() == "NO_EQUATION_FOUND":
                st.warning("No mathematical equation found in this image.")
            
            else:    
                st.subheader("Extracted Latex")
                st.code(result, language="latex")
                st.subheader("Rendered Equation")
                st.latex(result)

        