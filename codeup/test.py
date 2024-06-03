c = "123 -123"
a,b = c.split(' ')
print(int(a) - int(b))

d = ['+','-','*','//']
for i in range(len(d)):
    print(1+int(d[i])+2)
