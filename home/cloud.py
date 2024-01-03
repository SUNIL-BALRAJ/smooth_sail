from azure.storage.blob import BlobServiceClient
import json
import os
import base64
import time
tmp=10
while tmp<22:

    # Replace these variables with your actual Azure Storage account details
    account_name = 'sihrg971a'
    account_key = 'YjBxAR0cjaINcJoOnSmsLTI5T/1ef9SKlen1M6CVDIybcui+ZfQ/Q5pSGfbh5ECCCKOlTo0kA6O9+AStM49hhQ=='
    container_name = 'sihcontainer'
    blob_name = f'sihiothub/01/2023/12/09/15/{tmp}.json'
    print(blob_name)
    local_json_file_path = 'local_data.json'


    # Create BlobServiceClient
    blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

    # Get Container Client
    container_client = blob_service_client.get_container_client(container_name)

    # Get Blob Client
    blob_client = container_client.get_blob_client(blob_name)

    # Download the JSON file from Azure Storage
    blob_data = blob_client.download_blob()
    json_data = blob_data.readall()

    # Parse the JSON data
    data_objects = [json.loads(line.decode()) for line in json_data.splitlines()]

    all_data = data_objects
    # Write combined data to the local file
    with open(local_json_file_path, 'w') as file:
        json.dump(all_data, file, indent=2)

    tmp+=1
    print(f"Data has been written to {local_json_file_path}.")

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