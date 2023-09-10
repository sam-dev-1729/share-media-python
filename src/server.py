"""Server."""
import socket

sock = socket.socket()
print("Socket created successfully.")

PORT = 8800
HOST = ""

sock.bind((HOST, PORT))

sock.listen(10)
print("Socket is listening...")

while True:
    client, addr = sock.accept()
    print("Connected with ", addr)

    data = client.recv(1024)
    print(data.decode())
    client.send("vide.mp4".encode())
    with open(data.decode(), "rb") as file:
        line = file.read(1024)
        while line:
            client.send(line)
            line = file.read(1024)

    print("File has been transferred successfully.")

    client.close()
