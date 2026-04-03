import socket 

# Client configuration — must match server HOST and PORT
HOST        = '127.0.0.1'   # Server address
PORT        = 12345          # Server UDP port
BUFFER_SIZE = 1024           # Max datagram size
TIMEOUT_SEC = 5.0            # Seconds to wait for reply


# TODO: Write the code from here.
def client():
    data = input("Client sends : ")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(data.encode("ascii"), (HOST, PORT))
    sock.settimeout(TIMEOUT_SEC)

    try:
        data, _ = sock.recvfrom(BUFFER_SIZE)  
        response = data.decode('ascii')
        print(f'Server reply : {response}')
    except socket.timeout as e:
        print("I think the server is down")
    finally:
        sock.close()

if __name__ == '__main__':
    client()