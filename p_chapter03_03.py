# Chapter03-03
# Special Method (Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Fuctions), Class(클래스)
# 클래스안에 정의할 수 있는 특별한(Built in) 메소드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type 으로 확인이 가능 -> value 형태로 표현

# 일반적인 튜플
pt1 = (1.0 , 5.0)
pt2 = (2.5 , 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0]-pt2[0]) **2 + (pt1[1] - pt2[1])**2)
print(l_leng1)

# 네임드 튜플 사용

from collections import namedtuple

# 네임드 튜플 선언
Point = namedtuple('Point', 'x y')
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)
print(pt3)
print(pt4)

#네임드 튜플 사용 방법
Point1 = namedtuple('Point', ['x', 'y'])
Point2 = namedtuple('Point', 'x,y')
Point3 = namedtuple('Point', 'x y')
Point4 = namedtuple('Point', 'x y x class', rename=True) # Default=False

print(Point4)

# Dict to Unpacking
temp_dict= {'x':75, 'y':55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10,20,30,40)
p5 = Point3(**temp_dict) #튜플은 1개가 붙고 딕셔너리는 2개가 붙음

print()
print(p1)
print(p2)
print(p3)
print(p4)

# 네임드 튜플 메소드로 변환하는법 (리스트 -> 튜플)
# _make() : 새로운 객체 생성
temp = [52,38]
p4 = Point1._make(temp)
print(p4)

# _fields : 필드 네임 확인
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrdereDict 반환
print(p1._asdict())

# 실 사용 실습
# 반 20명, 4개의 반 (A,B,C,D)

Classes = namedtuple('Classes', ['rank', 'number'])

#그룹 리스트 선언
numbers = [ str(n) for n in range(1,21)]
ranks= 'A B C D'.split()

# List Comprehension
students = [Classes(rank,number) for rank in ranks for number in numbers]
print(len(students))
print(students)

#추천
students2 = [Classes(rank,number)
            for rank in 'A B C D'.split()
                for number in [str(n)
                    for n in range(1,21)]]

print(students2)

# 출력

for s in students2:
    print(s)