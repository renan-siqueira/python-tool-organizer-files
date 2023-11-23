# File Organizer Tool

## Overview

This Python script efficiently organizes files into separate folders based on specific identifiers in their filenames. It's designed to simplify the task of sorting large numbers of images into distinct categories, making file management more manageable and intuitive.

## Features

- **Automatic Folder Creation:** The script creates designated folders if they don't already exist, ensuring a smooth sorting process without manual folder setup.
- **Customizable Sorting:** Users can specify the identifiers and folder names, allowing for flexible organization tailored to different needs.

## Requirements

- Python environment (Python 3.x recommended)
- `shutil` and `os` libraries (standard in Python)

## Configuration

Before running the script, ensure you have a `settings/config.py` file with a config dictionary containing at least the `APP_PATH_MAIN_FOLDER` key, which designates the base path for image organization.

## Usage

1. **Set Base Path:** Define the base path for your images in the `settings/config.py` file under `APP_PATH_MAIN_FOLDER`.

2. **Customize Identifiers and Folder Names:** In the script, set `FOLDER_NAME_1`, `FOLDER_NAME_2`, `IDENTIFIER_1`, and `IDENTIFIER_2` to match your sorting criteria.

3. **Run the Script:** Execute the script to start organizing your images:

```bash
python run.py
```

## License

This project is open-sourced and available to everyone under the [MIT License](LICENSE).
