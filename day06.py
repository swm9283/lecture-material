# namespace와 scope.
g = 1 #전역변수
def print_global():
    # g = 1 #지역변수  # print_gloabl socpe에 가려져서 보이지 않는다.
    print(g)
print_global()
print(g) # print_gloabl socpe에 가려져서 보이지 않는다.

def change_print_global():
    global g
    print(g) #global g를 사용안할 시 전역변수 g를 사용할 수 없다.
    g=2
    print(g)
change_print_global()

print(globals())
print(__name__)