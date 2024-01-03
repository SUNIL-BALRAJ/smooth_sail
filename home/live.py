import json
import requests
import os
while True:
    base_url = 'https://api.thingspeak.com/channels/2375718/feeds.json?api_key=ATHYX1B78TCPT7W6&results=2'
    params = {'results': 1}
    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json() 


    # Write the updated data back to the file
    with open(r'C:\Users\sumit\OneDrive\Desktop\investor_hack\static\assets\thingspeak_data.json','w') as file:
        json.dump(data, file, indent=2)