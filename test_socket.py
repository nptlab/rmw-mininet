import socket
import sys

# Create a TCP/IP socket
# Bind the socket to the port
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.56.1', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()