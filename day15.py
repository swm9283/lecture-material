def insert_data(position, pokemon):
    if position < 0 or position > len(pokemons):
        print("out of range.")
        return

    pokemons.append(None)  # 빈칸 추가
    for i in range(len(pokemons) - 1, position, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[position] = pokemon  # 지정한 위치에 pokemon 추가


def delete_data(position):
    """
    특정 위치의 data만 삭제.
    :param position:
    :return:
    """
    if position < 0 or position > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)
    pokemons[position] = None  # 데이터 삭제

    for i in range(position + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (pokemons[len_pokemons - 1])


def delete_data_all(position):
    """
    주어진 positon 이후의 모든 값을 지움.
    :param position: integer position
    :return:
    """
    if position < 0 or position > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)

    for i in range(position, len_pokemons - 1):
        # pokemons[i] = None
        pokemons.pop()  # index값이 없으면, 맨 뒤의 값부터 지운다.

    # for i in range(len_pokemons -1, position -1 , -1):
    #     pokemons.pop()


def add_data(pokemon):
    """
    list.append 구현.
    :param pokemon: String of Pokemon name
    :return:
    """
    pokemons.append(None)
    pokemons[len(pokemons) - 1] = pokemon


pokemons = []
select = -1

if __name__ == "__main__":  # main 함수?
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]
    while True:

        select = input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> ")

        if select == "1":
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif select == "2":
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(pokemons)
        elif select == "3":
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(pokemons)
        elif select == "4":
            print(pokemons)
            # exit        #exit에 대해서 알아보자. , exit은 뒤에 코드도 출력한뒤 종료
            break
            # print(1)
        else:
            print("1~4 중 하나를 입력하세요.")
            continue
