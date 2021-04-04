import socket

CORRECT_LINE = b'Correct\n'
READY_LINE = b"Ready?\n"

sock = socket.socket()
sock.connect(("0.0.0.0", 25005))


while True:
    data = sock.recv(1024)
    if data.endswith(CORRECT_LINE) or data.endswith(READY_LINE):
        data = sock.recv(1024)
    else:
        sep = CORRECT_LINE
        if READY_LINE in data:
            sep = READY_LINE
        data = data[(data.index(sep) + len(sep)) if sep in data else 0:]
    try:
        a, b = [int(c) for c in data.decode("ascii").strip().split(", ")]
    except Exception:
        # it's exactly the flag
        print(data.decode())
        break
    sock.send(f"{a * b}".encode("ascii"))
