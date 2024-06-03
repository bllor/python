c = "123 -123"
a,b = c.split(' ')
print(int(a) - int(b))

d = ['+','-','*','//']
'''
for i in len(d):
    print(1+int(d[i])+2)
이게 안되었던 이유는 len(d)으로 숫자만 출력했고 범위를 나타내지 않았기 때문
'''

for i in range(len(d)):
    print(1+int(d[i])+2)
