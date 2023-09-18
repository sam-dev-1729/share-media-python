"""Server."""

import os
import socket
import threading

sock = socket.socket()
print("Socket created successfully.")
PORT = 8800
HOST = ""

sock.bind((HOST, PORT))
sock.listen()
print("Socket is listening...")
# text = os.path.join("src", "assets", "text.txt")
# video = os.path.join("src", "assets", "video.mp4")
# image = os.path.join("src", "assets", "image.png")
# sound = os.path.join("src", "assets", "sound.mp3")
src = os.walk("src/assets")
src_list = []
for item in src:
    for value in item[2]:
        # print(idex)
        src_list.append(os.path.join("src", "assets", value))
PATH = "".join(f"{value}-" for value in src_list)

print(PATH)


def send(soc, data):
    """Send."""
    soc.send(str(data).encode())
    # try:
    #     soc.send(str(data).encode())
    # except Exception:
    #     soc.send("error to send data form sever!".encode())


def threaded(client):
    """Threaded."""
    send(client, PATH)
    index = int(client.recv(1024).decode())
    print(index)
    file_name = os.path.basename(src_list[index])
    send(client, file_name)
    with open(src_list[index], "rb") as file:
        line = file.read(1024)
        while line:
            send(client, line)
            line = file.read(1024)

    print("File has been transferred successfully.")
    client.close()


for number in range(100):
    print(number)
    client_soc, addr = sock.accept()
    print("Connected with ", addr)
    threading.Thread(target=threaded, args=(client_soc,)).start()
sock.close()
