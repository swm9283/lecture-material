# #input 2 numbers
# # 두 수 사이의 소수만 출력하게끔 해주세요.

start = int(input("start and end number : "))
end = int(input("start and end number : "))
if end < start:
    start, end = end, start

for k in range(start,end+1):
    if k <= 1:
        continue
    for i in range(2, k):
        if k % i == 0:
            break
    else:
        print(k, end=" ")






