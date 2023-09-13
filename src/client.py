"""Main."""
import socket

print("Socket created successfully.")

PORT = 8800
HOST = "localhost"


while True:
    sock = socket.socket()
    sock.connect((HOST, PORT))
    print("Connection Established.")
    data_list = sock.recv(1024).decode().split("-")
    data_list.pop(len(data_list) - 1)
    print("List of Files: ")
    for index, value in enumerate(data_list):
        print(index, ".", value)
        print("-----------------------")

    INDEX = str(input("\nchoose number of file you want to download: "))

    sock.send(INDEX.encode())
    recv_data = sock.recv(1024).decode()
    file_name = recv_data
    with open(file_name, "wb") as file:
        line = sock.recv(1024)
        while line:
            file.write(line)
            line = sock.recv(1024)

        print("File has been received successfully.")
    answer = input("you want to download again?(y/n)").lower()
    sock.close()

    if answer == "n":
        print("Connection Closed.")
        break
