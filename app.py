import os
import json
from dotenv import load_dotenv
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# the following packages are needed
# python-dotenv
# azure-storage-blob

# Load environment variables from .env file

load_dotenv()
account_name = os.environ.get('AZURE_STORAGE_ACCOUNT')
account_connection_string = os.environ.get(
    'AZURE_STORAGE_ACCOUNT_CONNECTION_STRING')

print(account_name)
print(account_connection_string)

exit()

# Initialize BlobServiceClient

blob_service_client = BlobServiceClient.from_connection_string(account_connection_string)
print ("BlobServiceClient created")

exit()

# Create a container

container_name = "bilder"
container_client = blob_service_client.get_container_client(container_name)

try:
    container_client.create_container()
    print(f"The container '{container_name}' has been created.")
except:
    print(f"The container '{container_name}' already exists.")

exit()

# Upload a file

local_filepath = "ArtIsPointless.jpeg"
blob_name = os.path.basename(local_filepath)

blob_client = container_client.get_blob_client(blob_name)

try:
    with open(local_filepath, "rb") as data:
        blob_client.upload_blob(data)
        print(f"The blob '{blob_name}' has been uploaded.")
except:
    print(f"The blob '{blob_name}' already exists.")

exit()

# Download the blob

download_filepath = "ArtIsPointless2.jpeg"

blob_client = container_client.get_blob_client(blob_name)

with open(download_filepath, "wb") as file:
    blob_data = blob_client.download_blob()
    file.write(blob_data.readall())
    print(f"The blob '{blob_name}' has been downloaded to {download_filepath}.")


