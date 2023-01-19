# recursion 재귀함수
def factorial_iter(n):
    """
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return: integer 팩토리얼 게싼 결과 값.
    """
    result = 1
    for k in range(1,n+1):
        result = result * k
    return result
print(factorial_iter(5))

def factorial_recu(n):
    """
    재귀 함수를 이용한 팩토리얼 함수
    :param n: n!
    :return:  자기 자신을 호출 또는 1
    """
    if n == 1: # 끝나는 조건
        return 1
    else:
        return factorial_recu(n-1) * n # factorial_recu가 (n-1)!이라는 의미를 내포하고 있다.

print(factorial_iter(1000))
print(factorial_recu(1000))



