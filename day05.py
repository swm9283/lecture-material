# set
# set의 특성 : 1. 순서 X 2.mutable 3.중복 X
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
s = set((1,2,3))
print(s)
s.add(4)
print(s)

s.remove(1)
print(s)

#in

#콤피네이션 연산자

# 셋 컴프리헨션

# 자료구조 결합하기 + 정리