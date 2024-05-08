'''
1.pip
pip: 파이썬 모듈이나 패키지를 쉽게 설치할 수 있도록 도와주는 도구
pip로 파이썬 프로그램을 설치하면 의존성 있는 모듈이나 패키지를 함께 설치해주기 때문에 매우 편리하다.
[1]설치
pip install library_name
[2]삭제
pip uninstall library_name
[3]특정버전으로 설치
pip install SomePackage==version
[4]최신버전으로 업그레이드하기
pip install --upgrade SomePackage
[5]설치된 패키지 확인하기
pip list

2.faker
테스트용 가짜 데이터를 생성할 때 사용하는 라이브러리
pip install faker
from faker import faker
fake = Faker()
fake.name --> 무작위로 생성한 이름을 리턴한다.
fake = Faker('ko-KR')을 할 경우 한글로 리턴한다.
fake.ipv4_private() 임의의 ip주소를 만들어낸다.

3.sympy
방정식 기호를 사용하게 해주는 라이브러리
'''