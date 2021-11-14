import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


IP_address = '192.168.8.110'
Port = 12347

server.bind((IP_address, Port))

server.listen(100)

list_of_clients = []

def clientthread(conn, addr):
    conn.send("Welcome to chatroom".encode("utf-8"))
    while True:
        try:
            message = conn.recv(2048)
            message = message.decode("utf-8")
            print(message)
            if message:
                print ("<" + addr[0] + "> " + message)
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except Exception as e:
            continue


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except Exception as e:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    print("Accepting connections")
    conn, addr = server.accept()
    list_of_clients.append(conn)

    print (addr[0] + " connected")
    t = threading.Thread(target=clientthread, args=(conn,addr))
    t.start()
    t.join()

conn.close()
server.close()
