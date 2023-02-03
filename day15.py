pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]


def insert_data(position, pokemon):
    if position < 0 or position > len(pokemons):
        print("out of range.")
        return

    pokemons.append(None)  # 빈칸 추가
    for i in range(len(pokemons) - 1, position, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[position] = pokemon  # 지정한 위치에 친구 추가


def delete_data(position):
    if position < 0 or position > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    len_pokemons = len(pokemons)
    pokemons[position] = None  # 데이터 삭제

    for i in range(position + 1, len_pokemons):
        pokemons[i - 1] = pokemons[i]
        pokemons[i] = None  # 배열의 맨 마지막 위치 삭제

    del (pokemons[len_pokemons - 1])


if __name__ == "__main__": # main 함수?
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]
    print(pokemons)
    insert_data(2, '거북왕')
    # pokemons.insert(2,"거북왕")  built-in 코드
    print(pokemons)
    insert_data(6, '망나뇽')
    # pokemons.insert(6,"망나뇽")  built-in 코드
    print(pokemons)

    delete_data(1)
    print(pokemons)
