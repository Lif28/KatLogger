import socket
import os

def client():
    
    HOST = "127.0.0.1"
    PORT = 4683

    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind((HOST, PORT))
    client.listen(0)

    client_socket, client_address = client.accept()
    print(f"accepted connection from {client_address[0]}:{client_address[1]}")

    while True:

        req = client_socket.recv(1024)
        req = req.decode("utf-8") #convert

        if req.lower() == "close":
            client_socket.send("closed".encode("utf-8")) #send a message that close connection
            break


        print(f"recived: {req}")
        os.system(req)


        if req.lower() == "closed":
            break

    client.close()
    print("connection to server closed")


client()
