import subprocess

# Define the images to pull, tag, and push
images = [
"nameOfTheImage:tag",
"nameOfTheImage:tag",
"nameOfTheImage:tag",
]

# Define source and destination registries
source_registry = "source"
destination_registry = "destination"

# Loop through the images, pulling, tagging, and pushing each one
for image in images:
    source_image = f"{source_registry}/{image}"
    destination_image = f"{destination_registry}/{image.split('/')[-1]}"

    # Pull the image
    subprocess.run(["docker", "pull", source_image], check=True)

    # Tag the image
    subprocess.run(["docker", "tag", source_image, destination_image], check=True)

    # Push the image
    subprocess.run(["docker", "push", destination_image], check=True)
