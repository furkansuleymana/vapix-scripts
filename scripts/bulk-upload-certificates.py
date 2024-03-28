"""
This script installs all certificates in a single folder on the camera. 

Before using this script, please verify that your certificate is compatible by attempting to install it via the web interface. 
If you are unable to install the certificate via the web interface, it will not work with this script either.
"""

import os
import requests
from requests.auth import HTTPDigestAuth
from xml.etree import ElementTree as ET


def send_soap_request(url, xml_file):
    # Read XML file
    with open(xml_file, "rb") as f:
        xml_data = f.read()

    # Send POST request
    response = requests.post(
        url, auth=HTTPDigestAuth("YourUsername", "YourPassword"), data=xml_data
    )
    print(f"Status code: {response.status_code}")


# Define cert folder path
folder_path = "PathToCertificates"

# Loop through files in the folder
for filename in os.listdir(folder_path):
    # Only if it is an XML file
    if filename.endswith(".xml"):
        # Construct full path
        file_path = os.path.join(folder_path, filename)

        # Define API URL
        url = "http://DeviceIPAddress/vapix/services"

        # Send request
        send_soap_request(url, file_path)
        print(f"Sent request for {filename} successfully.")
