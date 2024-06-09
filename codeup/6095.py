d=[] # 2차원 배열이 저장될 곳
for i in range(20) :
  d.append([]) #1차원 배열
  for j in range(20) : 
    d[i].append(0) #1차원 배열에 값을 0으로 넣음

n = int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1 #2차원 배열에 값을 1로 넣음

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')
  print()