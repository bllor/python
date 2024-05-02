'''
조건을 판단하여 해당 조건에 맞는 상황을 수행하는 데 쓰이는 것이 if문이다.
1. if문의 기본 구조
if 조건문:
    수행할 코드
else:
    수행할 코드
-- if문을 만들 때 if조건문: 다음 문장부터는 if문에 속하는 모든 문장에 들여쓰기를 해야한다.    
'''

#1. in, not in
print(1 in [1,2,3]) # 리스트에 1이 있으면 true, 없으면 false를 출력한다.
print(1 not in [1,2,3]) # 리스트에 1이 없는 경우 true를 출력한다.

#2. 조건문에서 아무 일도 하지 않게 설정하고 싶으면?
#--> pass를 사용하면 된다.
#주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라
pocket = ['paper','money','cellphone']
if 'money' in pocket:
    pass
else:
    print('카드를 꺼내라')
    

#3.조건부 표현식
score = 60
message = 'success' if score>60 else 'failure'
print(message)
     
#자바에서 else if처럼 파이썬에서는 elif를 사용한다.