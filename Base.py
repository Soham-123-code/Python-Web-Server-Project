""""
    This project attempts to create a simple HTTP web server
"""

import socket

#Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

#Create Socket 

#Create server_socket variable and set it to AF_INET
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
server_socket.bind((SERVER_HOST,SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s..... ' % SERVER_PORT)

while True:
    #Wait for client connection
    client_connection, client_address = server_socket.accept()

    #GET the client request
    request = client_connection.recv(1024).decode()
    print(request)

    #parse HTTP headers 
    headers = request.split('\n')
    filename = headers[0].split()[1]

    #Get the contents of the file
    if filename == '/favicon.ico':
        filename = '/index.html'

    if filename == '/':
        filename= '/index.html'

    try:
        fin = open('htdocs/' + filename)
        content = fin.read()
        fin.close()

        response = 'HTTP/1.0 200OK\n\n' + content
    except FileNotFoundError:

        response = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    #Send HTTP Response
    response = 'HTTP/1.0 200OK\n\n' + content
    client_connection.sendall(response.encode())
    client_connection.close()

#close scoket
server_socket.close()