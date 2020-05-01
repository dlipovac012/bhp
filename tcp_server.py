import socket
import threading

BIND_IP = '0.0.0.0'
BIND_PORT = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((BIND_IP, BIND_PORT))

server.listen(5)

print('[*] Listening on {ip}:{port}'.format(ip=BIND_IP, port=BIND_PORT))

def handle_client(client_socket):
    try:
        request = client_socket.recv(1024)
    except socket.error as err:
        print('There was an error receiving data: ', err)

    print('[*] Received {}'.format(request))
    
    try:
        client_socket.send(b'ACK!')
    except socket.error as err:
        print(err)

    client_socket.close()

while True:
    client, addr = server.accept()

    print('[*] Accepted connection from {ip}:{port}'.format(ip=addr[0], port=addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client, ))
    client_handler.start()
