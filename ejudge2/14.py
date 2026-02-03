n = int(input())
a = list(map(int, input().split()))

cnt = {}

for x in a:
    if x in cnt:
        cnt[x] += 1
    else:
        cnt[x] = 1

max_count = 0
answer = a[0]

for x in cnt:
    if cnt[x] > max_count:
        max_count = cnt[x]
        answer = x
    elif cnt[x] == max_count and x < answer:
        answer = x

print(answer)
