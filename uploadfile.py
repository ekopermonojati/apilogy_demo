import streamlit as st
import requests
import base64

# Set the API endpoint URL
api_endpoint = "https://bigvision.api.apilogy.id/ekyc-ktp-extraction/1.0.0/upload/ktp-extraction"

# Set the API key
api_key = "I2kMeD9ZHFKSNMvRTmebHP68iXi8YIAN"

# Create a file uploader widget for image files
file_uploader = st.file_uploader("Select an image file to upload", type=["jpeg"])

# Create a button to trigger the upload
btn_upload = st.button("Upload Image")

if btn_upload:
    # Check if a file was selected
    if file_uploader is not None:
        # Read the file contents
        file_contents = file_uploader.read()

        # Set the API headers
        headers = {"Accept": "application/json", "Content-Type": "multipart/form-data", "x-api-key": api_key}

        # Set the API data
        data = {"image": file_contents}

        # Send the image to the API server
        response = requests.post(api_endpoint, headers=headers, files={"image": file_contents})

        # Check if the upload was successful
        if response.status_code == 200:
            # Display the response as JSON text
            st.json(response.json())
        else:
            st.error("Error uploading image:", response.text)
    else:
        st.warning("No image file selected")
