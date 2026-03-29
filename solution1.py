import socket   
import ssl
import json     

# API configuration
HOST = 'timeapi.io'
PORT = 443                                        
PATH = '/api/v1/timezone/zone?timeZone=Asia/Seoul'

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
    ssl_socket = ssl.wrap_socket(sock)
    ssl_socket.sendall(request_text.encode('ascii'))

    raw = b""
    while True:
        data = ssl_socket.recv(4096)
        if not data:
            break
        raw += data
    
    try:
        _, body = raw.split(b"\r\n\r\n", 1)
    except ValueError:
        print("invalid response")
        return
    
    body_json = body.decode("utf-8")

    try:
        start_idx = body_json.find('{')
        end_idx = body_json.rfind('}') + 1
        json_str = body_json[start_idx:end_idx]
        
        body = json.loads(json_str)

        print(f"local_time = {body.get('local_time')}")
        print(f"timezone   = {body.get('timezone')}")
        print(f"utc_time   = {body.get('utc_time')}")
    except (json.JSONDecodeError, ValueError) as e:
        raise RuntimeError('JSON parse err') from e
    finally:
        ssl_socket.close()
    

if __name__ == '__main__':
    request()

# ----------------------------------------------------------
# TODO: Verify your output matches the following format:
#
#   datetime   = 2026-04-03T18:30:45.123456+09:00
#   timezone   = Asia/Seoul
#   utc_offset = +09:00
# ----------------------------------------------------------