import socket   
import json     

# API configuration
HOST = 'worldtimeapi.org'          # Target hostname
PORT = 80                          # Plain HTTP
PATH = '/api/timezone/Asia/Seoul'  # Endpoint path

request_text = (
    f"GET {PATH} HTTP/1.1\r\n"
    f"Host: {HOST}\r\n"
    f"User-Agent: Foundations of Python Network Programming\r\n"
    f"Connection: close\r\n"
    f"\r\n"
)

# TODO: Write the code from here.
def request():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.sendall(request_text.encode('ascii'))

    response = b""
    while True:
        data = sock.recv(4096)
        if not data:
            break
        response += data
    
    sock.close()

    parts = response.split(b"\r\n\r\n", 1)
    body = json.loads(parts[1].decode("utf-8"))

    print(f"datetime   = {body.get('datetime')}")
    print(f"timezone   = {body.get('timezone')}")
    print(f"utc_offset = {body.get('utc_offset')}")

request()


# ----------------------------------------------------------
# TODO: Verify your output matches the following format:
#
#   datetime   = 2026-04-03T18:30:45.123456+09:00
#   timezone   = Asia/Seoul
#   utc_offset = +09:00
# ----------------------------------------------------------
