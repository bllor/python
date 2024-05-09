'''
1.클로저
함수 안에 내부 함수를 구현하고 그 내부 함수를 리턴하는 함수

2.데코레이터
기존 함수를 바꾸지 않고 기능을 추가할 수 있게 만드는 함수
@함수명 과 같은 형태로 있으면 데코레이터 함수로 인식한다.
'''

#ex
'''
어떤 수에 항상 3을 곱해 리턴하는 함수가 있다.
만약 항상 5를 곱해 리턴하는 함수를 만들어야 한다면 
3을 곱하는 함수, 5를 곱하는 함수로 2개가 되고, 필요 시 마다 다른 숫자들을 늘려줘야해서 비효율적이다.
클래스를 이용하여 관리하는 방법이 있다.
'''
#1.클래스 이용
## mul부분을 __call__로 변경해야 사용 가능
class Mul:
    def __init__(self, m):
        self.m = m
        
    def mul(self,n):
        return self.m * n
print(__name__)    
if __name__ == "__main__":
    mul3 = Mul(3)        
    mul5 = Mul(5)

    print(mul3.mul(10))            
    print(mul5.mul(10))            
    
'''
class Mul:
    def __init__(self, m):
        self.m = m
        
    def __call__(self,n):
        return self.m * n
다음과 같이 사용하면 클래스를 만든 후 숫자를 넣어주면 바로 출력가능
위에서처럼 mul3.mul을 하지 않아도 된다.        
'''
#클로저의 예    
def mul(n):
    def wrapper(m):
        return m*n
    return wrapper
mul3 = mul(3)
print(mul3(10))
#다음과 같이 함수가 함수를 리턴한다

#데코레이터 예시
import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func()
        end = time.time()
        print("함수 수행 시간 : %f초"%(end-start))
        return result
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

myfunc()
# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()
#elapsed함수로 클로저를 만들었다.
#다음과 같이 사용하지 않고 @elapsed를 하여 클로저를 붙이게 사용할 수 있다.
#데코레이터함수에게 기존 함수의 입력 인수를 전달할 때는 *args, **kwargs를 사용한다.
# *args는 모든 입력 인수를 튜플로 변환하고, **kwargs는 모든 키=값 형태의 입력 인수를 딕셔너리로 변환한다ㅏ.

def elapsed2(original_func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = original_func(*args,**kwargs)
        end = time.time()
        print("함수 수행 시간 %f"%(end-start))
        return result
    return wrapper

@elapsed2
def myfunc2(msg):
    print(msg)
    
myfunc2("가즈아")    