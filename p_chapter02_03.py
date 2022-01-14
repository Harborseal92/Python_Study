class Car():
    """
    Car class
    Author : Leejh
    Date : 2021.11.05
    Description : class, Static, Instance Method
    """
    #클래스 변수(모든 인스턴스가 공유한다)
    price_per_raise = 1.2
    car_count=0

    def __init__(self,company,details):
        self._company = company
        self._details = details
        # Car.car_count+=1
        

    def __str__(self): #사용자 입장에서 출력할때 사용 ,str 메소드랑 repr 둘다없으면 그냥 클래스정보만표기해줌
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): #개발자 입장에서 객체를 그대로 표현해줄때 사용
        return 'repr : {} - {}'.format(self._company, self._details)

    #Instance Method
    #Self : 객체의 고유한 속성 값을 사용
    def detail_info(self):
        print('Current ID : {} '.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    
    #Instance Method
    def get_price(self):
        return 'Before Car Price -> campany : {} , price : {}'.format(self._company, self._details.get('price'))

    def get_price_calc(self):
        return 'After Car Price -> campany : {} , price : {}'.format(self._company, self._details.get('price')*Car.price_per_raise)

    #classmethod
    @classmethod
    def raise_price(cls,per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print("Succed! price increased.")

    #staticmethod
    @staticmethod
    def is_bmw(kkk):
        if kkk._company =="bmw":
            return 'Ok! This car is {}'.format(kkk._company)
        return 'Sorry. This car is not Bmw'

#Self 의미
car1 = Car('Ferrari' , {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('bmw' , {'color' : 'black' , 'horsepower' : 270, 'price' : 5000})

#전체정보
car1.detail_info()

#가격정보(직접 점근)
print(car1._details.get('price'))
print(car2._details['price'])

#가격정보(인상전)
print(car1.get_price())
print(car2.get_price())

#가격 인상(클래스 메소드 미사용)
Car.price_per_raise = 1.4

#Class메소드 사용
Car.raise_price(1.6)

# 가격정보(인상후)
print(car1.get_price_calc())
print(car2.get_price_calc())

#인스턴스로 호출(스테이틱)
print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

#클래스로 호출(스테이틱)
print(Car.is_bmw(car1))
