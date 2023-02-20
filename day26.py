from operator import itemgetter


## 함수 선언 부분 ##
def make_index(ary, pos):
    # beforeAry = []
    # index = 0
    # for data in ary:
    #     beforeAry.append((data[pos], index))
    #     index += 1
    beforeAry = [[ary[i][pos], i] for i in range(len(ary))]

    sortedAry = sorted(beforeAry, key=itemgetter(0))
    return sortedAry


def search_book(ary, fData):
    pos = -1
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        if fData == ary[mid][0]:
            return ary[mid][1]
        elif fData > ary[mid][0]:
            start = mid + 1
        else:
            end = mid - 1

    return pos


## 전역 변수 선언 부분 ##
book_array = [
    ["어린왕자", "쌩떽쥐베리"],
    ["이방인", "까뮈"],
    ["부활", "톨스토이"],
    ["신곡", "단테"],
    ["돈키호테", "세르반테스"],
    ["동물농장", "조지오웰"],
    ["데미안", "헤르만헤세"],
    ["파우스트", "괴테"],
    ["대지", "펄벅"],
]
nameIndex = []
authIndex = []

## 메인 코드 부분 ##
print("#책장의 도서 ==>", book_array)
nameIndex = make_index(book_array, 0)
print("#도서명 색인표 ==>", nameIndex)
authIndex = make_index(book_array, 1)
print("#작가명 색인표 ==>", authIndex)

findName = "신곡"
findPos = search_book(nameIndex, findName)
if findPos != -1:
    print(findName, "의 작가는", book_array[findPos][1], "입니다.")
else:
    print(findName, " 책은 없습니다.")

findName = "괴테"
findPos = search_book(authIndex, findName)
if findPos != -1:
    print(findName, "의 도서는", book_array[findPos][0], "입니다.")
else:
    print(findName, " 작가는 없습니다.")
