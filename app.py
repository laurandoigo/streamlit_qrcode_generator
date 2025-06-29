# app.py

import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# Configure the Streamlit page
st.set_page_config(page_title="QR Code Generator", page_icon="🔳")

# Title and description
st.title("🔳 QR Code Generator")
st.write("Generate a permanent (static) QR code instantly!")

# Text input for user-provided content
text = st.text_input("Enter text or URL to encode:", value="https://yourwebsite.com")

# If button is clicked and input is valid
if st.button("Generate QR Code") and text:
    # Create QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Generate the QR image
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert PIL image to bytes for rendering and download
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    # Display the image using correct parameter
    st.image(img_bytes, caption="Your QR Code", use_container_width=False)

    # Provide download button
    st.download_button(
        label="📥 Download QR Code",
        data=img_bytes,
        file_name="qr_code.png",
        mime="image/png"
    )
