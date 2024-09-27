""" Implement a simple web server
    - supports GET requests from the /static folder
"""

import socket

# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.settimeout(30)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    # Wait for client connections
    try:
        client_connection, client_address = server_socket.accept()
    except:
        #this triggers at an interval equal to socket.settimeout
        #is this correct? We can't return the eeror code to the client since it *is not connected*
        # response = 'HTTP/1.0 408 Request Timeout\n\n'
        # statuscode = "408"
        # file_out = open("WEBLOG.txt", "a")
        # file_out.write(statuscode + "\n")
        # file_out.close()
        print('Timeout Exception on socket.accept()')
        continue

    # Get the client request
    request = client_connection.recv(1024).decode()
    #print(request)

    #pull apart the request
    req_headers = request.split('\n')
    firstheader = req_headers[0].split()
    print(firstheader)
    #for some reason this randomly triggers, so if we get an empty request, we should just ignore it
    if (len(firstheader) == 0):
        continue
    
    #get the http method and the name of the file requested
    req_method = firstheader[0]
    if (req_method == 'GET'):
        req_name = firstheader[1]

    # Send HTTP response
    try:
        filed = open('./static' + req_name)
        content = filed.read()
        filed.close()
        response = 'HTTP/1.0 200 OK\n\n' + content
        statuscode = "200"
    except socket.timeout:
        response = 'HTTP/1.0 408 Request Timeout\n\n'
        statuscode = "408"
    except:
        filed = open('./static/404.html')
        content = filed.read()
        filed.close()
        response = 'HTTP/1.0 404 NOT FOUND\n\n' + content
        statuscode = "404"

    #write to log
    file_out = open("WEBLOG.txt", "a")
    file_out.write(req_method + " " + req_name + " " + statuscode + "\n")
    file_out.close()

    client_connection.sendall(response.encode())
    client_connection.close()

# Close socket
server_socket.close()