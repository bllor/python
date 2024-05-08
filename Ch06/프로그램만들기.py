'''
프로그램을 만드려면 가장 먼저 입력과 출력을 생각하라.

'''

#1.1000미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하기
result = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        result+=i
print(result)

#2.게시판 페이징하기
#한 페이지에서 보여주는 게시글이 10개이고, 총게시물이 65개일 때 총 페이지 수는?
import math
totalNo = 65
list = 10
totalPage=0
if (totalNo%list)==0:
    totalPage = totalNo//list
else:
    totalPage = totalNo//list+1
print(totalPage)