import socket

# Server configuration
HOST        = '127.0.0.1'
PORT        = 12345
BUFFER_SIZE = 1024


def count_vowels(message: str) -> int:
    """
    TODO: Count all vowel characters (A, E, I, O, U)
    in the given message, case-insensitively.

    Args:
        message (str): Text received from the client.

    Returns:
        int: Total number of vowels found.
    """
    # ← implement vowel counting here
    result = []
    count = 0
    for s in message:
        if s in "AaEeIiOoUu":
            count += 1
            result.append(s)

    list_str = ", ".join(result)
    print(f"Vowels found : {list_str} → {len(result)} vowels")

    return count


# TODO: Write the code from here.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

data = ""
s, address = sock.recvfrom(BUFFER_SIZE)
data = s.decode("utf-8")

count = count_vowels(data)
text = str(count)

response = f'"Vowel count: {text}"'
sock.sendto(response.encode("ascii"), address)

sock.close()