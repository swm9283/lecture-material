# function
#lambda

#function to use parameter
import random

# def squares(n):
#     """
#     제곱 함수
#     :param n: integer
#     :return:  integer
#     """
#     return n **2
#
# def process(no_lists,f):
#     for no in no_lists:
#         print(f(no))
#
#
# numbers = [random.randint(1,100) for i in range(5)]
# print(numbers)
# process(numbers,squares)

#function lambda
# 함수 이름이 들어가는 자리에 lambda 함수 이렇게 짧고 간결하게 작성할 수 있다.
def process(no_lists,f):
    for no in no_lists:
        print(f(no))


numbers = [random.randint(1,100) for i in range(5)]
print(numbers)
process(numbers, lambda x: x*x)
