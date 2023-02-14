# python client socket
import socket

print("에코 클라이언트 시작됨!")
# client socket 생성.
client_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM
)  # datagram으로 만들 떄는 socket.SOCK_Datagram 사용하면 된다.
# connect
client_socket.connect(("165.246.115.165", 20000))
print("서버에 연결됨.")

# 데이터 송수신
while True:
    msg = input("전송 메시지 입력 : ")
    if msg == "EXIT" or msg == "exit":  # 종료
        break
    client_socket.sendall((msg + "\n").encode())  # 송신

    data = client_socket.recv(1024).decode()  # 수신
    print(f"서버로 받은 메시지 : {data}")

# 소켓 닫기.
client_socket.close()
