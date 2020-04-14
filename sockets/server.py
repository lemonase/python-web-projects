import sys
import socket

HOST, PORT = socket.gethostname(), 1111

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket with an ip (or hostname) and a port number
s.bind((HOST, PORT))

# listen for 1kb
s.listen(1024)

# run forever accepting connections
while True:
    # returns a socket object, and an address
    rs, address = s.accept()

    # get the message
    recv_msg = rs.recv(100).decode()

    # log it and create a message
    print(f"Connection from {address}!")
    print(f"They say: {recv_msg}")

    # close socket if the message is quit
    if recv_msg == "quit" or recv_msg == "exit":
        rs.close()
        sys.exit(0)
