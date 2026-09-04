import socket

HOST = '0.0.0.0'  
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[+] Server is listening on {HOST}:{PORT}")
print("[+] Waiting for connection...")

conn, addr = server_socket.accept()
print(f"[+] Connected to {addr}")

while True:
    try:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print(f"Client: {msg}")
        
        reply = input("You: ")
        conn.send(reply.encode())
    except:
        break

conn.close()
server_socket.close()
print("[-] Connection closed")
