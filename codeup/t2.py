a ,b,c = 3,7,9

d = 2
f = True
while f:
    if d%a==0 and d%b==0 and d%c==0:
        print(d)
        f=False
    else:
        d+=1
# print(d)