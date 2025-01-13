import streamlit as st
import requests

# Set the API URL
API_URL = 'https://bigvision.api.apilogy.id/ekyc-ktp-extraction/1.0.0/upload/ktp-extraction'
API_KEY = 'I2kMeD9ZHFKSNMvRTmebHP68iXi8YIAN'

# Function to send the image to the API
def send_image_to_api(image_file):
    # Prepare headers for the API request
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'x-api-key': API_KEY
    }
    
    # Prepare the files to be sent in the POST request
    files = {
        'image': image_file
    }
    
    # Send the request to the API
    response = requests.post(API_URL, headers=headers, files=files)
    
    # Return the response data in JSON format
    return response.json()

# Streamlit app UI
st.title("KTP eKYC Image Upload")

# Upload image widget
uploaded_image = st.file_uploader("Choose a KTP image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded KTP Image", use_column_width=True)
    
    # Button to trigger the API call
    if st.button("Extract Information"):
        with st.spinner("Processing..."):
            # Send the image to the API
            result = send_image_to_api(uploaded_image)
            
            # Display the result
            st.write("API Response:")
            st.json(result)


