import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the numbers from 0 to 1000,000 to the server
for i in range(1000000):
    client_socket.sendto(str(i).encode(), ("localhost", 5566))

# Close the socket
client_socket.close()
