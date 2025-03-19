import socket

# Define the host and port to listen on
HOST, PORT = '127.0.0.1', 8080

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Allow immediate reuse of address after program exit
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Serving HTTP on {HOST} port {PORT} ...")

    while True:
        # Accept a new client connection
        client_connection, client_address = server_socket.accept()
        with client_connection:
            # Receive the request data (limit to 1024 bytes for simplicity)
            request_data = client_connection.recv(1024).decode('utf-8')
            print("Received request:")
            print(request_data)

            # Parse the request to get the path
            request_lines = request_data.splitlines()
            if len(request_lines) > 0:
                request_line = request_lines[0]
                # Split the request line into method, path, and protocol
                method, path, _ = request_line.split()

                # Handle the /about endpoint
                if path == '/about':
                    http_response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n"
                        "Content-Length: 100\r\n"
                        "\r\n"
                        "<html><body><h1>About Endpoint!</h1></body></html>"
                    )
                else:
                    # Default response for other paths
                    http_response = (
                        "HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n"
                        "Content-Length: 100\r\n"
                        "\r\n"
                        f"<html><body><h1>Path:{request_data}</h1></body></html>"
                    )

                # Send the HTTP response back to the client
                client_connection.sendall(http_response.encode('utf-8'))
