# Client-Server File Transfer

Share-media-python is a simple client-server program for transferring files over a network. It consists of a client script and a server script that communicate over sockets. 

## Client

The client does the following:

- Creates a socket and connects to the server
- Requests the file list from the server and displays it in a Tkinter listbox
- Allows the user to select a file and click the "Download" button
- Sends the index of the selected file to the server
- Receives the filename and size from the server
- Writes the file contents received from the server to disk
- Displays a message when the download is complete

The client handles some errors like:

- File not found on server
- Already existing file

## Server 

The server does the following:

- Creates a socket and listens for clients
- Maintains a list of available files
- Sends the file list when requested by client
- Sends the file name and size when index received
- Reads the file in chunks of 1024 bytes and sends to client

The server handles some errors like:

- File not found

## Usage

- Run the server script 
- Run the client script
- Client connects to server 
- Client requests and displays file list
- Client selects and downloads a file

## Requirements

- Python 3
- socket 
- os
- threading
- Tkinter

This simple client-server program demonstrates socket programming and file transfer in Python. Some improvements can be made like adding encryption, user authentication etc.
