#prime number
#while문 사용 version 1
number = int(input(" input number : "))
counts = 0
k = 1
while k <= number:
    if number % k == 0:
        counts = counts + 1
    k = k + 1
if counts == 2:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")

#for문사용 version2
number = int(input(" input number : "))
counts = 0
for i in range(1,number+1):
    if number % i ==0:
        counts = counts +1
if counts == 2:
    print(f"{number} is prime number")
else:
    print(f"{number} is not prime number")

#for문사용 version3, 반복을 조금이라도 줄임
number = int(input(" input number : "))
counts = 0
for i in range(2,number):
    if number % i ==0:
        counts = counts +1
if counts:
    print(f"{number} is not prime number")

else:
    print(f"{number} is prime number")

#version4 bool type을 사용!
number = int(input(" input number : "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
#    print(i)
if is_prime:
    print(f"{number} is prime number")

else:
    print(f"{number} is not prime number")

#version6 bool tpye에 break 추가 엄청난 성능발전!
number = int(input(" input number : "))
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
#    print(i)
if is_prime:
    print(f"{number} is prime number")

else:
    print(f"{number} is not prime number")
