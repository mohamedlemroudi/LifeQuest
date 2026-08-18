import json
from pathlib import Path

class JsonStorage:
    BASE_DIR = Path(__file__).resolve().parent.parent
    basic_path = BASE_DIR / "data"

    def __init__(self, file_path):
        self.file_path = self.basic_path / file_path

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            if isinstance(data, dict):
                data = [data]

        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        return data


    def save(self, data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
