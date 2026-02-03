n = int(input())
arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])

arr.sort(reverse=True)

for i in range(n):
    print(arr[i], end=' ')
print()
