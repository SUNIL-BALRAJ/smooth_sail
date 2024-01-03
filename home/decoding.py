import base64
import json
import time

while True:
    # File paths
    input_file_path = 'local_data.json'  # Replace with the actual path
    output_file_path = 'decoded.json'  # Replace with the desired output path

    # Read data from local_data.json
    with open(input_file_path, 'r') as file:
        data = json.load(file)

    decoded_bodies = []

    # Extract 'Body' from each JSON object and perform base64 decoding
    for item in data:
        encoded_body = item.get("Body")
        decoded_bytes = base64.b64decode(encoded_body)
        decoded_string = decoded_bytes.decode('utf-8')
        decoded_json = json.loads(decoded_string)
        decoded_bodies.append(decoded_json)

    # Write the decoded content to another JSON file
    with open(output_file_path, 'w') as output_file:
        json.dump(decoded_bodies, output_file, indent=2)

    print(f'Decoded content has been written to {output_file_path}.')
    time.sleep(5)
