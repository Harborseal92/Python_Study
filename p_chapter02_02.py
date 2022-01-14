#Chapter02-02
class Car():
    """
    Car class
    Author : Leejh
    Date : 2021.11.05
    """
    #클래스 변수(모든 인스턴스가 공유한다)
    car_count = 0


    def __init__(self,company,details):
        self._company = company
        self._details = details
        Car.car_count+=1
        

    def __str__(self): #사용자 입장에서 출력할때 사용 ,str 메소드랑 repr 둘다없으면 그냥 클래스정보만표기해줌
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): #개발자 입장에서 객체를 그대로 표현해줄때 사용
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current ID : {} '.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    
    def __del__(self):
        Car.car_count-=1


#Self 의미
car1 = Car('Ferrari' , {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('bmw' , {'color' : 'black' , 'horsepower' : 270, 'price' : 5000})
car3 = Car('Audi' , {'color' : 'Silver' ,'horsepower' : 300, 'price' : 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company) 
print(car1 is car2) #id 기준으로 비교 -> 같은지?

#dir & __dict__

print()
print()

print(car1.__dict__)
print(car2.__dict__)

# Doctring

print(Car.__doc__)

print()
print()

#인스턴스 생성하기
car1.detail_info()

print()
print()

#비교 . 부모는같다

print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__),id(car3.__class__))

#에러
#Car.detail_info() --> 클래스로 접근했을때는 반드시 인자를 넘겨야함(self)
Car.detail_info(car1)

#공유 확인
print(car1.__dict__)
print(car2.__dict__)
print(car1.car_count)
print(car2.car_count)
print(dir(car1))

#접근
print(car1.car_count)
print(Car.car_count)

#삭제 확인
del car2
print(car1.car_count)
print(car2.car_count)

#인스턴스 네임스페이스에 없으며 상위에서 검색
#즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색후 -> 상위(클래스 변수, 부모클래스 변수)
