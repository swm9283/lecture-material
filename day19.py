import tkinter as tk


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
    # global memos, count_memo_recursion
    # count_memo_recursion = count_memo_recursion + 1
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


def fact_recu(n):
    if n == 1:
        return 1
    else:
        return n * fact_recu(n - 1)


print(fact_recu(5))


# print(fact_recu(5))


def factorial_input():
    lbl_results.config(text=f"계산기 출력 결과 : {fact_recu(int(en_num_input.get()))}")


def fibonacci_input():
    lbl_results.config(text=f"계산기 출력 결과 : {fibo_memo_recu(int(en_num_input.get()))}")


win = tk.Tk()  # 윈도우 생성
win.title("Calculater")  # 피보나치, 팩토리얼 계산기
win.geometry("250x100")

en_num_input = tk.Entry()  # 텍스트 입력 상자
lbl_results = tk.Label(text="계산기 출력 결과 :")  # 레이블 , 계산 결과 출력용
btn_fact = tk.Button(text="팩토리얼", command=factorial_input)  # 레이블,
btn_fibo = tk.Button(text="피보나치", command=fibonacci_input)  # 레이블 피보나치 계산


# 레이아웃 (grid or place 사용가능)
en_num_input.pack()
lbl_results.pack()
btn_fact.pack(fill="x")
btn_fibo.pack(fill="x")

win.mainloop()
