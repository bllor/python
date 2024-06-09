m=[]
for i in range(12) : # 개미집은 10*10의 크기이지만 1로 둘러 쌓여 있으므로 12 = 1+10+1 로 해주어야 한다.
    m.append([])
    for j in range(12) :
        m[i].append(0)
        
for i in range(10) :
    a=input().split()
    for j in range(10) :
        m[i+1][j+1]=int(a[j]) #개미집이 1에 둘러쌓여 있으므로 첫 번째 수는 0번이 아닌 1번부터 들어가야 한다.

x = 2
y = 2
while True :
    if m[x][y] == 0 : #이동경로를 나타내는 코드
        m[x][y] = 9
    elif m[x][y] == 2 :
        m[x][y] = 9
        break

    if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
        break # 끝에 도착했을 때 그만 두게 만드는 코드

    #장애물을 회피하는 코드
    if m[x][y+1] != 1 : 
        y += 1
    elif m[x+1][y] != 1 :
        x += 1
    
for i in range(1, 11) :
    for j in range(1, 11) :
        print(m[i][j], end=' ')
    print()