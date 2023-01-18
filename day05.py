# function
# #input 2 numbers
# # 두 수 사이의 소수만 출력하게끔 해주세요.

#소수인지 판단하는 함수
def isprime(n):
    """
    매개변수로 받은 수가 소수인지 여부를 판단하는 함수
    :param n: integer number
    :return: retrun True or False
    """
    if n <= 1:
        return False
    for k in range(2,n):
        if n % k == 0:
            return False
    else:
        return True

print(isprime(100))
help(isprime) # 내가 작성한 코드의 도움말 확인!

start = int(input(" enter the start number : "))
end = int(input("enter the end number : "))
if end < start:
    start, end = end, start
for i in range(start, end+1):
    if isprime(i):
        print(i, end=" ")
