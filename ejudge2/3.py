n = int(input())            
arr = []                     

for i in range(n):        
    x = int(input())         
    arr.append(x)

s = 0
for i in range(n):           
    s += arr[i]

print(s)
