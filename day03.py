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