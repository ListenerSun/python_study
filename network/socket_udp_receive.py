import socket


# udp 服务端
def udp_server():
    while True:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = ("", 8000)
        udp_socket.bind(ip)
        data = udp_socket.recvfrom(1024)
        print(data[0].decode("utf-8"))
        udp_socket.close()


if __name__ == "__main__":
    # udp_server()
    pass