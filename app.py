# === Import necessary libraries ===

import streamlit as st        # Streamlit for building the interactive web interface
import qrcode                 # qrcode to generate QR code images
from io import BytesIO        # BytesIO to handle in-memory binary streams (for download functionality)
from PIL import Image         # PIL (Pillow) to manipulate and save image objects

# === Configure the web app's title and favicon ===
st.set_page_config(page_title="QR Code Generator", page_icon="🔳")  # Sets the browser tab title and icon

# === Display the main title and description on the app ===
st.title("🔳 QR Code Generator")       # Displays a title at the top of the app
st.write("Generate a permanent (static) QR code instantly!")  # Short description below the title

# === Input field for user to enter the text or URL they want to encode ===
text = st.text_input("Enter text or URL to encode:", value="https://yourwebsite.com")  
# Creates a text input box with a default URL

# === If the 'Generate QR Code' button is clicked and input is provided ===
if st.button("Generate QR Code") and text:
    
    # --- Create the QR code object with desired configuration ---
    qr = qrcode.QRCode(
        version=1,  # QR code size (1 is smallest, good for short text)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction (recovers ~30% damaged data)
        box_size=10,  # Pixel size of each box in the QR code
        border=4,  # Minimum border width (must be ≥4 for most scanners)
    )

    # --- Add user-provided data to the QR code ---
    qr.add_data(text)      # Encodes the text/URL into the QR code
    qr.make(fit=True)      # Optimizes the QR size to fit the input data
    
    # --- Create the actual image from the QR code ---
    img = qr.make_image(fill_color="black", back_color="white")  # Set colors for QR code (black on white)

    # --- Show the generated QR code image on the web app ---
    st.image(img, caption="Your QR Code", use_column_width=False)  # Display QR code image with a caption

    # --- Prepare the image for download (convert it into a memory buffer) ---
    buffered = BytesIO()                  # Create a memory buffer to hold the image binary
    img.save(buffered, format="PNG")      # Save the image in PNG format to the buffer
    
    # --- Add a download button for the user to save the QR code ---
    st.download_button(
        label="📥 Download QR Code",            # Button label
        data=buffered.getvalue(),              # Binary data of the image
        file_name="qr_code.png",               # Default filename for download
        mime="image/png"                       # MIME type to indicate it's a PNG image
    )
