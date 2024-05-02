'''
함수가 하는 일 : 어떤 입력 값을 가지고 일을 수행한 후 그 결과물을 내어 놓는 것
함수르 사용하는 이유는 반복적으로 사용되는 부분을 줄이고, 프로그램의 흐름을 일목요연하게 볼 수 있게 만드려고.
함수의 구조
def 함수명(매개변수):
    수행할 문장

매개변수와 인수
매개변수는 함수에 입력으로 전달된 값을 받는 변수
인수는 함수를 호출할 때 전달하는 입력값

def add(a,b)
    return a+b

print(add(3,4))
여기서 a,b는 매개변수
3,4는 인수가 된다.
사실 매개변수,인수, 파라미터 등 모두 같은 말이다.

입력값이 없는 함수, 출력값이 없는 함수가 존재할 수 있다.
출력값이 없는 함수일 경우 출력할 경우 none이 출력되는데, 함수만 사용하면 함수 내 print문을 사용할 수 있다.    
'''

def add(a,b):
    print('%d + %d = %d' %(a,b,(a+b)))

a = add(3,4)
print(a)
add(5,6)

#여러 개의 입력 값 받기
#함수에 사용될 입력값이 몇 개인지 모를 경우
# def 함수명(*args)를 하면된다.
# 여기서 *args는 임의로 정한 변수이름으로 다른 것들을 사용해도 된다.
def add_many(*args):
    sum = 0
    for i in args:
        sum+=i
    
    return sum    
a = add_many(1,2,3)
b = add_many(1,2,3,4,5,6,7,8,9,10)
print(a,b)

'''
키워드 매개변수
매개변수 앞에 **를 붙이면 매개변수는 딕셔너리가 되고 key=value 형태의 입력값이 그 딕셔너리에 저장이 된다.
'''
def print_kwargs(**kwargs):
    print(kwargs)
    
print_kwargs(a=1)

print_kwargs(name='dongil',region='seoul')

'''
함수의 리턴값은 언제나 1개!
def add_and_mul(a,b):
    return a+b, (a*b)
print(add_and_mul(3,4))를 할 경우
(a+b,(a*b))를 한 쌍으로 묶어서 7,12를 출력한다.
두 개의 결과를 각각 변수에 저장하고 싶으면
result1, result2 = add_and_mul(3,4)처럼 2개를 작성하면
result1에는 7이, result2에는 12가 저장된다.    
'''

'''
매개변수에 초기값 미리 설정하기
def say_myself(name,age,man=True):
    print('내 이름은 %s입니다',%name)
    print('내 나이는 %d입니다',%age)
    if(man):
        print('남자입니다.')
    else:    
        print('남자입니다.')
        
초기값이 없는 매개변수는 초기값이 있는 매개변수 뒤에 사용할 수 없으므로
초기값이 있는 매개변수를 가장 뒤에 배치해야한다.

함수 안에서 함수 밖의 변수를 변경하는 방법
1.return
def add(a):
    return a=a+1
a=3
a=add(a)
        
2.global
def add():
    global a
    a=a+1
a=2
add()
print(a)    
함수는 독립적으로 존재하는 것이 좋으므로 global 명령어는 사용하지 않는 것이 좋다.

lambda예약어
lambda는 함수를 생성할 때 사용하는 예약어로, def와 동일한 역할을 한다.
def를 사용해야할 정도로 복잡하지 않거나 def를 사용할 수 없는 곳에 주로 쓰인다.
add = lambda a,b: a+b
print(add(3,4)) --> 7
'''    
def add():
    global a
    a=a+1
a=2
add()
print(a)    
