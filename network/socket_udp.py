import  socket

# udp 客户端
def udp_client():
    # 创建一个 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        send_data = input("请输入要发送的内容:")
        # 发送套接字
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.0.107", 8000))
    udp_socket.close()

# tcp 客户端
def tcp_client():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        send_data = input("[Tcp]请输入要发送内容:")
        tcp_socket.listen(128)


if __name__ == "__main__":
    udp_client()