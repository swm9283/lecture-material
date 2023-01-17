#list
#copy
primes = [2,19,3.0,5,7,11]
primes_cp=primes
print(primes)
print(primes_cp)
primes[-1] = "lunch time"
print(primes)
print(primes_cp)
primes_cp[0] = "morning coffe"
print(primes)
print(primes_cp)

#얕은 카피
#같은 사물함을 사용하기 때문에 일어나는 문제이다.
#참조의 형태일 경우 이 방식 주로 사용한다.
# .copy() method list() 변환함수 슬라이스 [:]
prac = [1,2,[3,2]]
prac_copy = prac.copy()
prac_list = list(prac)
prac_slice = prac[:]
print(prac,prac_copy,prac_list,prac_slice)
prac[2][0] = 1
prac[1] = -77 #immutable type이므로 영향을 받지 않는다.
print(prac,prac_copy,prac_list,prac_slice)



#딥카피
#명확하게 별도의 사본이 필요할 경우
#
import copy
a = [1,2,[5,-9]]
b=copy.deepcopy(a) #별도의 메모리 공간을 받은 것이다.
a[2][1] = 7 #mutable, but deepcopy b is not affected
print(a,b)












#  sort

#  TypeError: '<' not supported between instances of 'str' and 'int'
mixed = [6,4,5,"A",7,"트와이스","B","마마무"]
mixed.sort()
print(mixed)



#문자형일 때 숫자 영어(대문자, 소문자) 한글 : 사전 순으로 정렬된다.
mixed = ["6","4","5","A","7","트와이스","B","마마무","b"]
# mixed.sort()
mixed.sort(reverse=True) #  역순
print(mixed)




# primes = [2,19,3.0,5,7,11]
# print(primes)
# primes.sort()
# print(primes)




# primes_sorted = sorted(primes)
# print(primes)
# print(primes_sorted)