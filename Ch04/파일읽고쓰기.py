'''
1.파일 생성하기
파일_객체 = open(파일경로_파일명,파일열기모드)
파일열기모드
[1] r : 읽기모드 - 파일을 읽을 때만 사용한다. 
[2] w : 쓰기모드 - 파일에 내용을 쓸 때 사용한다.
[3] a : 추가모드 - 파일의 마지막에 새로운 내용을 추가할 때 사용한다.

'''
# #1. 파일에 내용쓰기
# f =open('/Users/bia/Desktop/새파일.txt','w')
# for i in range(0,11):
#     data = '%d번째 줄입니다\n' %i
#     f.write(data)
# f.close()

#2.파일 내용 읽기
#[1]readline
#readline을 사용할 경우 해당 파일의 첫번째 줄을 출력하는데,
#모든 내용을 출력하려면 while문을 사용하면 된다.
# f = open('/Users/bia/Desktop/새파일.txt','r')
# line= f.readline()
# print(line)
# # f.close()

# while True:
#     line = f.readline()
#     if not line: break
#     print(line)

# f.close()

#2.readlines함수 사용하기
#readlines함수는 파일의 모든 줄을 읽어서 각각의 중을 요소로 가지는 리스트를 리턴합니다.
#파일문장 끝에 줄바꿈 문자가 있을 경우 제거하는 것이 좋다.
f2 = open('/Users/bia/Desktop/새파일.txt','r')
line2= f2.readlines()
for line in line2:
    print(line)
f2.close()
    
#read함수
#read함수는 파일의 내용 전체를 문자열로 리턴한다.

#with open(파일명,읽는방식) as f:
# f.write()
#처럼 with과 함께 사용한다면 close를 하지 않아도 자동으로 닫아준다.