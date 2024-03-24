## Overview

The Docker image for the Photo Sorter application is available on Docker Hub under the repository nbeo/photo-sorter. This image packages the Photo Sorter application, allowing users to easily run the application in any environment that supports Docker, without the need for a local Python environment or managing dependencies.

## Image Repository
The Docker image can be found at:

``nbeo/photo-sorter:tagname``
Replace tagname with the specific version tag you wish to use. For the latest version, you can use latest as the tag.

## Prerequisites
Before you can run the Docker image, ensure you have Docker installed on your system. Docker installation guides for various platforms are available at Docker's official documentation.
## Running the Docker Image
To run the Photo Sorter Docker image, you will need to mount the source and destination directories from your host system to the Docker container. This allows the Photo Sorter application inside the container to access and process your photos.

Here is a basic command to run the Docker image, assuming you are using the latest tag:

```docker run -v /path/to/your/source:/src -v /path/to/your/destination:/dest nbeo/photo-sorter:latest /src /dest```

Replace /path/to/your/source with the absolute path to the directory containing the photos you wish to sort. Similarly, replace /path/to/your/destination with the absolute path to the directory where you want the sorted photos to be placed.

If your application supports additional arguments or flags (e.g., for recursive processing), you can include them at the end of the command.

## Updating the Image
To ensure you are using the latest version of the Photo Sorter application, you can pull the latest image from Docker Hub by running:

```docker pull nbeo/photo-sorter:latest```

Alternatively, replace latest with a specific version tag if you wish to use a particular version of the application.

## Support and Contributions
For support, additional information, or to contribute to the Photo Sorter project, please visit the project's GitHub repository or contact the maintainer directly. Contributions, bug reports, and feature requests are welcome.

## License
The Photo Sorter Docker image and its contents are licensed under the terms specified in the project's repository. Please review the license for more details on using, modifying, and distributing the software.

