#function
#함수를 인수로 받아서 매개변수로 던질 수 있다.
#함수 안에 함수를 또 정의할 수 있다.(inner function)
#closure nolocal local variable에 대한 공부!
#closure 매우 중요한 개념이다. 여러번 봐보자
def calculate():
    x = 1
    y = 2
    temp = 0

    def add_sub(n):
        # nonlocal x #nonlcal을 사용하면 지역변수를 변경할 수 있다.
        nonlocal temp #calculate 내의 temp와 add_sub의 temp가 같다.
        # x = 11 # local variable
        temp = temp + x + n - y  # add_sub가 x,y를 기억하고 있다.
        return temp
    print("once")
    return add_sub #합수 이름이 return값.

c1 = calculate()

for i in range(5):
    print(c1(i)) # add_sub에 i를 넣은 것과 같다. calculate는 한 번 돌아가는데 그 와중에 add_sub가 5번 돌아가네
print(type(c1))
print(c1)
