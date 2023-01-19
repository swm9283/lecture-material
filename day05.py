def calculate():
    x = 1
    y = 2
    temp = 0
    def add_sub(n):
        nonlocal temp
        temp = temp + x + n - y
        return temp
    print("once")
    return add_sub
c1 =calculate()
for i in range(5):
    print(c1(i))

def echo(anything):
    return anything + " " + anything


thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

thing =None
if thing is None:
    print("It's Nothing")
else:
    print("It's something")
a = ['']
print(a)
print(type(a))

def buggy(arg,result = []):
    result.append(arg)
    print(result)
buggy("a")
buggy("b")

def nonbuggy(arg):
    result = []
    result.append(arg)
    print(result)
nonbuggy("a")
nonbuggy("b")

def nonbuggy2(arg,result = None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
nonbuggy2("a")
nonbuggy2("a")
