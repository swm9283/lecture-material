# dictionary 중복된 값은 출력되지 않는다.
harry_porter={"헤르미온느":"그리핀도르","말포이" :"슬리데린","론":"그리핀도르","헤르미온느":"그리핀도르"}
print(harry_porter)
print(type(harry_porter))

#
PI=3.14
print(f"원주율의 값은 {PI}이고 타입은 {type(PI)}입니다.")

#chapter 3
#number1
print(2*2*2*2)
print(2**4)
print(pow(2,4))
print(7//2) #정수 나누기
print(7/2) #소수점 나누기
print(7%2) #나머지 연산자

print(type(divmod(9,5)))
print(type((1,2)))
test=1,2 #packing
print(type(test))
a,b = test #unpacking
print(a)
print(b)

#number2
number=154
print(bin(number))
print(hex(number))
print(oct(number))

print(ord("a"))
print(hex(ord(" ")))

#if
limits = 20
tweets = "pass" * 7
diff = limits - len(tweets)
if diff >=0:
    print(tweets)
else:
    print(f"글자 수 {abs(diff)}초과")


vowels ="aeiou"
letter = "u"
if letter in vowels:
    print("실행안됨")

a=[]
print(bool(a))
a.append(1)
print(a)
print(bool(a))
print(bool(set()))














