# set
# set의 특성 : 1. 순서 X 2.mutable 3.중복 X 4.set은 index와 키가 없다.

#making the set
empty_set = set()
# print(empty_set)
even_number = {0,2,4,6,8}
odd_number = {1,3,5,7,9}
print(even_number,odd_number)
print(type(even_number),type(odd_number))

letter_list = list("letters")
letter_list_to_set = set(letter_list)

letter_dict= {"letters": "letters"}
letter_dict_to_set = set(letter_dict)
print(letter_dict, letter_dict_to_set)

letter_tuple = "l","e","t","t","e","r"
letter_tuple_to_set = set(letter_tuple) #셋은 중복된 값을 삭제하여 셋을 생성
print(letter_tuple,letter_tuple_to_set)

#set mutable
s = set()
for i in range(4):
    s.add(i)
print(s)

for i in range(4):
    s.remove(i)
print(s)

#in
drinks = {"martini": {"vodka","vermouth"},
          "black russian": {"vodka","kahlua"},
          "white russian": {"cream","vodka","kahlua"},
          "manhattan": {"rye","vermouth","bitters"},
          "screwdriver": {"orange juice","vodka"}}
for name, contents in drinks.items(): #unpacking
    if "vodka" in contents:
        print(name)

for name, contents in drinks.items():
    if "vodka" in contents and not ("cream" in contents or "vermouth" in contents):
        print(name)

#콤비네이션 연산자.
for name, contents in drinks.items(): #unpacking
    if "vodka" in contents and contents & {"vermouth","orange juice"}:
        print(name)

bruss = drinks["black russian"]
wruss = drinks["white russian"]

a={1,2}
b={2,3}

#교집합
print(a & b)
print(a.intersection(b))

#합집합
print(a | b)
print(a.union(b))

#차집합
print(a-b)
print(a.difference(b))

#대칭 차집합
print(a^b)
print(a.symmetric_difference(b))

print(bruss ^ wruss)

#부분집합
print(a<=b)
print(a.issubset(b))
print(bruss<=wruss)

#진부분집합
print(a<b)
print(bruss<wruss)
#상위집합
print(a>=b)
print(a.issuperset(b))
#진상위집합
print(a>b)



# 셋 컴프리헨션
a_set = {number for number in range(1,6) if number % 3 ==1}
print(a_set)

a_dick = {number: number for number in range(1,6) if number % 3 ==1}
print(a_dick)

#불변 셋 생성하기
a = frozenset([3,2,1])
print(a)


# 자료구조 결합하기 + 정리