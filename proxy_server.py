import socket
import time
import sys

from urlextract import URLExtract

HOST, PORT, BFFR_SZ = ("", 8001, 2048)


def get_remote_ip(host):

    try:
        print(f'Getting IP for {host}')
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    print(f'Ip address of {host} is {remote_ip}')
    return remote_ip


def main():
    port = 80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_start:
        print("proxy server started")
        s_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s_start.bind((HOST, PORT))
        s_start.listen(1)
        while True:
            connection, address = s_start.accept()
            print("Connected by:", address)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_end:
                send_data = connection.recv(BFFR_SZ)
                host = send_data.decode()
                print("Connecting to ", host)

                remote_ip = get_remote_ip(host)
                s_end.connect((remote_ip, port))

                print(f"sending receive data from {send_data} to {host}")
                s_end.sendall(send_data)
                s_end.shutdown(socket.SHUT_WR)

                data = s_end.recv(BFFR_SZ)
                print(f"sending received data from {data} to client")
                connection.send(data)

            connection.close()


if __name__ == "__main__":
    main()
