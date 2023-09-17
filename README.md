# Share-Media Client-Server

This is a simple client-server application for transferring files over a socket connection.

## Client

The client code is in `client.py`. 

It does the following:

- Creates a socket and connects to the server
- Receives a list of available files from the server
- Prints the list of files and prompts the user to choose a file
- Sends the index of the chosen file to the server
- Receives the file name from the server
- Receives the file contents in chunks of 1024 bytes and writes them to a file
- Closes the socket
- Gives option to download another file or exit

## Server 

The server code is in `server.py`.

It does the following:

- Creates a socket and binds it to a port
- Gets a list of files in the `src/assets` folder
- Accepts a connection from a client
- Sends the list of file names concatenated with '-' to the client 
- Receives the index of the file chosen by the client
- Sends the file name to the client
- Opens the file and sends 1024 byte chunks of the data to the client
- Closes the connection when file transfer is complete
- Continues listening for new connections

This allows the client to download any file from the server's `src/assets` folder by index. The files are streamed chunk-by-chunk for efficiency.

## Usage

Run the server code first:

```
python server.py
``` 

Then run the client code:

```
python client.py
```

The client will receive the list of files, prompt for input, and download the chosen file.
# karyar-python-projects-template

Hello dear students and welcome.
To create your project, just simply [use this template](https://github.com/new?template_name=karyar-python-projects-template&template_owner=shywn-mrk).


# Installation

To Start developing using this template you need to follow these steps:

1 - Create a virtual environment:

```bash
python -m venv env
```

2 - Activate the virtual environment:

- Windows:

```bash
env/Scripts/activate
```

- Mac/Linux:

```bash
source env/bin/activate
```

3 - Install the required packages:

```bash
pip install -r requirements.txt
```

4 - Install pre-commit to your `.git/hooks/`:
```bash
pre-commit install
```

Also make sure you autoupdate pre-commit if you faced any issues:
```bash
pre-commit autoupdate
```


5 - Start developing your project and we wish you the best ;)


# Commiting
You may have noticed we are using pre-commit that checks many things
and lowers the risks of implementing disasters.
pre-commit checks before you commit your changes
and if anything goes wrong, you cannot commit.
Fix the errors and try to commit again and you're good to go.
If you want to run pre-commit without commiting you can run:
```bash
pre-commit run -a
```
