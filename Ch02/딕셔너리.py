'''
딕셔너리 : key와 value를 한 쌍으로 가지는 자료형
딕셔너리는 리스트나 튜플처럼 순차적으로 해당 요솟값을 구하지 않고 key를 통해 value를 얻는다.
value에는 어떠한 자료형도 들어올 수 있다.
'''

#딕셔너리[key]를 할경우 해당 key의 value 값이 출력된다.
a={1:'hi'}
print(a[1])

'''
딕셔너리 관련 함수
1.딕셔너리 쌍 추가하기
a={1:'hi'}
a[2]='b'를 할 경우
a={1:'hi',2:'b'}로 추가가 된다.
2.딕셔너리 요소 삭제하기
del a[1]
딕셔너리 a의 키값이 1인 key:value를 제거한다.
'''

'''
딕셔너리를 만들 때 유의할 점
key가 중복될 경우 하나를 제외한 나머지 것들이 모두 무시된다.
key에 리스트를 사용할 수 없다.
'''

'''
딕셔너리 관련 함수
1.keys()
해당 딕셔너리의 모든 key값을 출력한다.
2.values()
해당 딕셔너리의 모든 value값을 출력한다.
3.items()
key와 value의 쌍을 튜플로 묶은 값을 객체로 리턴한다.
4.clear()
리스트의 모든 key와 value를 삭제한다.
5.get()
a.get(key)를 할 경우 해당 value를 리턴한다.
a[key]와 다른 점은 a[key]를 사용했을 때 해당 key가 없을 경우 오류를 발생하지만
a.get(key)는 none를 리턴한다.
아니면 a.get(key,'zzzzz')로 할경우 key가 없을 경우 'zzzz'를 출력하게 만들 수 있다.
6.in
해당 key가 딕셔너리 안에 있는지 확인하는 방법으로 있을 경우 true, 없을 경우 false를 리턴한다.
'''
a={"name":'dongil',"age":29,"region":"seoul"}
print(a.keys())
for i in a.keys():
    print(i)
    
b={"name":"홍길동","birth":'1128','age':30}
    