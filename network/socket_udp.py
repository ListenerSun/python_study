import  socket

def main():
    # 创建一个 套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        send_data = input("请输入要发送的内容:")
        # 发送套接字
        udp_socket.sendto(send_data.encode("utf-8"), ("192.168.0.107", 8000))
    udp_socket.close()


if __name__ == "__main__":
    main()