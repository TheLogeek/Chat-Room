import socket, threading

HOST = "127.0.0.1"
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients, usernames = [], []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f"{username} left the chat".encode('ascii'))
            usernames.remove(username)
            break

def receive():
    print("\033[32m Server running... \033[0m")
    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")

        client.send("USER".encode('ascii'))
        username = client.recv(1024).decode('ascii')
        usernames.append(username), clients.append(client)

        print(f"Client's username is {username}")
        broadcast(f"{username} joined the chat".encode('ascii'))
        client.send("Connected to the server".encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()