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

        if text.isdigit() and text != "":
            return text
        else:
            print("Invalid value. input int")

# TODO: Write the code from here.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

text = input("")
sock.sendall(text.encode("ascii"))
data = sock.recv(BUFFER_SIZE).decode("ascii")
print(data)
if "Error 400" in data:
    sock.close()
    exit()    

attempt = 0
while attempt < 3:
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

resp = sock.recv(BUFFER_SIZE).decode("ascii")
print(f"{resp}")

sock.close()