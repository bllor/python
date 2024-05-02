'''
for문
for문의 기본 구조
for 변수 in 리스트(or 튜플 or 문자열):
'''

#1. for문과 continue문
# for문 안의 문장을 수행하는 도중 continue
for i in [1,2,3,4,5]:
    if i ==2 : continue
    else: print(i)
    
# range 함수
a = range(10) # 10미만의 숫자를 포함하는 range 객체를 만든다.
#시작숫자와 끝 숫자를 지정할 수 있는데, 이때 끝 숫자는 포함되지 않는다.
b = range(10,20)

#for과 range를 이용한 구구단
for a in range(2,10):
    for b in range(1,10):
        print('%d * %d = %d' %(a,b,(a*b)), end= " ")
    print('')
    
