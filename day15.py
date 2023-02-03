#다항식의 선형 리스트 표현.

## 함수 선언 부분 ##
def print_poly(px):
    """
    다항식 표현
    :param px: 계수를 가지고 있는 리스트
    :return:
    """
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
        coef = px[i]  # 계수
        if term == len(px) - 1:
            if coef == 0:
                term = term - 1
                continue
            elif coef > 0:
                poly_str = poly_str + f"{coef}x^{term}"
                term = term - 1

            else:
                poly_str = poly_str + f"{coef}x^{term}"
                term = term - 1
        elif(term == 0):
            if coef == 0:
                break
            elif coef > 0:
                poly_str = poly_str + "+" + f"{coef}"
            else:
                poly_str = poly_str + f"{coef}"
        else:
            if coef == 0:
                term = term - 1
                continue
            elif coef > 0:
                poly_str = poly_str + "+" + f"{coef}x^{term}"
                term = term - 1

            else:
                poly_str = poly_str + f"{coef}x^{term}"
                term = term - 1

        # if coef == 0:
        #     term = term -1
        #     continue
        # elif coef > 0:
        #     poly_str = poly_str + "+" + f"{coef}x^{term}"
        #     term = term - 1
        #
        # else:
        #     poly_str = poly_str + f"{coef}x^{term}"
        #     term = term - 1

    return poly_str


def clac_poly(xvalue, p_x):
    """
    다항식 계산
    :param xvalue: 다항식에 대입할 x 값
    :param p_x: 다항식의 계수
    :return: 다항식의 결과값.
    """
    ret_value = 0
    term = len(p_x) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = p_x[i]  # 계수
        ret_value += coef * xvalue ** term
        term = term - 1

    return ret_value


## 전역 변수 선언 부분 ##
px = [7, -0, 0, 5]

## 메인 코드 부분 ##
if __name__ == "__main__":
    pstr = print_poly(px)
    print(pstr)

    x_value = int(input("X 값-->"))

    px_value = clac_poly(x_value, px)
    print(px_value)


