"""Server."""

import os
import socket
import threading

sock = socket.socket()
print("Socket created successfully.")
PORT = 8800
HOST = ""
sock.bind((HOST, PORT))

src = os.walk("src/assets")
src_list = []
for item in src:
    for value in item[2]:
        # print(idex)
        src_list.append(os.path.join("src", "assets", value))

PATH = "".join(f"{value}-" for value in src_list)


def handle_client(client):
    """Handel client."""
    print("Connected")
    while True:
        print("wait for client")
        data = client.recv(1024)
        print(data.decode())
        if not data:
            break
        if "get-list" in data.decode():
            client.sendall(PATH.encode())
            continue
        index = int(data.decode())
        file_name = os.path.basename(src_list[index])
        client.sendall(str(file_name).encode())
        size = os.path.getsize(src_list[index])
        print(size)
        client.send(str(size).encode())
        with open(src_list[index], "rb") as file:
            line = file.read(1024)
            while line:
                client.sendall(line)
                line = file.read(1024)
                print(line)
        # client.sendall(b'end')

        print("File has been transferred successfully.")

    client.close()


sock.listen()
print("Listening...")
for number in range(100):
    print(number)
    client_soc, address = sock.accept()
    threading.Thread(target=handle_client, args=(client_soc,)).start()
sock.close()
# while True:
#     client_soc, address = sock.accept()
#     threading.Thread(target=handle_client, args=(client_soc,)).start()
# sock.close()
