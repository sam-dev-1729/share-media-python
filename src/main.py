"""Main."""
import os
import socket

sock = socket.socket()
print("Socket created successfully.")

PORT = 8800
HOST = "localhost"

sock.connect((HOST, PORT))
print("Connection Established.")

text = os.path.join("src", "assets", "text.txt")
video = os.path.join("src", "assets", "video.mp4")
image = os.path.join("src", "assets", "image.png")
sound = os.path.join("src", "assets", "sound.mp3")

sock.send(image.encode())
name = sock.recv(1024)
with open(name.decode(), "wb") as file:
    line = sock.recv(1024)

    while line:
        file.write(line)
        line = sock.recv(1024)

    print("File has been received successfully.")

    file.close()
    sock.close()
    print("Connection Closed.")
