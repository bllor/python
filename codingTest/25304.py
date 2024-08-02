totalPrice = int(input())
totalItemNo = int(input())

for i in range(totalItemNo):
    price, no = map(int,input().split(' '))
    totalPrice -= price*no

if totalPrice ==0:
    print('Yes')
else:
    print('No')