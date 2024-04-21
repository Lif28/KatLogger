import socket
import os

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    PORT = 46283

    server.bind((HOST, PORT))
    server.listen(0)
    print(f"Listening on {HOST}:{PORT}")

    client_socket, client_address = server.accept()
    print(f"accepted connectionHOST
HOST
HOST from {client_address[0]}:{client_address[1]}")

    while True:
        #recive 1024 bites of data from the client
        req = client_socket.recv(1024)
        req = req.decode("utf-8") #convert

        if req.lower() == "close":
            client_socket.send("closed".encode("utf-8")) #send a message that close connection
            break

        print(f"recived: {req}")
        os.system(req)

        #normal response that sends the client (to the server) when we want to connect
        response = "accepted".encode("utf-8")
        client_socket.send(response)

    #close the connection
    client_socket.close()
    print("connection closed")
    server.close()

server()
