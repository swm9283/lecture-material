#특수 다항식 처리 프로그램

## 함수 선언 부분 ##
def print_poly(t_x, p_x):
    poly_str = "P(x) = "

    for i in range(len(p_x)):
        term = t_x[i]  # 항 차수
        coef = p_x[i]  # 계수

        if (coef >= 0):
            poly_str += "+"
        poly_str += str(coef) + "x^" + str(term) + " "

    return poly_str


def calc_poly(x_val, t_x, p_x):
    ret_value = 0

    for i in range(len(px)):
        term = t_x[i]  # 항 차수
        coef = p_x[i]  # 계수
        ret_value += coef * x_val ** term

    return ret_value


## 전역 변수 선언 부분 ##
tx = [300, 20, 0]
px = [7, -4, 5]

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = print_poly(tx, px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calc_poly(xValue, tx, px)
    print(pxValue)
