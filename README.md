# share-media-python

This project implements a simple client-server application for transferring files over a socket connection.

## Overview

The project consists of a server script (`server.py`) and a client script (`client.py`). 

The server sets up a listening socket on port 8800 and waits for incoming client connections. When a client connects, the server sends a list of available files and then allows the client to request a file by index. The server sends the requested file's contents over the socket connection.

The client connects to the server socket and receives the list of available files. It displays this in a Tkinter GUI listbox. The user can select a file to download, which will trigger the client to request that file from the server and save it locally. The client also has an upload tab, which is unimplemented.

## Running

To start the server:

```
python server.py
``` 

To run the client:

```
python client.py
```

The client will connect to localhost:8800 by default.

## Implementation

### Server

- Sets up a listening TCP socket on port 8800
- Builds a list of available files by walking the `src/assets` folder 
- Sends file list when client connects
- Receives file index from client and sends back file contents
- Spawns a thread to handle each client connection

### Client

- Connects to server socket 
- Receives file list and populates GUI listbox
- Allows selecting file to download via listbox
- Requests file from server by index and saves to local disk
- Displays download progress with Tkinter progressbar
- Has unimplemented upload tab

## Next Steps

Some potential improvements:

- Implement file upload functionality
- Improve threading and concurrency
- Add option to select download location
- Integrate with an existing GUI framework like Tkinter
- Add authentication between client and server
- Implement network optimizations like compression
