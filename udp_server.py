import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a local address and port
server_socket.bind(("localhost", 5566))

# Receive data from the client in a loop
count = 0
while True:
    data, client_address = server_socket.recvfrom(1024)
    if not data:
        # If the data is not received, break out of the loop
        break
    count += 1

# Close the server socket
server_socket.close()
print("Received {} messages".format(count))
print("hi")
