import socket, threading

HOST = input("Enter server's IP address: ")
PORT = 12345

username = input("Choose a username: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == "USER":
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("\033[31m An error occured! \033[0m")
            client.close()
            break

def write():
    while True:
        msg = f"{username}: {input('')}"
        client.send(msg.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()