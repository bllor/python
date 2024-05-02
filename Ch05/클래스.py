'''
과자틀을 클래스, 과자 틀로 찍어낸 과자를 객체라고 한다고 가정하자.
클래스로 만든 객체는 객체마다 고유한 성격을 가지고 있고, 서로 전혀 영향을 주지 않는다.
과자에 구멍이 있거나, 많이 탔거나, 적게 탔거나 등 고유한 성격을 가지고 있고,
한 입 베어 먹었다 한들 다른 과자들에 영향을 주지 않는다는 의미이다.

객체와 인스턴스
클래스로 만든 객체를 인스턴스라고도 한다.
a= Cookie()로 만든 a는 객체이다.
a객체는 Cookie의 인스턴스이다.
즉 인스턴스라는 말은 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용한다.
'''
#1 사칙연산 클래스 만들기
#클래스 내에서 사용되는 함수를 매서드라고 한다.
#파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.
#self를 사용하는 이유는 객체를 호출할 때 호출한 객체 자신이 전달되기 때문이다.
class fourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first+self.second
        return result        
        
a = fourCal()
a.setdata(4,2)
print(a.first)
print(a.second)
b = fourCal()
b.setdata(7,5)
#다음과 같이 b를 이용하여 first, second의 값을 넣어도 a객체의 값은 변하지 않는다
#즉 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.

print(a.add())

#생성자
#객체가 생성될 때 자동으로 호출되는 메서드
#__init__를 사용하면 이 메서드는 생성자가 된다.

class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def setData(self,a,b):
        self.a = a
        self.b = b
    
    def mul(self):
        result = self.a*self.b
        return result
    
#위의 코드와 같이 생성자를 추가하게 되면 객체를 만들 때 생성자의 매개변수를 추가해주어야 한다.

#클래스의 상속
#어떤 클래스에서 다른 클래스의 기능을 물려받아서 사용할 때 상속을 사용한다.
#상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경할 때 주로 사용하는데
#기존 클래스를 변경하면 되지 않나? 라는 생각을 할 수 있지만
#기존 클래스가 라이브러리로 사용되거나 수정이 허용되지 않는 상황일 때 상속 받아서 사용한다.
#class 클래스명(상속받을 클래스명)의 형태로 상속받아서 사용할 수 있다.

class moreCal(cal):
    def doubleadd(self):
        result = (self.a+self.b)*2
        return result
    
c = moreCal(4,2) # cal의 생성자도 상속받아서 사용하게 된다.
print(c.doubleadd())
print(c.mul())

'''
3.메서드 오버라이딩
부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩이라고 한다.

4.클래스 변수
객체변수와 달리 클래스로 만든 모든 객체에서 쓰인다.
'''

        