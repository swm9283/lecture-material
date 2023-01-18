#function
def do_nothing():
    pass

# #None
#
# # print(do_nothing())
#
# mamamoo = ["화사","솔라","휘인","문별"]
# # print(mamamoo.pop()) #삭제할 값 리턴 후 삭제. 문별 pop
# print(mamamoo.remove("문별")) # 삭제만 함. 따라서 print 함수해서 출력할 값이 없다.
# print(mamamoo)

#매표소 요금 계산 for *
# *args 가변적인 인수를 받을 때 용이하다. 즉 던져진 인수의 값을 예측할 수 없을 때 용이하다. 튜플로 묶어서 처리한다.
# 튜플로 받기 때문에 가능하다.
def calculate_fee(*args):
    """
    놀이공원 요금 계산 프로그림
    :param args: ages
    :return: total fee for paying
    """
    total = 0
    for age in args:
        if age >= 19:
            total =  total + 10000
        else:
            total = total + 3000
    return total

print(calculate_fee(45,43,10,7))