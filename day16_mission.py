#현재 위치부터 가까운 편의점 관리하기.
import random
from string import ascii_uppercase
class Node:
    def __init__(self,data):
        self.data = data # (편의점이름,x좌표,y좌표)의 튜플형태의 자료를 받는다.
        self.link = None

def calc_distance(x,y):
    return (x**2 + y**2)**(1/2)
def printNodes(start):
    current = start
    if current == None:
        print("None")
        return
    print(current.data,end=" ")
    while current.link!=start:
        current = current.link
        print(current.data,end=" ")
    print()



def sort_by_distance(sort_data):
    global pre, current,head
    printNodes(head)


    if head is None:
        node = Node(sort_data)
        head = node
        node.link = head
        return

    node = Node(sort_data)
    current = head1

    if calc_distance(head.data[1],head.data[2]) > calc_distance(sort_data[1],sort_data[2]):
        node.link= head
        head = node
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        return

    #중간 삽입 <- 이 부분 손보자.
    while current.link != head:
        pre = current
        current= current.link
        if calc_distance(current.data[1],current.data[2]) > calc_distance(sort_data[1],sort_data[2]):
            pre.link = node
            node.link = current
            return

                #마지막 추가
    current.link = node
    node.link = head




#  global variables

pre, current, head = None, None, None
# make the alphabet_list uppercase
alphabet_list = list(ascii_uppercase)
print(alphabet_list)
#  make the convenient_store data.
data_array = []
for i in range(0, 11, 1):
    data_array.append((alphabet_list[i], random.randint(1, 100), random.randint(1, 100)))
distance_data = []
for i in range(0, 11, 1):
    distance_data.append(calc_distance(data_array[i][1], data_array[i][2]))

if __name__ =="__main__":
    for i in data_array:
        sort_by_distance(i)
    printNodes(head)