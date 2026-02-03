import sys

doc = {}
lines = sys.stdin.read().splitlines()

n = int(lines[0])

for i in range(1, n + 1):
    parts = lines[i].split()
    cmd = parts[0]
    if cmd == "set":
        key = parts[1]
        value = parts[2]
        doc[key] = value
    elif cmd == "get":
        key = parts[1]
        if key in doc:
            print(doc[key])
        else:
            print(f"KE: no key {key} found in the document")
