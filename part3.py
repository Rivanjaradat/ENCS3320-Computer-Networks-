from socket import *

serverPort = 7788
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    ip = addr[0]
    port = addr[1]
    print('Got connection from', "IP: " + ip + ", Port: " + str(port))
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)

    # Check the request path
    if sentence.startswith("GET /ar "):
    # Send the main_ar.html file
     connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
     connectionSocket.send('Content-Type: text/html \r\n'.encode())
     connectionSocket.send('\r\n'.encode())

     with open("main_ar.html", "rb") as f:
        
      connectionSocket.send(f.read())
    
    elif sentence.startswith("GET / ") or sentence.startswith("GET /en "):
        # Send the main_en.html file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("main_en.html", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /css/style.css "):
        # Send the style.css file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/css \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("style.css", "rb") as f:
            connectionSocket.send(f.read())


    elif sentence.startswith("GET /rivan.html") :
        # Send the rivan.html file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("rivan.html", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /ahmad.html") :
        # Send the rivan.html file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("ahmad.html", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /rania.html") :
        # Send the rivan.html file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("rania.html", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /rivanar.html") :
        # Send the rivan.html file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("rivanar.html", "rb") as f:
            connectionSocket.send(f.read())

    elif sentence.startswith("GET /raniaar.html") :
        # Send the rivan.html file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("raniaar.html", "rb") as f:
            connectionSocket.send(f.read())
            
    elif sentence.startswith("GET /ahmadar.html") :
        # Send the rivan.html file
        connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("ahmadar.html", "rb") as f:
            connectionSocket.send(f.read())
            
    elif sentence.startswith("GET /bzu.png "):
    # Send the bzu.png file
     connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
     connectionSocket.send('Content-Type: image/png \r\n'.encode())
     connectionSocket.send('\r\n'.encode())
     with open("bzu.png", "rb") as f:
        connectionSocket.send(f.read())

    elif sentence.startswith("GET /comm.png "):
    # Send the bzu.png file
     connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
     connectionSocket.send('Content-Type: image/png \r\n'.encode())
     connectionSocket.send('\r\n'.encode())
     with open("comm.png", "rb") as f:
        connectionSocket.send(f.read())

    elif sentence.startswith("GET /rivan.jpg"):
    # Send the bzu.png file
     connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
     connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
     connectionSocket.send('\r\n'.encode())
     with open("rivan.jpg", "rb") as f:
        connectionSocket.send(f.read())

    elif sentence.startswith("GET /rania.jpg"):
    # Send the bzu.png file
     connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
     connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
     connectionSocket.send('\r\n'.encode())
     with open("rania.jpg", "rb") as f:
        connectionSocket.send(f.read())

    elif sentence.startswith("GET /ahmad.jpg"):
    # Send the bzu.png file
     connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
     connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
     connectionSocket.send('\r\n'.encode())
     with open("ahmad.jpg", "rb") as f:
        connectionSocket.send(f.read())
        
    elif sentence.startswith("GET /2.jpg"):
    # Send the bzu.png file
     connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
     connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
     connectionSocket.send('\r\n'.encode())
     with open("2.jpg", "rb") as f:
        connectionSocket.send(f.read())

    elif sentence.startswith("GET /com.png"):
    # Send the bzu.png file
     connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
     connectionSocket.send('Content-Type: image/png \r\n'.encode())
     connectionSocket.send('\r\n'.encode())
     with open("com.png", "rb") as f:
        connectionSocket.send(f.read())     
	   
    elif sentence.startswith("GET /1.jpg"):
    # Send the comm.png file
     connectionSocket.send("HTTP/1.1 200 OK\r\n".encode())
     connectionSocket.send('Content-Type: image/jpg \r\n'.encode())
     connectionSocket.send('\r\n'.encode())
     with open("1.jpg ", "rb") as f:
        connectionSocket.send(f.read())

    elif sentence.startswith("GET /go "):
        # Redirect to Google
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://google.com\r\n".encode())
        connectionSocket.send('\r\n'.encode())

    elif sentence.startswith("GET /so "):
        # Redirect to Stack Overflow
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://stackoverflow.com\r\n".encode())
        connectionSocket.send('\r\n'.encode())

    elif sentence.startswith("GET /bzu "):
        # Redirect to Birzeit University
        connectionSocket.send("HTTP/1.1 307 Temporary Redirect\r\n".encode())
        connectionSocket.send("Location: https://www.birzeit.edu \r\n".encode())

    else:
        # Send a 404 Not Found response
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send('Content-Type: text/html \r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        connectionSocket.send('\r\n'.encode())
        with open("error.html", "rb") as f:
            connectionSocket.send(f.read())


    # Close the connection
    connectionSocket.close()