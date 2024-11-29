from foundry_dev_tools import FoundryContext, JWTTokenProvider
import contextlib
import urllib3
from pathlib import Path
from tqdm import tqdm
import os
import json

# Suppress only the single warning from urllib3.
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

# Read the token and host from environment variables
TOKEN = os.getenv("FOUNDRY_TOKEN")
HOST = os.getenv("FOUNDRY_HOST")

if not TOKEN:
    raise ValueError("The environment variable 'FOUNDRY_TOKEN' is not set")
if not HOST:
    raise ValueError("The environment variable 'FOUNDRY_HOST' is not set")

# Foundry Target RID
TARGET_DATASET_RID = "ri.foundry.main.dataset.d2a0bda7-1751-47b4-b275-217aee0a8c22"

# Directory to scan
DIRECTORY = Path(r"C:\Users\arukavina\Downloads\25 New Data")
# File extension to filter
FILE_EXTENSION = ".rpt"  # Change this to the desired file extension

# Status file to keep track of uploaded files
STATUS_FILE = DIRECTORY / "uploaded_files.json"


# Load the list of already uploaded files from the status file
def load_uploaded_files():
    if STATUS_FILE.exists():
        with open(STATUS_FILE, "r") as f:
            return set(json.load(f))
    return set()


# Save the list of uploaded files to the status file
def save_uploaded_files(uploaded_files):
    with open(STATUS_FILE, "w") as f:
        json.dump(list(uploaded_files), f)


@contextlib.contextmanager
def upload_file_to_foundry(ctx, file_path):
    boto3_client = ctx.s3.get_boto3_client(verify=False)
    file_size = file_path.stat().st_size
    path_in_dataset = file_path.name

    with tqdm(total=file_size, desc=path_in_dataset, unit="B", unit_scale=True) as pbar:
        boto3_client.upload_file(
            str(file_path), TARGET_DATASET_RID, path_in_dataset, Callback=pbar.update
        )


# Initialize Foundry context
ctx = FoundryContext(token_provider=JWTTokenProvider(host=HOST, jwt=TOKEN))

# Load previously uploaded files
uploaded_files = load_uploaded_files()

# Loop through the contents of the directory and upload new files
for file in DIRECTORY.iterdir():
    if file.is_file() and file.suffix == FILE_EXTENSION and file.name not in uploaded_files:
        try:
            print(f"Uploading: {file.name}")

            upload_file_to_foundry(ctx, file)

            # Mark the file as uploaded
            uploaded_files.add(file.name)
            # Save the updated list of uploaded files
            save_uploaded_files(uploaded_files)

        except Exception as e:
            print(f"Failed to upload {file.name}: {e}")

# Print the list of successfully uploaded files
print("Successfully uploaded files:")
for uploaded_file in uploaded_files:
    print(uploaded_file)
