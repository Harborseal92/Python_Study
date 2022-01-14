# Chapter04-01
# 시퀀스형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str,bytes,bytearray,array.array,memoryview])
# 가변(list,bytearray, arra.array, memoryview, deque)
# 불변(tuple, tuple, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending Llsts)
chars = '+_)(*&^%$#@!)'
code_list1=[]

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))
print(code_list1)

# Comprehending Lists
code_list2 = [ord(s) for s in chars]
print(code_list2)

#Comprehending list + Map + Filter
code_list3 = [ord(s) for s in chars if ord(s) >40 ]
code_list4 = list(filter(lambda x : x > 40, map(ord,chars)))
print(code_list3)

#Generator 생성
import array

#Generator : 한 번에 한 개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in chars))


print(type(tuple_g))
print(next(tuple_g))
print(next(tuple_g))
print(tuple_g)

# 제너레이터 예제
print(('%s' % c + str(n) for c in ['A','B','C','D'] for n in range(1,21) ))

# 리스트 주의
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~'] * 3 ] * 4

print()
# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1)
print(marks2)

# 증명
print([id(i) for i in marks1])
print([id(i) for i in marks2])
