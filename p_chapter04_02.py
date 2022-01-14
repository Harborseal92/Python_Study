# Chapter04-02
# 시퀀스형
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque])
# 플랫(Flat : 한개의 자료형[str,bytes,bytearray,array.array,memoryview])
# 가변(list,bytearray, arra.array, memoryview, deque)
# 불변(tuple, tuple, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

print(divmod(100,9)) # divmod -> 몫과 나머지 반환
print(divmod(*(100,9)))
print(*(divmod(100,9)))

print()

x, y, *rest = range(10)
print(x, y, rest)
x, y, *rest = range(2)
print(x,y,rest)
x, y, *rest = 1,2,3,4,5
print(x,y,rest)

print()
print()

# Mutable(가변) vs Immutable(불변)
l = (15,20,25)
m = [15,20,25]

print(l,id(l))
print(m, id(m))

l = l * 2
m = m * 2
print(l, id(l))
print(m, id(m))

l *= 2
m *= 2
print(l, id(l))
print(m, id(m))
# 변경이 자주일어나는것은 리스트가 유리하다. 튜플에 넣으면 계속 id값이 재할당되서 별로다

# sort vs sorted
# reverse, key=Len, key=str.Lower, key=func...

# sorted : 정렬 후 새로운 객체 반환

f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawerry', 'coconut']
print('sorted -' ,  sorted(f_list))
print('sorted - ' , sorted(f_list, reverse=True))
print('sorted - ' , sorted(f_list,key=len)) #알파벳의 길이순으로 정렬
print('sorted - ' , sorted(f_list, key = lambda x: x[-1]))
print('sorted - ' , sorted(f_list, key=lambda x: x[-1], reverse=True))
print(f_list) # 안바뀐다
print()
# sort : 정렬후 객체 직접 변경

# 반환 값 확인(None)
print('sort - ', f_list.sort(),f_list)

# List vs Array 적합 한 사용법 설명
# 리스트 기반 : 융통성 -> 왜? 다양한 자료형, 범용적 사용 , 속도
# 숫자 기반 : array 가 유리! 정말 많은 데이터를 묶어서 고속의 연산을 해야할때
# 숫자 기반 : 배열(리스트와 거의 호환)

