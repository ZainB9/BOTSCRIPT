import requests
import time
import random
import threading

def send():
    url = "url"
    payload = {'content': "message"}
    headers = {'authorization': 'your token'}
    interval = 960  # 16 minutes = 960 seconds
    
    while True:
        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()  # Check if the request was successful
            print("Claim message sent successfully:", response.json())
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")
        
        time.sleep(interval)

def send_play():
    url = "url"
    payload = {'content': "message"}
    headers = {'authorization': 'your token'}
    interval = 1860 + random.randint(0, 75)  # 31 minutes + random seconds

    while True:
        try:
            response = requests.post(url, data=payload, headers=headers)
            response.raise_for_status()  # Check if the request was successful
            print("Playchallenge message sent successfully:", response.json())
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        time.sleep(interval)

# Run both functions in parallel
threading.Thread(target=send).start()
threading.Thread(target=send_play).start()
