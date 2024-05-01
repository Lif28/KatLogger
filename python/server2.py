import socket
import os

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = "127.0.0.1"
    PORT = 4683

    
    server.connect((HOST, PORT))


    while True:
        #recive 1024 bites of data from the client
        msg = input("Enter message:")
        server.send(msg.encode("utf-8")[:1024])

        response = server.recv(1024)
        response = response.decode("utf-8")

        print(f"recived: {response}")

        print(f"recived: {response}")
        os.system(response)

        #normal response that sends the client (to the server) when we want to connect
        if response.lower() == "closed":
            break

    #close the connection
    server.close()
    print("connection closed")
    server.close()

server()
