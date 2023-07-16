import docker

client = docker.from_env()
images = client.images.list()

existing_versions = [float(image.tags[0].split(":")[1]) for image in images if image.tags and image.tags[0].startswith("nedm0r/flask-database")]

if existing_versions:
    latest_version = max(existing_versions)
    next_version = latest_version + 0.1
else:
    next_version = 1.0

# Format the version number to one decimal place
next_version = f"{next_version:.1f}"

image_name = f"nedm0r/flask-database:{next_version}"
client.images.build(path=".", tag=image_name, rm=True, pull=True)
print(f"Successfully built image: {image_name}")

# Push the image with the specified tag
client.images.push(repository="nedm0r/flask-database", tag=next_version)
print(f"Successfully pushed image: {image_name}")

# Push the image with the 'latest' tag
latest_tag = "latest"
latest_image_name = f"nedm0r/flask-database:{latest_tag}"
image_to_tag = client.images.get(image_name)
image_to_tag.tag(repository="nedm0r/flask-database", tag=latest_tag)
client.images.push(repository="nedm0r/flask-database", tag=latest_tag)
print(f"Successfully pushed image: {latest_image_name}")
