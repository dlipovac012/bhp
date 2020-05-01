import socket
import sys

target_host = '0.0.0.0'
target_port = 9999

try:
    # create socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created successfully')
except socket.error as err:
    print('socket creation failed with error: ', err)

try:
    # resolve IP
    host_ip = socket.gethostbyname(target_host)
except socket.gaierror:
    print('There was an error resolving a host')
    sys.exit()

# connect client
client.connect((host_ip, target_port))
# send giberish data
client.send(b"GET / HTTP/1.1\r\nHost: 0.0.0.0\r\n\r\n")

response = client.recv(4096)

print(response)