while True:
    gugudane = int(input("원하는 수의 구구단을 입력하세요,0을 입력시 프로그램이 종료됩니다., 예)3 :"))
    count = 1
    if gugudane == 0:
        print("프로그램이 종료되었습니다")
        break
    # if gugudane>0 and gugudane<10: old style
    if 1 <= gugudane < 10:
        while count <= 9:
            print("{0} * {1} = {2}".format(gugudane, count, gugudane * count))
            count = count + 1


    else:
        print("1에서 9사이의 값을 입력하세요!")


numbers = [1,3,5]
position = 0
while position <len(numbers):
    number =numbers[position]
    if number % 2 ==0:
        print("found even number",number)
        break
    position = position +1
else:
    print("No even number found")


#for문 사용
while True:
    gugudane = int(input("원하는 수의 구구단을 입력하세요,0을 입력시 프로그램이 종료됩니다., 예)3 :"))
    if gugudane == 0:
        print("프로그램이 종료되었습니다")
        break
    # if gugudane>0 and gugudane<10: old style
    if 1 <= gugudane < 10:
        for i in range(1,10,2): # 건너뛰기 사용가능
            print("{0} * {1} = {2}".format(gugudane,i, gugudane * i))
    else:
        print("1에서 9사이의 값을 입력하세요!")





























































