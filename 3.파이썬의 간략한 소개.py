# 24.1.25
# 파이썬 공식 문서 튜토리얼

#ex1
print(2+4)

#ex2
# 5**2를 하게 되면 제곱이 된다.
print(5**2)

#ex3
tax = 12.5 / 100
price = 100.50
totalPrice = tax*price
print(totalPrice)
print(round(totalPrice,2))#소수점2자리 까지 표시


#ex4
print('does\'t') # == does't
print('hello world \nwelcome python') #\n ==   줄바꿈

#ex5
print('C:\some\name')
#위의 print를 출력할 경우\n이 특수문자 취급이 되어 
# C:\some
# ame
# 와 같은 형식으로 출력이 된다
# 특수문자로 취급 받고 싶지 않으면 문자열 앞에 r을 붙혀주면 된다.

print(r'C:\some\name')

#긴 문장의 문자열 작성

print("""\
Usage: thingy [options]
        -h      display this usage message
        -H hostname hostname to connect to
""")





