import socket

# Client configuration — must match server HOST and PORT
HOST         = '127.0.0.1'
PORT         = 9999
BUFFER_SIZE  = 1024
MAX_ATTEMPTS = 3   # Must match server's limit


def get_integer_answer(attempt: int) -> str:
    """
    TODO: Prompt the user for an integer answer and keep
    asking until valid numeric input is provided.
    Return the validated string.

    Args:
        attempt (int): Current attempt number for the prompt.

    Returns:
        str: Validated integer string to send to the server.
    """
    # ← implement input validation here
    
    while True:
        text = input(f"Attempt: {attempt}\n")

        try:
            int(text)
            return text
        except ValueError:
            print("Invalid value. input int")

# TODO: Write the code from here.
def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except ConnectionError as e:
        sock.close()
        raise RuntimeError('I think the server is down') from e

    text = "start"
    sock.sendall(text.encode("ascii"))
    data = sock.recv(BUFFER_SIZE).decode("ascii")
    print(data)
    if "Error 400" in data:
        sock.close()
        exit()    

    attempt = 1
    while attempt <= MAX_ATTEMPTS:
        text = get_integer_answer(attempt)
        sock.sendall(text.encode("ascii"))

        resp = sock.recv(BUFFER_SIZE).decode("ascii")
        print(f"{resp}")

        if "Correct" in resp:
            sock.close()
            exit()
        elif "Incorrect" in resp:
            attempt += 1
        elif "Game Over" in resp:
            break  

    sock.close()

if __name__ == '__main__':
    client()