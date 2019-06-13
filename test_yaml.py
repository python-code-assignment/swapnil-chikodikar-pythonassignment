import yaml


def yaml_loader(file_path):
        """Loads a YAML file"""
        with open(file_path, "r") as file_descriptor:
            data = yaml.load(file_descriptor)
        return data


def yaml_dump(file_path, data):
    """Dumps data to a yaml file"""
    with open(file_path, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)
    return


FILE_PATH = "example1.yaml"
DATA = yaml_loader(FILE_PATH)
print DATA
