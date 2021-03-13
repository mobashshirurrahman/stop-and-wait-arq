import socket  # Importing socket library of python by which we connect server and client

c = socket.socket()   # creating socket object for receiver
print("Receiver  created")

c.connect(('localhost',8998))   # connecting to server on port number 8998

rec_message = "starting msg"
while True:
    received_message = c.recv(1024).decode()

    print(received_message, "  is received")
    if received_message != rec_message:
        ack = input("enter ack for received frame: ")
        c.send(bytes(ack, 'utf-8'))


