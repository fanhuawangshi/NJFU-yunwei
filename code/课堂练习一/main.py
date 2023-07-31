import json

if __name__ == "__main__":
    with open("a.json", 'r') as f:
        info = json.loads(f.read())
    for k, v in info.items():
        print(k, v)
