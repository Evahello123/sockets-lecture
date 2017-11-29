import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address
addr = input("Enter the target IP address: 192.17.96.7")
port = int(input("Enter the target port: 10000"))
server_address = (addr, port)

# Message to send
message = bytes(input("Enter your NetID: zihewu2"), "utf-8")

try:
    # Send data
    sent = sock.sendto(message, server_address)

    # Receive response
    data, server = sock.recvfrom(4096)
    print('received "%s"' % data)

finally:
    print('closing socket')
    sock.close()
