#간단한 복습
# list tuple offset 가능 딕셔너리 set : offset 불가능

def do_nothing():
    pass
do_nothing()

def make_a_sound():
    print("quack")
make_a_sound()

def agree():
    return True
if agree():
    print("Splendid!")
else:
    print("That was unexpected")

def blackskirt(everything):
    return everything + " " + everything
print(blackskirt("anything"))

# anything 인수(argument)  everything 매개변수(parameter)

def commentary(color):
    if color == "red":
        return "It's a tomato"
    elif color == "green":
        return "It's a green pepper"
    elif color == "bee purple":
        return "I dont't know what it is, but only bees can see it"
    else:
        # return "I've never heard of the color " + color + "."
        print("I've never heard of the color " + color + ".")
        #print는 값을 반환하지않고 주어진 인수를 출력하고 끝난다. 값을 반환하려면 return으로 사용하면 된다.
        #함수가 명시적으로 return을 호출하지 않으면, 호출자는 반환값으로 None을 얻는다.
comment = commentary("blue")
print(comment)

print(do_nothing())


# None != False
thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing") #None이 False처럼 보일 수 있다.

if thing is None: # True 값을 반환
    print("It's some thing")
else:
    print("It's no thing")

if thing is False: #False 값을 반환
    print("It's some thing")
else:
    print("It's no thing") # None != False

def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")
whatis(None)
whatis(True)
whatis(False)
whatis(0)
whatis(0.0)
whatis("")
whatis(" ") #공백도 문자열이다.
whatis(())
whatis({})
whatis([])
whatis(set())
whatis(123) #0을 제외한 모든 수는 True이다.

def menu(wine,entree,dessert):
    return  {"wine": wine, "entree": entree, "dessert": dessert}
#위치 인수
#
dinner = menu("바디감 진한 와인","steak","내가 좋아하는 에그타르트")
print(dinner)
dinner2 = menu("steak","바디감 진한 와인","내가 좋아하는 에그타르트")
print(f"오늘의 저녁은 와인으로는 {dinner2['wine']}을 마시고 메인요리로는 {dinner2['entree']}를 먹고 마무리로는 깔끕하게 {dinner2['dessert']}로 할거에요")

print(menu(wine= "바디감 진한 와인", entree = "steak", dessert = "에그타르트" ))


def menu2(wine,entree,dessert="pudding"):
    return {"wine": wine, "entree": entree, "dessert": dessert}

print(menu2(wine="바다김 진한 와인",entree="스테이크"))


# 기본 인수는 함수가 실행될 때 계산되지 않고, 함수를 정의할 때 계산된다.
def buggy(arg, result = []):
    result.append(arg)
    print(result)
buggy("a")
buggy("b")

def works(arg):
    result = []
    result.append(arg)
    return result
print(works("a"))
print(works("b"))

