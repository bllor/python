n = int(input())

for i in range(n):
    a,b = map(int, input().split(' '))
    str = 'Case #{}: {} + {} = {}'.format(i+1,a,b,a+b)
    print(str)