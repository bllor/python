'''
파이썬은 동적 프로그래밍 언어로 변수의 타입을 변경할 수 있다
동적 프로그래밍 언어는 유연한 코딩이 가능하여 쉽고 빠르게 프로그램을 만들 수 잇지만,
프로젝트의 규모가 커질수록 타입을 잘못 사용해 버그가 생길 확률이 높아진다.
num: int = 1 or ->:int 를 통해 리턴타입의 타입도 정할 수 있다.
타입 어노테이션으로 매개변수의 타입을 명시하더라도 변경될 수 있는데,
이 때 mypy라이브러리를 사용하면 타입 변경을 막을 수 있다.
'''