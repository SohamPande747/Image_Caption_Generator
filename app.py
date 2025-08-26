import streamlit as st
from PIL import Image
from model import generate_image_caption, model  # import your function and model

st.title("Image Caption Generator")
st.write("Upload or drag-and-drop an image and click 'Generate Caption'.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        # Save uploaded file temporarily
        temp_path = f"temp_{uploaded_file.name}"
        image.save(temp_path)

        # Show spinner while generating caption
        with st.spinner("Generating caption..."):
            caption = generate_image_caption(temp_path, model)

        st.success("Caption Generated!")
        st.write(f"**Caption:** {caption}")

        # Clean up temp file
        import os
        os.remove(temp_path)
