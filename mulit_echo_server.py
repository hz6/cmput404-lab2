import socket
import time
from multiprocessing import Process

HOST, PORT, BFFR_SZ = ("", 8000, 2048)


def handle_multi_echo(connection, address):
    print("Connected by:", address)

    data = connection.recv(BFFR_SZ)
    connection.sendall(data)
    connection.shutdown()
    connection.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as skt:
        skt.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        skt.bind((HOST, PORT))
        skt.listen()
        while 1:
            connection, address = skt.accept()
            process = Process(target=handle_multi_echo,
                              args=(connection, address))
            process.daemon = True

            process.start()
            print("process started:", process)


if __name__ == "__main__":
    main()
