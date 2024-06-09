# 2차원 배열 생성
d=[]
for i in range(20) :
  d.append([])
  for j in range(20) : 
    d[i].append(0)

#입력되는 바둑판을 d에 저장
#한 번에 모든 바둑판들이 들어올 것이라 생각해서 a = input().split()로 배열을 받을 수 있다고 생각했었음
for i in range(19) :
  a = input().split()
  for j in range(19) :
    d[i+1][j+1] = int(a[j])

n = int(input())
for i in range(n) :
  x,y=input().split()
  x=int(x)
  y=int(y)
  for j in range(1, 20) :
    if d[j][y]==0 :
      d[j][y]=1
    else :
      d[j][y]=0

    if d[x][j]==0 :
      d[x][j]=1
    else :
      d[x][j]=0

for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print()

