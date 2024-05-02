'''
문장을 반복해서 수행해야 할 경우 while문을 사용한다.
그래서 while문을 반복문이라고 한다.
while의 조건이 거짓이 될 때까지 반복한다.
'''

#10번찍어서 안넘어가는 나무 없다.

a=1

while(a<11):
    print('나무를'+str(a)+'번 찍었습니다.')
    
    if a== 10:
        print('나무가 넘어갑니다.')
    a+=1
        
        
#여러 가지 선택지 중 하나를 선택해서 입력 받는 예제
prompt = '''
1.add
2.del
3.list
4.quit

Enter number: '''

# number= 0
# while number!=4:
#     print(prompt)
#     number= int(input())

#while문의 맨 처음으로 돌아가기
#: continue를 할 경우 해당 코드 아래의 내용들은 사용되지 않고
#while문의 제일 처음으로 올라가게 된다.
a = 0
while a<10:
    a=a+1
    if a%2 ==0: continue
    print(a)