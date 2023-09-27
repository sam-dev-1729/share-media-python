"""Client."""
import os
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
        if item != "":
            listbox.insert(tk.END, os.path.basename(item))


def popupmsg(msg, geometry="220x150"):
    """Popup."""
    popup = tk.Tk()
    popup.geometry(geometry)
    popup.wm_title("Notice!")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=20)
    btn = ttk.Button(popup, text="Okay", command=popup.destroy)
    btn.pack()
    popup.mainloop()


def download_file():
    """Download file."""
    file_index = listbox.curselection()[0]

    # filename = listbox.get(index)
    # print('file', filename,index,)

    sock.sendall(str(file_index).encode())
    recv_filename = sock.recv(1024).decode()
    try:
        size = int(sock.recv(1024).decode())
        if size == -1:
            raise FileNotFoundError
        received = 0
        # progress =ttk.Progressbar(orient='horizontal',
        # maximum=100,length=300, mode='determinate')
        # progress.pack()
        download_path = os.path.join("src", "downloads", recv_filename)
        # src = os.walk("src/downloads")
        # for item in src:
        #     for value in item[2]:
        #         # print(idex)
        #         if value == recv_filename:
        #             popupmsg(f'you already download the
        #                       {recv_filename} file')
        #             break

        with open(download_path, "wb") as file:
            while received < size:
                # progress['value'] = received / size * 100
                # progress.place()
                data = sock.recv(1024)
                received += len(data)
                file.write(data)
        popupmsg(f"{recv_filename} downloaded successfully!")
    except FileNotFoundError:
        popupmsg(f"{recv_filename} not found!")


def upload():
    """Upload to server."""
    print("pressed")


root = tk.Tk()
root.geometry("350x350")
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
