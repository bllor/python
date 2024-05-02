'''
변수 : 객체 == 자료형의 데이터와 같은 것을 의미한다.
파이썬에서는 자료형의 타입을 지정해주지 않아도 된다.
'''

#리스트 복사하기
a=[1,2,3]
b=a
c=a[:]
from copy import copy
d = copy(a)
print(b)
print(c)
print(d)
