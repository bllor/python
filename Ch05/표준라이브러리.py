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
    
