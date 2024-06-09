h, w = map(int, input().split())

d2=[]
for i in range(h):
    d2.append([])
    for j in range(w):
        d2[i].append(0)

n = int(input())

for i in range(n):
    l,d,x,y = map(int, input().split())
    if d == 0 :
        for j in range(l):
            d2[x-1][y-1+j]=1 # x,y가 0,0부터 시작되지 않으므로 0으로 저장될 수 있게 1을 빼줌
    else:
        for j in range(l):
            d2[x-1+j][y-1]=1
            
for i in range(h):
    for j in range(w):
        print(d2[i][j], end= ' ')
    print()