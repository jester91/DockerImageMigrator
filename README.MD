# Docker Image Replicator

This script automates the process of pulling Docker images from one registry, tagging them, and then pushing them to another registry. It's particularly useful for mirroring images between different environments or ensuring that private registries contain all required images.

## Prerequisites

Before running this script, ensure you have the following:

- Docker installed on your machine.
- Logged in to both the source and destination Docker registries on your machine.
- Python 3.x installed on your machine.

## Configuration

1. Open the script in a text editor.
2. Modify the `images` list to contain the names of the Docker images you want to replicate. For example:

   ```python
   images = [
     "yourimage1:tag",
     "yourimage2:tag",
     "yourimage3:tag",
   ] 
   ```
Set the source_registry and destination_registry variables to your source and destination Docker registry URLs, respectively. For example:
```
source_registry = "docker.io"
destination_registry = "your.private.registry"
```
## Usage
Ensure Docker is running on your system.

Log in to your Docker registries (source and destination) using the docker login command.

Run the script using Python:

python3 docker_image_replicator.py
Replace docker_image_replicator.py with the name of your script file, if different.

The script will iterate through each image in the images list, pull it from the source_registry, tag it with the destination_registry, and push it to the destination_registry.

## Troubleshooting

Ensure that you have the necessary permissions to access both the source and destination Docker registries.
Confirm that all image names and tags are correct.
Verify that Docker is running properly on your system.
Check your network connection if images are not pulling or pushing correctly.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.