""" 
This script can be used when cameras in the network change their zoom levels over time. 
It runs in an endless loop, periodically adjusting the zoom level.

It's important to note that changing the zoom level sends an HTTP request, which can put strain on both the camera and its mechanics. 
While the camera can tolerate the mechanics not moving if the value hasn't changed, moving the mechanics every minute can cause long-term damage to the camera. 
"""

import requests
import time

# Define the base URL and the IP addresses
base_url = "http://{}/axis-cgi/opticssetup.cgi"
ip_addresses = ["192.168.1.1", "192.168.1.2", "192.168.1.3", "192.168.1.4"]

# Define the parameters
parameters = {"azoom": "0.55", "source": "1"}

# Create an endless loop
while True:
    # Loop through the IP addresses
    for ip in ip_addresses:
        # Construct the URL
        url = base_url.format(ip)

        # Make the GET request
        response = requests.get(url, auth=HTTPDigestAuth("YourUsername", "YourPassword"), params=parameters)

        # Print the response
        print(f"Response from {ip}: {response.status_code}")

        # Wait
        time.sleep(60)
