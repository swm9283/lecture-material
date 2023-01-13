#mission 1
import random
secret = random.randint(1,10)
guess = int(input("1~10사이의 숫자를 입력하시오 :"))
if guess < secret:
    print("too low")
elif guess > secret:
    print("too high")
else:
    print("just right")