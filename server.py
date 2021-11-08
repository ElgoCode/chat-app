# socket is built in library for connecting two nodes on a network to communicate with each other
import socket
from threading import Thread


# global varibales
Clients = []


# server 
server = socket.socket()
HOST = "127.0.0.1"
PORT = 5646
ADDRESS = (HOST,PORT)
server.bind(ADDRESS)
server.listen(3)

# functions 
def send(msg):
    """"
    sending the msg for all clients including the client that sent the msg
    """
    for client in Clients:
        client.send(msg)
def broadcast(msg,theClientThatSendMsg):
    """"
    sending the msg for all clients except the client that sent the msg
    """
    for client in Clients:
        if client == theClientThatSendMsg:
            continue
        client.send(msg)
def recv(client):
    while True:
        try:
            # msg in bytes
            msg = client.recv(1024)
            broadcast(msg,client)
        except :
            print("client exit the chat")
            broadcast("someone left the chat".encode(),client)
            removeClient(client)
            break


def removeClient(client):
    for index,clientToRemove in enumerate(Clients):
        if client == clientToRemove:
            client.close()
            del Clients[index]
            break



print("waiting for connections...")

# main thread listining to connections
while True:
    try:
        client,addr = server.accept()
        print("someone conect to the server")
        # add the new connected client to Clients list
        Clients.append(client)
        newThread = Thread(target=recv,args=(client,))
        newThread.daemon = True
        newThread.start()
    except:
        print("\nclosing the server...")
        server.close()
        quit()



















