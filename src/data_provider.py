import json
from pathlib import Path


class JSONDataProvider:

    @staticmethod
    def load_from_file(file_name:str):
        path = Path(file_name)
        if not path.exists():
            print(f"{file_name} not found. Please create the file with supplier data.")
            return None
        with open(path, "r") as f:
            data = json.load(f)
        return data