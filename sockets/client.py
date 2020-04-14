import socket

HOST, PORT = socket.gethostname(), 1111

while True:
    print(f"Please enter a message to send to ({HOST, PORT})")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    user_input = input().encode()
    s.send(user_input)
    s.close()
