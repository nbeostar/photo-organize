# Photo Sorter

## Introduction
Photo Sorter is a Python utility that organizes your photo collection into folders based on the EXIF timestamp data. It also renames the files using a combination of the photo's timestamp and a SHA-256 hash of the file content to ensure uniqueness.

## Features
- Extracts EXIF timestamp data from images to determine their creation date.
- Sorts photos into folder structures based on their creation date.
- Renames photos using their timestamp and a hash of their content.
- Supports recursive directory traversal to organize photos in nested folders.

## Requirements
- Python 3.6 or later
- External libraries: `exif`, `hashlib`, `argparse`, `shutil`, `os`, `datetime`

## Installation
1. Ensure that Python 3.6+ is installed on your system.
2. Clone this repository or download the source code.
3. Navigate to the project directory and create a virtual environment:

```python -m venv venv```

4. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`
5. Install the required dependencies:

```pip install -r requirements.txt```

## Usage
To use Photo Sorter, run the script from the command line with the source and destination directories as arguments. You can also specify the `-r` flag to enable recursive sorting of photos in subdirectories.

### Basic Usage
```python photo_sorter.py <source_directory> <destination_directory>```

### Recursive Sorting
```python photo_sorter.py <source_directory> <destination_directory> -r```

Replace `<source_directory>` with the path to the directory containing your photos, and `<destination_directory>` with the path where you want the sorted and renamed photos to be placed.

## Running with Docker

This section guides you through the process of building and running the Photo Sorter application using Docker.

### Building the Docker Image

To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

```docker build -t photo_sorter .```

This command builds a new Docker image named photo_sorter based on the instructions in your Dockerfile.

### Running the Docker Container
After the image is built, you can run the application in a Docker container. Since the Photo Sorter requires access to directories on your host system for source and destination paths, you'll need to mount these directories when starting the container:

```
docker run -v /path/to/source:/src -v /path/to/destination:/dest photo_sorter
```
Replace /path/to/source with the path to the directory containing your photos, and /path/to/destination with the path where you want the sorted and renamed photos to be placed.

### Notes

- Ensure your Python application (`photo_sorter.py`) is properly configured to parse command-line arguments for source and destination directories, as the Docker container will pass these arguments when it starts.
- The Docker `RUN` command in the `Dockerfile` assumes you have a `requirements.txt` file listing all necessary Python packages.
- The `docker run` command example above assumes that your script is set up to take source and destination directory paths as command-line arguments. Adjust the paths and script options as necessary for your project.

## Contributing
Contributions to the Photo Sorter project are welcome. Please feel free to report any bugs, suggest features, or submit pull requests.

## License
[MIT License](LICENSE)
