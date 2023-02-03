best_friends= [("다현",200),("정연",100),("쯔위",90),("사나",30),("지효",15)]

#위치를 찾아야돼.

def add_friends(data):
    len_best_friends = len(best_friends)
    best_friends.append(None)
    for i in range(len_best_friends-1,-1,-1):
        if data[1] >= best_friends[i][1]:
            best_friends[i+1] = best_friends[i]
            best_friends[i] = data
    print(best_friends)
def question():
    name = input("추가할 친구를 입력하세요 :")
    number = int(input("횟수를 입력하세요 : "))
    data = (name,number)
    return data
add_friends(question())






