import json

def run(file_path: str):
    total = 0
    levels = {}
    keys = {}

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            total += 1
            data = json.loads(line)

            level = data.get("level", "unknown")
            levels[level] = levels.get(level, 0) + 1

            for k in data.keys():
                keys[k] = keys.get(k, 0) + 1

    print("=== Stats ===")
    print(f"Total lines: {total}")
    print("By level:")
    for lvl, count in levels.items():
        print(f"  {lvl}: {count}")
    print("Most common keys:")
    for k, count in sorted(keys.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {k}: {count}")
