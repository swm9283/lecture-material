#  list
# scores = ("A+","B+","C+")
# print(scores[0])
# # scores[1] = " B+" : 튜플은 immutable]
#
# #  일시적으로 list로 변환
# temp = list(scores)
# temp[0] = "B+"
# temp[1] = "A+"
# #  다시 튜플로 변환
# scores = tuple(temp)
# print(scores[0])
# print(scores[1])
# print(scores)
#
#
# #문자열 분할로 생성하기 : split()

big_bang = ["GD","태양","탑","대성","승리"]
exo = ["백현","첸"]
#  big_bang.append("인하") #뒤에 삽입
big_bang.insert(1,"인하") #원하는 위치에 삽입
#  exo.extend(big_bang)
#  exo = exo + big_bang
exo.append(big_bang) # 리스트 안에 리스트를 넣었다.
print(exo)
print(exo[-1][-4]) #역방향 태양
print(exo[2][2]) #태양

exo[-2] = "시우민" #리스트는 mutable
print(exo)

#삭제하기
# print(exo.pop()) # 빅뱅 pop
print(exo[2].pop()) # 승리 pop
print(exo[2].pop(-2)) # 탑 pop
del exo[2][-1] # 대성 delete
# exo[2].remove("인하") not in exo
exo[2].remove("인하")

exo.clear()
print(exo) #unit 활동 종료

#원하는 값 찾기 : .index("값")

#존재 여부 확인하기 : in

#값 세기 : count()

#문자열로 변환하기 : join()

#정렬하기
# .sort() :원본을 바꿀 때
# sorted() :복사본을 만들 때

































































