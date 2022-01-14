#Chapter02-01
#객체 지향 프로그래밍(oop) -> 코드의 재사용, 코드 중복 방지
#규모가 큰 프로젝트(프로그램) -> 함수중심 -> 데이터 방대 -> 규모가 복잡해진다

#클래스 중심 -> 데이터 중심 -> 객체로 관리


#차량 1 
car_company_1 = 'Ferrari'
car_detail_1 = [
    {'color' : 'White'},
    {'horsepower' : 400},
    {'price' : 8000}
]

#차량 2
car_company_2 = 'Bmw'
car_detail_2 = [
    {'color' : 'black'},
    {'horsepower' : 270},
    {'price' : 5000}
]

#차량 3
car_company_3 = 'Audi'
car_detail_3 = [
    {'color' : 'Silver'},
    {'horsepower' : 300},
    {'price' : 6000}
]

#리스트 구조
car_company_list = ['Ferrai','Bmw','Audi']
car_detail_list= [
    {'color' : 'White', 'horsepower' : 400, 'price' : 8000},
    {'color' : 'black' , 'horsepower' : 270, 'price' : 5000},
    {'color' : 'Silver' ,'horsepower' : 300, 'price' : 6000}
]

# 천개 만개가 되면 인덱스 번호를 알아야한다.

del car_company_list[1]
del car_detail_list[1]
print()
print(car_detail_list)
print(car_company_list)
print()
print()
#---------------------------

#딕셔너리 구조
#코드반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dicts=[
    {'car_company' : 'Ferrai',  'car_detail': {'color' : 'White', 'horsepower' : 400, 'price' : 8000}},
    {'car_company' : 'Bmw',  'car_detail': {'color' : 'black' , 'horsepower' : 270, 'price' : 5000}},
    {'car_company' : 'Audi',  'car_detail': {'color' : 'Silver' ,'horsepower' : 300, 'price' : 6000}}
]

print(car_dicts)

print()
print()

#---------------------------------------------------------

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코스 반복 최소화, 메소드 활용

class Car():
    def __init__(self,company,details):
        self._company = company
        self._details = details

    def __str__(self): #사용자 입장에서 출력할때 사용 ,str 메소드랑 repr 둘다없으면 그냥 클래스정보만표기해줌
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self): #개발자 입장에서 객체를 그대로 표현해줄때 사용
        return 'repr : {} - {}'.format(self._company, self._details)

car1 = Car('Ferrari' , {'color' : 'White', 'horsepower' : 400, 'price' : 8000})
car2 = Car('bmw' , {'color' : 'black' , 'horsepower' : 270, 'price' : 5000})
car3 = Car('Audi' , {'color' : 'Silver' ,'horsepower' : 300, 'price' : 6000})

print(car1)
print()
print()
#print(dir(car1))

#리스트 선엄
car_list=[]

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

print()
print()

for x in car_list:
    print(repr(x))

print()
print()
