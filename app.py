import streamlit as st
import requests

# Streamlit app title
st.title("KTP Extraction Demo App")
api_key = st.text_input("License API Key")
# Instructions
st.write("Upload a KTP image, and the app will extract data using the Apilogy API.")

# File uploader for the KTP image
uploaded_file = st.file_uploader("Choose a KTP image...", type=["jpg", "jpeg", "png"])

# Check if a file has been uploaded
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded KTP Image", use_container_width=True)
    
    # Button to initiate extraction
    if st.button("Extract KTP Data"):
        # Set up the API request
        url = "https://bigvision.api.apilogy.id/ekyc-ktp-extraction/1.0.0/upload/ktp-extraction"
        headers = {
            'Accept': 'application/json',
            'x-api-key': api_key
        }
        
        # Prepare the file for upload
        files = {'image': uploaded_file}
        
        # Make the request to the API
        with st.spinner("Extracting data..."):
            response = requests.post(url, headers=headers, files=files)
        
        # Handle the response
        if response.status_code == 200:
            extracted_data = response.json()
            st.success("Data extraction successful!")
            st.json(extracted_data)  # Display extracted data in JSON format
        else:
            st.error("Data extraction failed. Please contact Telkom account manager to update your license")
else:
    st.info("Please upload a KTP image to start the extraction.")
