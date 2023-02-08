## 클래스 및 함수 선언 부분 ##
# 깊이 우선 탐색.
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


## 전역 변수 선언 부분 ##
G1 = None
stack = []  #  다음 방문할 vertex를 담는다.
visitedAry = []  # 방문한 정점
A, B, C, D, E, F, G, H, I = 0, 1, 2, 3, 4, 5, 6, 7, 8

## 메인 코드 부분 ##
G1 = Graph(9)
# A
G1.graph[A][1] = 1
G1.graph[A][2] = 1
G1.graph[A][4] = 1
# B
G1.graph[B][0] = 1
G1.graph[B][2] = 1
G1.graph[B][3] = 1
# c
G1.graph[C][0] = 1
G1.graph[C][1] = 1
G1.graph[C][3] = 1
G1.graph[C][4] = 1
G1.graph[C][5] = 1
# d
G1.graph[D][1] = 1
G1.graph[D][2] = 1
# e
G1.graph[E][0] = 1
G1.graph[E][2] = 1
G1.graph[E][6] = 1
G1.graph[E][7] = 1
# f
G1.graph[F][2] = 1
# g
G1.graph[G][4] = 1
G1.graph[G][8] = 1
# h
G1.graph[H][4] = 1
G1.graph[H][8] = 1
# i
G1.graph[I][6] = 1
G1.graph[I][7] = 1
#
# print("## G1 무방향 그래프 ##")
# for row in range(9):
#     for col in range(9):
#         print(G1.graph[row][col], end=" ")
#     print()

current = 0  # 시작 정점 A
stack.append(current)  # push
visitedAry.append(current)  # push

while len(stack) != 0:
    next = None
    for vertex in range(9):
        if G1.graph[current][vertex] == 1:
            if vertex in visitedAry:  # 방문한 적이 있는 정점이면 탈락
                pass
            else:  # 방문한 적이 없으면 다음 정점으로 지정
                next = vertex
                break

    if next != None:  # 다음에 방문할 정점이 있는 경우
        current = next
        stack.append(current)
        visitedAry.append(current)
    else:  # 다음에 방문할 정점이 없는 경우
        current = stack.pop()


print("방문 순서 -->", end="")
for i in visitedAry:
    print(chr(ord("A") + i), end="   ")
