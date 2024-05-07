'''
오류 예외 처리 기법
1.try - except문
기본 구조
try:
    code
except 발생오류 as 오류변수:
    print(오류변수)

2.try - finally문
finally절은 try문 수행 도중 예외 발생 여부에 상관 없이 항상 수행된다.
보통 finally절은 사용한 리소스를 close해야할 때 많이 사용한다.

3.여러 개의 오류문 처리하기
여러 개의 오류문을 처리하고 싶으면 except에 발생오류를 추가해주면된다.
ex)
try:
    code1..
except ZeroDivisionError:

except IndexError:

4.try else문
try문 수행 중 오류가 발생하면 except절, 오류가 발생하지 않으면 else절이 수행된다.

5.오류 회피하기
try:
    code1...
except 오류명:
    pass
pass를 사용할 경우 해당 오류가 발생해도 계속 진행이 된다.

6.오류 일부러 발생하기
raise 명령어를 사용하면 일부러 오류를 발생시킬 수 있다.

'''

#7. 예외 만들기
class MyError(Exception):
    pass


def say_nick(nick):
    if nick=='바보':
        raise MyError()
    
    print(nick)

try:
    say_nick('천재')
    say_nick('바보')
except MyError:
    print("그런 말은 나쁜 말이에요.")
'''
except MyError as e:
    print(e)
로 에러 메세지를 출력하고 싶으면
class MyError(Exception):
    def __str__(self):
        return '허용되지 않는 별명입니다.'
와 같이 사용하면 된다.
'''