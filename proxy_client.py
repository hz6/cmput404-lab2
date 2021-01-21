import socket

HOST, PORT, BFFR_SZ = ("localhost", 8001, 2048)


def connect(address):
    payload = "www.google.com"
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
    except Exception as exception:
        print(exception)
    finally:
        print("close socket")
        s.close()


def main():
    connect(('127.0.0.1', PORT))


if __name__ == "__main__":
    main()
