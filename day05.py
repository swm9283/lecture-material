# def calculate_fee(*args):
# v0.2
import random

# def calculate_fee(*args):

# def calculate_fee(args) -> list:
#     """
#     놀이공원 요금 계산 프로그램
#     :param args: ages
#     :return: 지불할 총 입장료
#     :param args: ages in list
#     :return: [전체 인원 수, 어른 수, 아이 수, 지불할 총 입장료]
#     """
#     total = 0
#     adults = 0
#     kids = 0
#     for age in args:
#         if 19 <= age:  # adult
#             total = total + 10000
#             adults = adults + 1
#         else:
#             total = total + 3000
#             kids = kids + 1
#     return [len(args), adults, kids, total]
#
#
# no_of_visitor = int(input('몇 분 이세요? '))
# ages = [random.randint(1, 60) for age in range(no_of_visitor)]
# results = calculate_fee(ages)
# print(f'{results[0]}명 방문 하셨고 어른 {results[1]}명, 아이 {results[2]}명 총 요금은 {results[-1]}원 입니다')


# 이 코드 딕셔너리로 바꾸어보자!!!
def calculate_fee(args) -> dict: #리턴을 리스트로 하겠다.
    """
    놀이공원 요금 계산 프로그램
    :param args: ages
    :return: 지불할 총 입장료
    :param args: ages in list
    :return: {"no_of_people": 총 인원
    """
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 19 <= age:  # adult
            total = total + 10000
            adults = adults + 1
        else:
            total = total + 3000
            kids = kids + 1
    return [len(args), adults, kids, total] #여기만 딕셔너리로 바꾸면된다.

no_of_visitor = int(input('몇 분 이세요? '))
ages = [random.randint(1, 60) for age in range(no_of_visitor)]
results = calculate_fee(ages)
print(f'{results[0]}명 방문 하셨고 어른 {results[1]}명, 아이 {results[2]}명 총 요금은 {results[-1]}원 입니다')

#독스트링
# print(calculate_fee.__doc__) #help(calculate_fee)
# help(calculate_fee)
# help(len)






