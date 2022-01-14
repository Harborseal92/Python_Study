# Chapter04-03
# 시퀀스형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str,bytes,bytearray,array.array,memoryview])
# 가변(list,bytearray, arra.array, memoryview, deque)
# 불변(tuple, tuple, bytes)
# 해시 테이블
# Key 에 Value 를 저장하는 구조 
# 파이썬 dict 는 해쉬 테이블의 예
# 키 값의 연산 결과에 때라 직접 접근이 가능한 구조
# key 값을 해싱 함수를 -> 해쉬 주소 -> key 에 대한 value 참조

# Dict 구조
# print(__builtins__.__dict__)
print()
# Hash 값 확인

t1 = (10,20, (30,40,50))
t2 = (10,20,[30,40,50])
print(hash(t1))
# print(hash(t2)) 예외, 불변형만 해쉬가능

print()
print()

source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault

for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] =[v]
print(new_dict1)
print()

# Use Setdefault

for k,v in source:
    new_dict2.setdefault(k,[]).append(v)
print(new_dict2)