import json


def write_json(data):
    json_data = json.dumps(data, indent=4)
    with open("users.json", "w") as json_file:
        json_file.write(json_data)


def read_json():
    with open("users.json", "r") as json_file:
        data = json.load(json_file)
        return data


