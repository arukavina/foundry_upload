# Foundry File Upload Script

This repository contains a Python script designed to upload large files to Foundry datasets, especially when other upload methods are not available. The script tracks uploaded files and avoids redundant uploads, providing a seamless experience for managing large data transfers.

---

## Features

- Upload files from a specified directory to a Foundry dataset.
- Avoid redundant uploads by tracking previously uploaded files.
- Use environment variables for configuration.
- Display progress bars for file uploads using `tqdm`.

---

## Prerequisites

Before using the script, ensure the following:

1. **Python Environment**: Install Python 3.8 or higher.
2. **Required Libraries**: Install the following Python packages:
   ```bash
   pip install foundry-dev-tools urllib3 tqdm boto3
   ```
3. **Environment Variables**: Set up the required environment variables:
   - `FOUNDRY_TOKEN`: Foundry access token.
   - `FOUNDRY_HOST`: Foundry host URL.
   - `INPUT_PATH`: Path to the directory containing the files to upload.
   - `TARGET_DATASET_RID`: Resource ID of the target Foundry dataset.

---

## Setup

### Environment Variables

The script requires the following environment variables:

- `FOUNDRY_TOKEN`: Your Foundry access token for authentication.
- `FOUNDRY_HOST`: The Foundry instance URL.
- `INPUT_PATH`: Directory containing files to be uploaded.
- `TARGET_DATASET_RID`: The resource ID of the target dataset in Foundry.

Use a `.env` file or export the variables in your shell session:
```bash
export FOUNDRY_TOKEN="your_token"
export FOUNDRY_HOST="your_host"
export INPUT_PATH="/path/to/your/files"
export TARGET_DATASET_RID="your_dataset_rid"
```

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/arukavina/foundry_upload.git
   cd foundry-file-upload
   ```

2. Set up the required environment variables as described above.

3. Place your target files in the directory specified by `INPUT_PATH`.

4. Run the script:
   ```bash
   python upload_files.py
   ```

5. Monitor the progress bars for each file being uploaded.

6. Review the `uploaded_files.json` file to track uploaded files.

---

## Script Overview

### Key Functionalities

1. **File Filtering**:
   The script scans the directory specified by `INPUT_PATH` and filters files based on their extension (default: `.rpt`). Modify the `FILE_EXTENSION` variable to target a different file type.

2. **Upload Tracking**:
   - The script tracks uploaded files using a JSON file (`uploaded_files.json`) stored in the input directory.
   - Functions `load_uploaded_files` and `save_uploaded_files` manage this tracking.

3. **File Uploads**:
   Files are uploaded to the specified Foundry dataset using an S3 client provided by the `foundry_dev_tools` library.

4. **Error Handling**:
   The script gracefully handles upload errors and continues processing other files.

### Main Upload Functionality

#### Uploading Files

The `upload_file_to_foundry` function manages the file upload process:
```python
@contextlib.contextmanager
def upload_file_to_foundry(ctx, file_path):
    boto3_client = ctx.s3.get_boto3_client(verify=False)
    file_size = file_path.stat().st_size
    path_in_dataset = file_path.name

    with tqdm(total=file_size, desc=path_in_dataset, unit="B", unit_scale=True) as pbar:
        boto3_client.upload_file(
            str(file_path), TARGET_DATASET_RID, path_in_dataset, Callback=pbar.update
        )
```

#### Final Output

At the end of the script, a list of successfully uploaded files is displayed:
```python
print("Successfully uploaded files:")
for uploaded_file in uploaded_files:
    print(uploaded_file)
```

---

## Notes

- Ensure that the `FOUNDRY_TOKEN` and `FOUNDRY_HOST` values are correct to avoid authentication issues.
- Files already listed in `uploaded_files.json` are skipped.
- Modify `FILE_EXTENSION` to target a different file type if needed.

---

## License

See the LICENSE file for details.

---

## Contributing

Contributions are welcome!
---

By using this script, you can efficiently upload large volumes of data to Foundry, bypassing other upload constraints.

