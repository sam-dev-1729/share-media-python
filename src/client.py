"""Client."""
import socket
import tkinter as tk
from tkinter import ttk

print("Socket created successfully.")

PORT = 8800
HOST = "localhost"

sock = socket.socket()
sock.connect((HOST, PORT))
print("Connection Established.")


def connect_to_server():
    """Connect to server."""
    sock.sendall(b"get-list")
    data = sock.recv(1024)
    if not data:
        return
    decoded = data.decode().split("-")
    for item in decoded:
        listbox.insert(tk.END, item)


def download_file():
    """Download file."""
    file_index = listbox.curselection()[0]

    # filename = listbox.get(index)
    # print('file', filename,index,)

    sock.sendall(str(file_index).encode())
    recv_filename = sock.recv(1024).decode()
    size = int(sock.recv(1024).decode())
    received = 0

    with open(recv_filename, "wb") as file:
        while received < size:
            data = sock.recv(1024)
            received += len(data)
            file.write(data)
    # with open(recv_filename, "wb") as file:
    #     line = sock.recv(1024)
    #     while line:
    #         file.write(line)
    #         line = sock.recv(1024)

    # sock.close()
    # listbox.delete(file_index)


def upload():
    """Upload to server."""
    print("pressed")


root = tk.Tk()

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

download_frame = ttk.Frame(notebook)
notebook.add(download_frame, text="Download")

lbl_download = ttk.Label(download_frame, text="Download File:")
btn_download = ttk.Button(
    download_frame,
    text="Download",
    command=download_file,
)
listbox = tk.Listbox(download_frame)

lbl_download.pack(pady=10)
listbox.pack()
btn_download.pack()

connect_to_server()

upload_frame = ttk.Frame(notebook)
notebook.add(upload_frame, text="Upload")

lbl_upload = ttk.Label(upload_frame, text="Select File to Upload:")
btn_upload = ttk.Button(upload_frame, text="Upload", command=upload)

lbl_upload.pack(pady=10)
btn_upload.pack()

root.mainloop()
