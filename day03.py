print("I'm a boy")

#긴 텍스트를 작성할 때

army = '우리는 국가와 국민에 충성을 다하는 대한믹국 육군이다. ' \
       '하나 우리는 자유민주주의를 수호하며 조국 통일의 역군이 된다.'

army2 = ''' 우리는 국가와 국민에 충성을 다하는 대한믹국 육군이다.
하나 우리는 자유민주주의를 수호하며 조국 통일의 역군이 된다.'''
print(army, army2)


# escape
# \n 문자
army3 = '우리는 국가와 국민에 충성을 다하는 대한믹국 육군이다.\n\n하나 우리는 자유민주주의를 수호하며 조국 통일의 역군이 된다.'
print(army3)
# \' \" 로 ' , " 를 표현할 수 있다.
testimony= "\"I dit nothing!\" he said. \"Or that other thing.\""
print(testimony)
#


#str() :문자열로 변환

#복제하기 by using * : 자주 사용하지는 않는다.
start = "Na" * 4 + "\n"
middle = "Hey" * 3 + "\n"
end = "Goodbye"
print(start+start+middle+end)

#슬라이스 offset 0부터 시작함을 명심하자!
univ = "Inha University"
print(univ[5:])
print(univ[5:15])
print(univ[-10:])
print(univ[::2])
print(univ[5:-6])
print(univ[-10:-6])

#len() :문자열의 길이
print(len(univ))

#문자열 나누기 : split 문자열을 리스트로 바꿀 때 많이 사용한다.
#string.split(" ") 디폴트값은 " "
print(univ.split()) #defalt값은 spacebar " "이다.
print(univ.split("i"))


#문자열 합치기 join split과 반대개념이다.
# " ",join(문자열 리스트)
pocketmon_list = ["파카츄", "꼬부기", "이상해", "파이리"]
pocketmon_string = "$".join(pocketmon_list)
print(pocketmon_string)
print(type(pocketmon_string))

#연습

univ_split = univ.split()
print(univ_split)
univ_join = " ".join(univ_split)
print(univ_join)


#문자열 대체하기
inha = "a duck goes into a sea"
print(inha.replace("a","a nice"))
print(inha.replace("a ","a nice ")) #띄어쓰기 하나로 큰 차이가 난다.

#문자열 스트립 : strip()
subject = " $  python, data structure, database    $" #가운데 값은 영향을 받지 않는다, 맨 양 끝에 있는 반복된 값만 제거한다.
print(subject.strip("$"))

blurt = "what the fuck...!??!"
print(blurt.strip(".?!"))

#검색과 탐색!
print(subject.find("data"),subject.index("data"))
print(subject.find("inha"))
# print(subject.index("inha"))
print(subject.rfind("data"))
print(subject.count("data"))

#대소문자
setup = 'a duck goes into a bar...'
setup = setup.strip(".")
print(setup.capitalize())

#정렬, 출력을 예쁘게 할려고





#포메팅
#old modern ultra modern
#예전 포맷들도 알아야한다.

song="""When an eel grabs your arm,
and it causes great harm,
That's -  a moray"""
print(song.rfind("m"))
index = song.rfind("m")
song_upper = song[index].upper()
print(index)
song_after = song[:index] + song_upper + song[index+1:]
print(song_after)
















































































