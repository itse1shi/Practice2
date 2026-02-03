n = int(input())

cnt = {}

for _ in range(n):
    number = input()
    if number in cnt:
        cnt[number] += 1
    else:
        cnt[number] = 1

answer = 0
for number in cnt:
    if cnt[number] == 3:
        answer += 1

print(answer)
