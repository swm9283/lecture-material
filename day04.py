# dictionary
alcohol_foods = {"맥주": "치킨","소주": "골뱅이 소면","와인":"치즈","위스키": "소금과 레몬"}
alcohol_list = list(alcohol_foods) # extract keys
# food_list = list(alcohol_foods.values()) #extract values
food_list = [food for food in alcohol_foods.values()] # extract values and append list
#enumerate
for food in enumerate(food_list):
    print(food[1])
# less 파이써닉 범위 지정시 사용
for food in range(len(food_list)):
    print(food)
# more 파이써닉
for food in food_list:
    print(food)



