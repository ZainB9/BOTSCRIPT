import requests
import time
import random


# Define your variables #Change the numbers in the url to your channel id and the authorization to your token.
url = "THE URL"
payload = {'content': "THE MESSAGE"}
headers = {'authorization': 'YOUR TOKEN'}

# Set the interval in seconds (31 minutes = 1860 seconds)
random_seconds = random.randint(60, 125)
interval = 1860 + random_seconds


# Infinite loop to keep sending the message every 31 minutes
while True:
    try:
        response = requests.post(url, data=payload, headers=headers)
        response.raise_for_status()  # Check if the request was successful
        print("Message sent successfully:", response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    
    # Wait for the specified interval before sending the next message
    time.sleep(interval)
