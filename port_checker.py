import socket

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))  # OS assigns a free port
        return s.getsockname()[1]

print(f"Free port found: {find_free_port()}")
