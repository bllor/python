n = int(input())

a = input().split(' ')
x= int(input())
m = 0
for i in range(n):
    if x == int(a[i]):
        m+=1
print(m)