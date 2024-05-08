'''
많이 사용되는 표준 라이브러리
1.datetime
-날짜를 표현할 때 많이 쓰인다.

2.time
시간과 관련된 라이브러리
-time.acstime :현재 날짜와 시간을 알아보기 쉽게 나타낸다.
-time.ctime :현재 날짜와 시간을 알아보기 쉽게 나타낸다. --> 항상 현재 시간만 리턴한다.

3.math
-math.gcd : 최대 공약수 구하기
-math.lcm : 최소 공배수 구하기

4.itertools.zip_longest
같은 개수의 자료형을 묶는데 자료의 개수가 다르다면 긴 객체의 개수에 맞춰 fillvalue에 설정한 값을 넣는다.

5.itertools.permutation
itertools.permutation(iterable, r)은 반복 가능한 객체 중에서 r개를 선택한 순열을 리턴한다.

6.itertools.combination(iterable, r)
반복 가능 객체 중에서 r개를 선택한 조합을 이터레이터로 리턴하는 함수

7.functools.reduce(function,iterable)
함수를 반복 가능한 객체의 요소에 차례대로 누적 적용하여 하나의 값으로 줄이는 함수

8.operator.itemgetter
key 매개변수를 적용하여 다양한 기준으로 정렬할 수 있게 도와준다.
itemgetter(1)은 해당리스트의 첫번째 키값을 기준으로 정렬한다는 뜻이다.
리스트가 아닌 클래스 객체라면 attrgetter를 사용한다.

9.shutil
파일을 이동하거나 복사할 때 사용하는 모듈
작업 중인 파일을 자동으로 백업하는 기능을 구현하고자 할 때는
import shutil
shutil.copy(exist_file,new_file)
파일을 이동하고자 할 때는
shutil.move(exist_file,new_file)

10.glob
디렉터리에 있는 파일들의 이름을 리스트 형식으로 출력한다.

11.pickle
객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈

12.os
[1]os.envirnon - 내 시스템의 환경변수값을 알고 싶을 때
[2]os.chdir - 현재 디렉터리의 위치를 변경할 수 있다.
[3]os.getcwd - 디렉터리 위치 돌려받기
[4]os.system - 시스템 명령어 호출하기
[5]os.popen - 실행한 시스템 명령어의 결괏값 돌려받기

13.zipfile
zipfile은 여러 개의 파일을 zip형식으로 합치거나 이를 해제할 때 사용
with zipfile.ZipFile(파일명)as myfile:
    myfile.write(파일1)
처럼 write()를 통해 파일을 합치고
extract(특정파일명)을 통해 특정파일만 압축해제하거나
extractall()을 통해 모든 파일을 해제할 수 있다.
*압축의 종류
[1]zip_stored: 압축하지 않고 파일을 zip으로만 묶는다. --> 속도가 빠르다.
[2]zip_deflated: 일반적인 zip압축으로 속도가 빠르고 압축률이 낮다
[3]zip_bzip2: bzip2압축으로 압축률이 높고 속도가 느리다.
[4]zip_lzma: lzma 압축으로 압축률이 높고 속도가 느리다.

14.traceback
프로그램 실행 중 발생한 오류를 추적하고자 할 때 사용하는 모듈
예외 부분에 
import traceback
print(traceback.format_exc())를 할 경우 오류추적결과를 문자열로 리턴한다.

15.json
[1]json_load(file) : json파일을 읽을 때
[2]json_dumps(file) : json파일을 생성할 때
-->한글 문자열이 아스키 형태의 문자열로 변경되는 것을 방지하는 방법
-->json.dump(file_name, ensure_ascii=False)
[3]json_loads(file) : json문자열을 한글이 깨지지 않고 출력하는 방법
'''

#ex
import itertools

num_list = [1,2,3,4,5]
# print(itertools.permutations(num_list,2))
# print(itertools.combinations(num_list,3))

it = itertools.combinations(num_list,3)
for a,b in itertools.permutations(num_list,2):
    print(a,b)
    
print('-----------------')
for i in it:
    print(i)    
    
