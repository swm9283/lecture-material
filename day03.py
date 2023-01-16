# 반복문 : while과 for문
gugudane =int(input("원하는 수의 구구단을 입력하세요, 예)3 :"))
count = 1
# while count<=9:
#     print(f"{gugudane} * {count} = {gugudane*count}")
#     count=count+1

while count<=9:
    print("{0} * {1} = {2}".format(gugudane,count,gugudane*count))
    count=count+1

while True:
    gugudane = int(input("원하는 수의 구구단을 입력하세요, 예)3 :"))
    count = 1
    # if gugudane>0 and gugudane<10: old style
    if 1 <= gugudane < 10:
        while count <= 9:
            print("{0} * {1} = {2}".format(gugudane, count, gugudane * count))
            count = count + 1
        break

    else:
        print("1에서 9사이의 값을 입력하세요!")





















































































