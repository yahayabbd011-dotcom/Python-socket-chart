import socket

SERVER_IP = '127.0.0.1'  # Canza zuwa IP din server
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
print(f"[+] Connected to server {SERVER_IP}:{PORT}")

while True:
    try:
        msg = input("You: ")
        client_socket.send(msg.encode())
        
        reply = client_socket.recv(1024).decode()
        if not reply:
            break
        print(f"Server: {reply}")
    except:
        break

client_socket.close()
print("[-] Disconnected")
