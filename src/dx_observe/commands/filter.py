import json

def run(file_path: str, level: str = None, contains: str = None):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)

            if level and data.get("level") != level:
                continue

            if contains and contains.lower() not in json.dumps(data).lower():
                continue

            print(json.dumps(data))
