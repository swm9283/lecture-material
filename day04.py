# dictionary
# students = {"name": "kim inha", "age": 23, "eyes": [0.9,1.1]}
#
# # for k in students.keys()
# # for k in students:
# #     print(k)
# # for k in students.values():
# for k, v in students.items():
#     print(f"{k} : {v}")
# # print(f"이름은 {students[["name"]]}")
# print(f"이름은 {students['name']}, 나이는 {students['age']}", end = " ")
# print(f"시력은 좌: {students['eyes'][0]} 우 : {students['eyes'][1]}")

#술 안주 추천 시스템
import random

alcohol_foods = {"맥주": "치킨","소주": "골뱅이 소면","와인":"치즈","위스키": "소금과 레몬"}
alcohol_list = list(alcohol_foods) # extract keys
# food_list = list(alcohol_foods.values()) #extract values
food_list = [food for food in alcohol_foods.values()] # extract values and append list
while True:
    alcohol = input(f"술을 선택하세요 1) {alcohol_list[0]} 2) {alcohol_list[1]} 3) {alcohol_list[2]} 4) {alcohol_list[3]} 5) 아무거나 6) 계산 :")
    if alcohol == "6":
        print("다음에 또 뵙겠습니다.")
        break
    elif alcohol == "1":
        print(f"{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다.")
    elif alcohol == "2":
        print(f"{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다.")
    elif alcohol == "3":
        print(f"{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다.")
        pass
    elif alcohol == "4":
        print(f"{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다.")
    elif alcohol == "5":
        ran_alcohol = random.choice(alcohol_list)
        ran_food = random.choice(food_list)
        print(f"랜덤으로 추천하는 술은 {ran_alcohol}이고 안주는 {ran_food}입니다.")
    else:
        print("메뉴에서 골라 주세요.")



