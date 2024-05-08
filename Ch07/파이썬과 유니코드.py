'''
1.아스키 코드
영문자를 숫자로 대체한 최초의 코드

2.유니코드
모든 나라의 문자를 숫자로 만든 코드

3.유니코드로 문자열 다루기
[1]인코딩하기
a= '한글'
a.encode('utf-8')을 할 경우 유니코드를 이용하여 한글을 인코딩한 것이 된다.
[2]디코딩하기
decode('utf-8')

4.euc-kr로 된 파일 읽기
with open('file_name', encoding = 'euc-kr')as f:
    data = f.read()
    
'''
