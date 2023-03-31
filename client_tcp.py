# Import the socket module
from socket import *

# Import the time module for tracking elapsed time
import time

# Set the server name and port number
serverName = 'localhost'
serverPort = 5566

# Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# Connect the socket to the server
clientSocket.connect((serverName, serverPort))

# Initialize the message counter and start time
c = 0
start_time = time.time()

# Send 1000000 messages to the server
for i in range(1, 1000001):
    # Send the current message to the server, encoded as a string
    clientSocket.send(str(i).encode())
    print("Client send " + str(i) + " to server ")

# Calculate the elapsed time
elapsed_time = time.time() - start_time

# Print the total number of sent messages and elapsed time
print("Client send " + str(i) + " to server " + str(elapsed_time) + " seconds")

# Close the socket
clientSocket.close()