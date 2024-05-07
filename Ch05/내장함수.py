'''
1.abs  - 절대값 리턴
2.all(x) - x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴한다.
3.any(x) - x의 요소 중 하나라도 참이면 True리턴
4.chr(i) - 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴
5.dir() - 객체가 지닌 변수나 함수를 보여주는 함수
6.divmod(a,b) - a를 b로 나눈 몫과 나머지를 튜플로 리턴한다.
7.enumerate - 데이터(리스트,튜플,문자열)를 입력으로 받아 인덱스 값을 포함한 enumerate 객체를 리턴한다.
8.eval - 문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결과값을 리턴하는 함수
9.filter(함수(),데이터) - 데이터의 요소 순서대로 함수를 호출했을 때 리턴값이 참인 것만 묶어서 리턴한다.
10.hex(x) - x를 16진수 문자열로 변환하여 리턴
11. id - 객체를 입력받아 고유 주솟값을 리턴
12.input([prompt]) - 사용자 입력을 받는 함수 *[]는 괄호 안의 내용을 생략할 수 있다는 관례 표기법
13.int - 문자열 형태의 숫자나 소수점이 있는 문자를 정수로 리턴
14.isinstance(object, class) - 입력 받은 객체(object)가 그 클래스의 인스턴스인지를 판단하여 참이면 true를 리턴
15.len(s) -s의 길이
16.list(str) - str을 리스트로 만드는 함수
17.map(함수,데이터) - 데이터의 각 요소를 함수를 적용한 결과를 리턴하는 함수 
18.max, min - 데이터 속 최대, 최소값 출력
19.oct - 정수를 8진수 문자열로 바꾸어 리턴
20.open - 파일을 읽을 때 사용하며, 
            w : 쓰기모드로 파일 열기,r : 읽기모드로 파일 열기,
            a :추가모드로 파일열기 ,b : 바이너리 모드로 파일열기
21.ocd - 문자의 유니코드 숫자 값을 리턴하는 함수
22.pow(x,y) - x를 y제곱한 결과값
23.range([start,]stop[,step])
- 인수가 하나일 경우 0˜해당인수까지
- 인수가 2개일 경우 첫번째 인수부터 두번째 인수 바로 앞 수까지
- 인수가 3개일 경우 첫번째 인수부터 두번째 인수 앞 숫자까지 세번째 인수 간격으로 시작
24.round(num[,num2]) - num을 num2까지 반올림
25.sort() - 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴

'''

#ex
print(eval('1+2'))

#함수만 사용시
def positive(li):
    result=[]
    for i in li:
        if i > 0 :
            result.append(i)
    return result

list2 = [1,2,3,0,-1,-2,-7,5,6]
print(positive(list2))
## filter 사용
def positive2(x):
    return x>0
print(list(filter(positive2,list2)))

## lamda사용
print(list(filter(lambda x:x>0,list2)))

##map 적용전
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
        
    return result
numberList = [1,2,3,4]
result = two_times(numberList)
print(result)

#map 적용 후 
def twotwo_times(number):
    return number*2

print(list(map(twotwo_times,numberList)))