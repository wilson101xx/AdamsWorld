from user_interface import start_applications
import os
import logging
import requests

logging.basicConfig(level=logging.INFO)

def main():
    file_path = "documents/AdamWilsonCV.pdf"
    file_name = os.path.basename(file_path)  # Extracts 'AdamWilsonCV.pdf'

    # Open the file in binary mode using a context manager
    with open(file_path, "rb") as f:
        files = {
            "file1": (file_name, f),  # Use 'file_name' instead of 'file_path'
        }

        # Additional data you might want to pass along with the file
        data = {
            "documentId": "doc_adamscv",  # Adjust the documentId as needed
        }

        # Make a POST request to upload the file to the /upload endpoint
        response = requests.post("http://kernel_memory:9001/upload", files=files, data=data)

        # Log the response
        logging.info(response.text)

if __name__ == "__main__":
    main()
    start_applications()
