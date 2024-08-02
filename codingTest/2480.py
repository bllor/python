a,b,c = [5,5,5]

ab,ac,bc = a==b, a==c, b==c
dic = [ab,ac,bc]
no = 0
for i in dic:
    if i:
        no +=1
# print(no)

if no ==3:
    print(10000+a*1000)
elif no ==1:
    for i in range(len(dic)):
        if dic[i]:
            if i ==0:
                print(1000+a*100)
            else:
                print(1000+c*100)
            break
else:
    max = a
    cno = b
    if b<c:
        cno = c
    if max<cno:
        max = cno
    print(max*100)