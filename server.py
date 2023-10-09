import socket

# Create Socket
host = "0.0.0.0"  # Bind to all available network interfaces
port = 12345  # Use a port number of your choice
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket object
s.bind((host, port))
s.listen(5)

# Accept Client Connection
print("Waiting for client...")
conn, addr = s.accept()  # Accept connection when a client connects
print("Connected by " + addr[0])

# Print Client Data
while True:
    data = conn.recv(1024)  # Receive client data
    if not data:
        break
    print(data.decode('utf-8'))

conn.close()  # Close the connection when done
