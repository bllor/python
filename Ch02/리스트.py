'''
파이썬에서 리스트는 대괄호([])로 감싸주고 각 요솟값은 쉼표로 구분하여 사용할 수 있습니다.
리스트는 비어있을 수도 있고, 숫자, 문자로만 구성될 수도 있으며, 숫자+문자로 구성될 수도 있다.
즉 리스트는 어떠한 자료형도 포함할 수 있습니다.
'''

#리스트 인덱싱과 슬라이싱
a=[1,2,3,4,5]
print(a[0]+a[2])
print(a[1:3])

#리스트 연산하기
#리스트 역시 더할 수 있고, 곱할 수 있다.
#곱하게 될 경우 해당 리스트를 n번 반복한다.
#리스트의 길이를 구하는 방법은 len(리스트)를 하면 된다.
b=[1,2,3]
c=[4,5,6]
print(b+c)
print(b*2)

#리스트의 수정과 삭제
#리스트 값 수정하기
#수정하고자하는 문자의 인덱스를 이용하여 수정할 수 있고, del 문자의 인덱스를 이용하여 문자를 삭제할 수 있다.
e = ["a","b","c","d"]
print(e)
e[1]="f"
print(e)
del e[1]
print(e)

#리스트 관련 함수
'''
1.리스트에 요소 추가하기(append())
--> 리스트의 맨마지막에 해당 요소를 추가한다.
2.리스트 정렬(sort())
3.리스트 뒤집기(reverse())
-->a=[1,3,2]일 때 a.reverse를 할경우 2,3,1로 출력된다.
3.인덱스 반환(index())
4.리스트에 요소삽입(insert(a,b))
리스트의 인덱스번호a에 b를 추가한다.
5.리스트 요소 제거(remove)
remove(x)는 리스트에서 첫 번째로 나오는 x를 제거한다.
6.리스트 요소 끄집어 내기(pop())
리스트의 맨 마지막 요소를 리턴하고 그 요소는 리스트에서 삭제한다.
7.리스트에 포함된 요소 x의 개수 세기(count(x))
8.리스트 확장
-->a.extend([1,2])를 할 경우 원래의 a리스트에 1,2 리스트를 더하게 된다.
-->a+=[1,2]와 같다.
'''