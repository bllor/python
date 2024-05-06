'''
모듈 : 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일
모듈은 다른 파이썬 프로그램에서 불러와 사용할 수 있도록 만든 파이썬 파일이다.
import 파일명을 통해서 해당 클래스 파일을 불러올 수 있으며 그 파일 내의 함수를 사용할 수 있다.
아니면 자바스크립트에서처럼 from 모듈_이름 import 모듈함수 처럼 사용할 수 있다.
'''

import modi1
print(modi1.add(3,4))
#import하는 순간 modi1파일이 실행되어 결과값을 출력하는데
#함수만 사용하고 싶으면 해당 파일에 if__name__=="__main__" 코드를 추가하고
#결과값을 if문 안에 넣으면 된다.
#__name__변수란 파이썬 내부적으로 사용하는 특별한 변수 이름이다.
#직접 파일을 실행할 경우 __name__변수에 __main__값이 저장이 되어 if문이 참이 된다. 

import mod2
print(mod2.PI)

#다른 디렉터리에 있는 모듈 불러오는 방법
#sys.path.append 사용하기
#sys.path의 경로에 다른 디렉터리의 주소를 추가하여 사용할 수 있게 만든다.
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('/Users/bia/Desktop/workspace/python/Ch04/mod3.py'))))
from Ch04 import mod3

print(mod3.add(6,4))
