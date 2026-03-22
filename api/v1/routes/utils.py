import json
import os

def load_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found at {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)

def save_config(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)