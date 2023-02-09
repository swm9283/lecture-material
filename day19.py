def fibo_recu(n):
    """
    재귀함수를 사용한 피보나치 수열 처리
    :param n:
    :return:
    """
    global count_recursion
    count_recursion = count_recursion + 1
    if n <= 1:
        return n
    else:
        return fibo_recu(n - 1) + fibo_recu(n - 2)


def fibo_iteration(n):
    """
    반복문을 사용한 피보나치 수열 처리
    :param n:
    :return:
    """
    r = list()
    p1, p2 = 1, 1
    for _ in range(n):
        r.append(p1)
        p1, p2 = p2, p1 + p2
    return r[-1]


memos = [None for _ in range(100)]
memos[0], memos[1] = 0, 1  # 전역 변수로 한 번 처리한 결과 값을 저장


def fibo_memo_recu(n):
    """
    Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global memos, count_memo_recursion
    count_memo_recursion = count_memo_recursion + 1
    if n <= 1:
        return memos[n]

    if memos[n] is not None:  # 전역 메모리 memos에 이전에 계산한 결과 값이 존재하면 재귀함수를 호출하지 않겠다.
        return memos[n]
    else:
        memos[n] = fibo_memo_recu(n - 2) + fibo_memo_recu(n - 1)  # 처음 방문하는 n이면
        return memos[n]


def fibo_memo(n):
    """
    Memoization(DP)을 사용한 피보나치 수열 처리 함수
    :param n:
    :return:
    """
    global count_memoization
    count_memoization = count_memoization + 1
    memo = [0, 1]
    if n <= 1:
        return memo[n]
    else:
        for i in range(2, n + 1):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n]


count_memoization = 0
count_recursion = 0
count_memo_recursion = 0

for i in range(2, 30):
    print(f" {i} : {fibo_memo(i)}")  ## memoization
print("####################")
print("피보나치 수 --> 0 1 ")
# for i in range(2, 40):
#     print(f" {i} : {fibo_iteration(i)}") ## iteration
print("####################")
print("피보나치 수 --> 0 1 ")
for i in range(2, 30):
    print(f" {i} : {fibo_recu(i)}")  # recursion 역시 재귀는 오버헤드 때문에 느리네


for i in range(2, 30):
    print(f" {i} : {fibo_memo_recu(i)}")  ## memoization


print(f"재귀 : {count_recursion} 메모: {count_memoization} 재귀 메모: {count_memo_recursion}")
