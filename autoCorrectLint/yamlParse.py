# parse YAML file get my need info
import yaml
from yaml import Loader


def parse_yaml(yaml_file):
    file = open(yaml_file, "r", encoding="utf-8")
    file_data = file.read()
    file.close()

    data = yaml.load(file_data, Loader=Loader)
    print(data)
    return data