# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# collections, text, List, Dict, Set, Tuple, unpacking, *args... : iterable

# 
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# print(dir(t))

for c in t:
    pass
    # print(c)

# while
w = iter(t)

while True:
    try:
        print(next(w))
    except StopIteration:
        break
print()

# 반복형 확인
print(hasattr(t, '__iter__')) # True 나오면 이터레이터임

from collections import abc
print(isinstance(t,abc.Iterable))

print()
print()

# next

class WordSplitter:
    def __init__(self,text):
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        print('called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration')
        self._idx +=1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do today what you could do tomorrow')
print(wi)
print(next(wi))
print(next(wi))

# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 증가 후 메모리 사용량 증가 -> 제네레이터 사용권장
# 2. 단위 실행 가능한 코루틴 구현과 연동
# 3. 작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self,text):
        self._text = text.split(' ')
    
    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
            return
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wg = WordSplitGenerator('Do today what you could do tomorrow')
wt = iter(wg)
print(wt,wg)