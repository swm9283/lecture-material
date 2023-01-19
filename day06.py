#generator

#대표적인 예는 range() function이다. 이 방식으로 이해하면 쉽다.
def a(): # generator
    yield 1
    yield 2
    yield 3

def b(): #normal function
    return 1 # function stop
    return 2 #죽은 코드
    return 3 #죽은 코드

print(a(),b())
for i in a():
    print(i)

c = a()
print(c)
for i in c:
    print(i)

for i in c: # generator는 한 번만 순회할 수 있다.
    print(i)

#zip에 대해 공부하자.
a = list(zip(["a","b"],["1","2"]))
print(a)
print(type(a[0]))

