from google.cloud import storage
import io
from PIL import Image
from google.cloud import storage
from google.oauth2 import service_account

def read_image_from_gcp_bucket(bucket_name, file_name, credentials_path):

    credentials = service_account.Credentials.from_service_account_file(credentials_path)

    # Create a storage client
    client = storage.Client(credentials=credentials)

    # Get the bucket
    bucket = client.get_bucket(bucket_name)

    # Get the blob (file) from the bucket
    blob = bucket.blob(file_name)

    # Download the contents of the blob as bytes
    content = blob.download_as_bytes()

    # Create an in-memory file object from the bytes
    file_object = io.BytesIO(content)

    # Open the image using PIL library
    image = Image.open(file_object)
    print("hello world")

    # Display or process the image as needed
    image.show()

# Specify your GCP bucket name and file name (replace with your values)
bucket_name = "bucket_from_terraform_pranav_reddy"
file_name = "random_name"
credentials_path = "key.json"

# Call the function to read the image from the GCP bucket
read_image_from_gcp_bucket(bucket_name, file_name, credentials_path)

