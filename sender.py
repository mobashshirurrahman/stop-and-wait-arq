# Importing socket library of python by which we connect server and client
import socket

# creating socket object
s = socket.socket()
print("Sender  created")  # printing after connection creation

s.bind(('localhost', 8998))  # binding socket object with ip adress and port number
s.listen(3)  # listenting to the client maximum 3 client allowed here as 3 is passed

print("waiting for connection")  # waiting for the connection
# s.settimeout(15.0)
c, addr = s.accept()  # it will accept the connection and return client socket and adress
print("connected with ", addr)
ack_expected = "1"  # expected frame number
ack = "0"

while True:  # this while loop will iterate until user want to stay for connection

    frame = input("enter frame to send: ")  # enter frame to send

    c.send(bytes(frame, 'utf-8'))  # now sent frame to client as byte stream
    while ack_expected != ack:  # until we can not get expected acknowledgement number
                                # from reeceiver we will resend frame

        # now we will put try and catch block to handle exception caused by settimeout() function
        try:
            c.settimeout(12.0)    # timeout duration of 12 second
            ack = c.recv(1024).decode()     # received acknowledgement from receiver

            while ack_expected != ack:     # if ack expected doesnt match with received one then resend frame
                print(frame, " frame is resent !")
                c.send(bytes(frame, 'utf-8'))
                ack = c.recv(1024).decode()
                print(ack)
        except socket.timeout:   # in case of time out again resend the frame

            while ack_expected != ack:
                print(frame, " frame is resend after timeout of 12 sec !!")
                break

    # asking user if wants to close the connection
    stop_connection = input("wants to stop connection type: 'yes' to exit ")
    if stop_connection == "yes":
        print("connection closed")
        c.close()    # to close connection
        break
    # changing expected ack value accordingly
    if ack_expected == "0":
        ack_expected = "1"
    else:
        ack_expected = "0"
