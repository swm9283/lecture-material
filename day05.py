#function

def inha():
    """
    숫자출력
    :return:
    """
    print(60)


def call_func(f):
    """
    매개변수로 함수를 넘겨받아 실행
    :param f:  매개변수가 함수
    :return:
    """
    f() #넘겨 받은 함수 실행

call_func(inha)
print(type(call_func))

def subtract(n1,n2):
    print(n1-n2)


def run_fucntion(func,arg1,arg2):
    """
    함수를 매개변수로 받아 함수 안에서 해당함수를 실행
    :param func: 첫번째 인수는 함수
    :param arg1: 정수 값
    :param arg2: 정수 값
    :return:
    """
    func(arg1,arg2) #넘겨 받은 함수 실행, arg1과 arg2는 넘겨 받은 함수의 인수로 들어가게된다.


















