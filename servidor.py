import socket

HOST = 'localhost'
PORT = 50000

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((HOST, PORT))
soc.listen()
print('Aguardando conexão de um cliente')
conn, ender = soc.accept()

print('Conectado em', ender)
while True:
    data = conn.recv(1024)
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data)