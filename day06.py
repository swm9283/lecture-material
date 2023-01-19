# ex 9-1
def good():
    return ["Harry", "Ron", "Hermione"]
print(good())

# ex 9-2
def get_odds():
    """
    range(10) 중에서 홀수만 generator한다.
    :return: generator
    """
    for i in range(10):
        # if i % 2: # 0이 아닌 수는 모두 True이다.
        if i % 2 == 1:
            yield i
temp = []
for k in get_odds():
    temp.append(k)
print(temp[2])
