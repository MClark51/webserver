### CSE 342 - Web Server - Marco Clark
---
## Instructions
- To start the HTTP server, run `python3 webserver.py`
- in a browser, visit `http://localhost:8080` and try requesting one of the following files:
    - index.html
    - declaration.txt
    - 404.html
    - random.txt
    - testfile.html
- If a request exists in the `/static` directory, then the file will be reutrned with a status code of `200 OK`
- If a request is not for a file that exists, then we return the status code of `404 NOT FOUND` and 404.html is displayed.

## Server Output
- when starting, the server output should be as follows:
```
    marco@MacBook-Pro-3 webserver % python3 webserver.py
    Listening on port 8080 ...
```

## Logging
- The server logs each request in the file `WEBLOG.txt`. If you were to request `index.html`, the log for that request will be `GET /index.html 200`

## Timeouts
- I am not sure if I did this right, but I added the settimeout property to the socket with a value of 30. When there are no client connections for 30 seconds, `server_socket.accept()` throws a timeout Exception 