#튜플 immutable 값을 바꿀 수 없다. 반드시 알자!!
#리스트는 mmutable이다
#make the tuple
a = "harry",
b = ("harry",)
c = ()
d = "harry","ron"  #packing
e = ("herimione")  # string
f = ("harry","ron") #packing
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#튜플 수정하기
g = ("heriminone",)
print(id(g))
g = g + f
print(id(g))
print(g)


x,y = f  #unpacking
print(x)
print(y)

#tuple() :다른 객체를 튜플로 만들어준다.
marx_list = ["Groucho","Chico","Harpo"]
marx_tuple = tuple(marx_list)
print(marx_list)
print(marx_tuple)





















