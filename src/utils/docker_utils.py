import docker

def get_image_layers(image_name):
    client = docker.from_env()
    image = client.images.get(image_name)
    return [layer['CreatedBy'] for layer in image.history()]

def get_container_env_vars(container_id):
    client = docker.from_env()
    container = client.containers.get(container_id)
    return container.attrs['Config']['Env']

def run_command_in_container(container_id, command):
    client = docker.from_env()
    container = client.containers.get(container_id)
    return container.exec_run(command)