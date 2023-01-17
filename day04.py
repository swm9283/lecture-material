# list 03
# list comprehension and generator

#list comprehension
# [ 표현식 for 항목 in 순회 가능한 객체]
# 책에 나온 여러 코드 작성해서 해보자.

# 이 코드를 줄이고 싶다
odd_list = []
for i in range(1,11):
    if i % 2 ==1 :
        odd_list.append(i)
print(odd_list)

#리스트 컴프리헨션
odd_list_comprehension= [i for i in range(1,11) if i % 2 ==1]
print(odd_list_comprehension,type(odd_list_comprehension))

#튜플 컴프리헨션이 없을까?
# <generator object <genexpr> at 0x10488b510>
#  튜플 컴프리헨션은 존재하지 않는다.
odd_tupple =(i for i in range(1,11) if i % 2 ==1)
print(odd_tupple,type(odd_tupple))

#연습문제


