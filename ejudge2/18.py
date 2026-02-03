n = int(input())

a = []
for i in range(n):
    s = input()
    a.append(s)

first_index = {}
for i in range(n):
    if a[i] not in first_index:
        first_index[a[i]] = i + 1 

keys = list(first_index.keys())
keys.sort()

for s in keys:
    print(s, first_index[s])
