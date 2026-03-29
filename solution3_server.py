import socket
import random

# Server configuration
HOST         = '127.0.0.1'
PORT         = 9999
BUFFER_SIZE  = 1024
MAX_ATTEMPTS = 3


def play_game(conn: socket.socket, addr: tuple) -> None:
    """
    TODO: Implement one full Math Quiz session.

    Args:
        conn: Accepted TCP client socket.
        addr: Client's (host, port).
    """
    # ← implement play_game here
    while True:
        start_str = conn.recv(BUFFER_SIZE).decode("ascii")
        if start_str != "start":
            text = "Error 400: Bad Request. Send 'start' to play."
            conn.sendall(text.encode("ascii"))
            return
        else:
            break

    x, y = random.randint(1, 20), random.randint(1, 20)
    text = f"What is {x} + {y}?"
    conn.sendall(text.encode("ascii"))
    count = 0
    while True:
        ans = conn.recv(BUFFER_SIZE).decode("ascii")

        if not ans.isdigit():
            text = f"non-numeric input!"
            conn.sendall(text.encode("ascii"))
            break

        if int(ans) == x + y:
            text = f"Correct! You win."
            conn.sendall(text.encode("ascii"))
            break
        else:
            count += 1
            if count >= 3:
                text = f"Game Over. Out of attempts. The correct answer was [{x + y}]."
                conn.sendall(text.encode("ascii"))
                break

            text = f"Incorrect. Try again!"
            conn.sendall(text.encode("ascii"))
            continue


# TODO: Write the code from here.
def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen()

    while True:
        sc, addr = sock.accept()
        play_game(sc, addr)
        sc.close()

if __name__ == '__main__':
    server()