def nonbuggy(arg,result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy("a")
nonbuggy("b")

#위치 인수 분해하기/모으기 : *
# 매개변수에서 위치 인수 변수를 튜플로 묶는다.

def print_args(*args):
    print("Positional tuple:", args)

print_args(3,2,1,"wait!","uh...")
print_args(2,5,6,"x")
args = (2,6,7,"x")
print_args(args)
print_args(*args)

def print_kwargs(**kwargs):
    print("Keyword arguments:",kwargs)

print_kwargs()
print_kwargs(wine="merlot",entree="mutton",dessert="macaroon")
kwargs = {"wine":"merlot","entree":"mutton","dessert":"macaroon"}
print_kwargs(**kwargs)

def print_data(data,*,start=0,end=100):
    for value in (data[start:end]):
        print(value)
data=["a","b","c","d","e","f"]
print_data(data)
# print_data(data,4,2)

outside = ["one","fine","day"]
def mangle(arg):
    arg[1] = "terrible"

mangle(outside)
print(outside)

def answer():
    print(42)
answer()

def run_something(func):
    func()
run_something(answer)

def add_args(arg1,arg2):
    print(arg1+arg2)
print(type(add_args))

def run_something_with_args(func,arg1,arg2):
    func(arg1,arg2)

run_something_with_args(add_args,5,9)


def sum_args(*args):
    return sum(args)

def run_with_positional_args(func, *args):
    return func(*args)
print(run_with_positional_args(sum_args,1,2,3,4))

def outer(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)
print(outer(4,7))

def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s' " % quote
    return inner(saying)
print(knights('Ni'))

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s' " % saying
    return inner2

a = knights2("Duck")
b = knights2("Hasenpfeffer")
print(type(a),type(b))
print(a)
print(b)
print(a())
print(b())

def edit_story(words, func):
    for word in words:
        print(func(word))
stairs = ['thud','meow','thud','hiss']

def enliven(word): # 첫 글자를 대문자로 만들고 느낌표 붙이기
    return word.capitalize() + '!'

edit_story(stairs,enliven)

edit_story(stairs, lambda word : word.capitalize() + "!")

# 제너레이터
def my_range(first=0,last=10,step=1):
    number = first
    while number < last:
        yield number
        number = number + 1
print(type(my_range))

ranger = my_range(1,5)
print(ranger)

for x in ranger:
    print(x)

for try_again in ranger: # 제너레이터는 한 번만 순회할 수 있다.
    print(try_again)

genobj = (pair for pair in zip(["a","b"],["1","2"]))

for thing in genobj:
    print(thing)

#zip에 대해서 다시 공부하자.
b = ["a","b"]
c = ["1","2"]
a = list(zip(b,c))
print(a)

#데커레이터
def document_it(func):
    def new_function(*args,**kwargs):
        print("Running function:",func.__name__)
        print("Positional arguments:",args)
        print("Keyword arguements", kwargs)
        result = func(*args,**kwargs)
        print("Result:", result)
        return result
    return new_function

#수동으로 데커레이터를 적용
def add_ints(a,b):
    return a + b
print(add_ints(3,5))
cooler_add_ints = document_it(add_ints)
print(cooler_add_ints(3,5))

#@데커레이터_이름
@document_it
def add_ints2(a,b):
    return a+b
print(add_ints2(3,5))

#여러개의 데코레이터를 가질 수 있다.
def square_it(func):
    def new_function(*args,**kwargs):
        result = func(*args,**kwargs)
        return result * result
    return new_function
@document_it
@square_it
def add_ints(a,b):
    return a + b
print(add_ints(3,5))

@square_it
@document_it
def add_ints(a,b):
    return a + b
print(add_ints(3,5))

#네임스페이스와 스코프
animal = "fruitbat"
def print_global():
    print("inside print_global: ",animal)


def change_and_print_gloabl():
    print("inside cnage_and_print_global :", animal)
    animal = "wormbat"
    print("after the change:", animal)

# change_and_print_gloabl()

def works():
    global animal
    # nonlocal animal
    print("before change:", animal)
    animal = "wormbat"
    print("after the change:", animal)
works()


# 전역변수 비지역변수 지역변수
global_variable = "global variables"
def outer():
    nonlocal_variables = "nonlocal variables"
    def inner():
        local_variables = "local variables"

#  variable shadowing
# global_var = "전역 변수"
# def outer():
#     nonlocal_var = "비전역 변수"
#     print(global_var) #가능
#     print(nonlocal_var) #가능
#
#     def inner():
#         local_var = "전역 변수"
#         print(global_var) #가능
#         print(nonlocal_var) #가능
#         print(local_var) #가능
#     print(local_var) #불가능
# print(global_var) #불가능
# print(nonlocal_var) #불가능
# print(local_var) #불가능

#재귀함수
def dive():
    return dive()

#팩토리얼 함수를 만들어보자.

def factorial_recursive(n):
    '''
    재귀함수를 이용한 순열함수
    :param n: n!
    :return: n!를 계산한 결과를 반환 (integer)
    '''
    if n == 1:
        return 1
    else:
        return factorial_recursive(n-1) * n
print(factorial_recursive(5))

def factorial_iteration(n):
    '''
    반복문을 이용한 순열함수
    :param n: n!
    :return: n!를 계산한 결과를 반환 (integer)
    '''
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
print(factorial_iteration(5))

short_list = [1,2,3]
position = 5
try:
    short_list[position]
except:
    print(f"Need a position 0 and {len(short_list)-1} but got {position}")

try:
    # raise Exception("쉬는 시간")
    # raise TypeError("타입에러")
    expr = input('분자 분모 입력 (띄어쓰기로 구분): ').split()
    print(int(expr[0]) / int(expr[1]))
except ValueError as err:
    print(f'숫자를 입력해주세요 ({err})')
except ZeroDivisionError as err:
    print(f'분모에 0이 올 수 없습니다 ({err})')
except IndexError as err:
    print(f'입력 값의 범위에 문제가 있습니다 ({err})')
except Exception as other:
    print(f'예외 발생 : {other}')
else:  # 예외가 발생 하지 않았을 때
    print('프로그램 정상', end=' ')
finally:  # 예외 발생 여부와 상관 없이 무조건 실행
    print('종료')





































