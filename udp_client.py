import socket

target_host = '0.0.0.0'
target_port = 9999

try:
    # create socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('Socket created successfully')
except socket.error as err:
    print('socket creation failed with error: ', err)

# send giberish data
client.sendto(b'AAABBBCCC', (target_host, target_port))

data, addr = client.recvfrom(4096)

print(data)