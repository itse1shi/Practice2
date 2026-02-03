n = int(input())              
arr = input().split()

for i in range(n):
    arr[i] = int(arr[i])

m = 0
for i in range(n):
    if arr[i] > m:
        m = arr[i]      

print(m)
