
# Import the socket module
from socket import *

# Import the time module for tracking elapsed time
import time

# Set the port number and server name
serverPort = 5566
servername = "localhost"

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the server name and port
serverSocket.bind((servername, serverPort))

# Set the socket to listen for incoming connections
serverSocket.listen(1)

# Print a message indicating that the server is ready to receive
print("The server is ready to receive")

# Initialize the count of received messages and start time
count = 0
start_time = time.time()

# Accept an incoming connection from a client
connection, clientAddress = serverSocket.accept()

# Initialize the message counter
i = 0

# Keep receiving messages until the message counter reaches 1000000
while i < 1000000:
    # Receive a message from the client in 1024-byte chunks and decode it
    message = connection.recv(1024)
    receivedMessage = message.decode()
    
    # Increment the message counter and the count of received messages
    i += 1
    count += 1

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Print the total number of received messages and elapsed time
print("Received " + str(count) + " packets in " + str(elapsed_time) + " seconds")

# Close the connection with the client
connection.close()

# Close the server socket
serverSocket.close()
