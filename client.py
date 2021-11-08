import socket
from threading import Thread


# client 
client = socket.socket()
HOST = "127.0.0.1"
PORT = 5646
ADDRESS = (HOST,PORT)
client.connect(ADDRESS)


# functions
def recv_msg():
    while True:
        try:
            msg = client.recv(1024)
            print("\n" + msg.decode())
            print("[ElgoCodeChat]>>")
        except:
            print("\nElgoCode $erver shutdowned!")
            client.close()
            break
    
recv_thread = Thread(target=recv_msg)
recv_thread.daemon = True
recv_thread.start()

while True:
    try:
        msg = input("[ElgoCodeChat]>>")
        client.send(msg.encode())
    except:
        print("\nclosing...")
        client.close()
        quit()










