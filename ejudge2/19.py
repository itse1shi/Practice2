n = int(input())

doramas = {}

for _ in range(n):
    s, k = input().split()
    k = int(k)
    if s in doramas:
        doramas[s] += k
    else:
        doramas[s] = k

keys = list(doramas.keys())
keys.sort()

for s in keys:
    print(s, doramas[s])
