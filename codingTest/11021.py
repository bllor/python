n = int(input())

for i in range(n):
    a,b = map(int, input().split(' '))
    str = 'case #{}: {}'.format(i+1,a+b)
    print(str)