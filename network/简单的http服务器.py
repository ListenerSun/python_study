import socket


def service_client(new_socke):
    """为客户端返回数据"""
#     1. 接收浏览器发送过来的请求, 即 http 请求
#     GET / HTTP/1.1
    request = new_socke.recv(1024)
    print(request)
    # 2. 返回http格式数据 给浏览器
    # 2.1 设置浏览器 header
    response = "HTTP/1.1 200 0k\r\n"
    response += "\r\n"
    # 2.2 返回数据
    response += "<font color=red>Hello Listener</font>"
    new_socke.send(response.encode("utf-8"))

def main():
    """整体流程"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 绑定
    tcp_server_socket.bind(("localhost", 8888))
    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
#     4. 等待客户端的链接
    new_socke, client_addr = tcp_server_socket.accept()
    print("连接的new_socket:", new_socke)
    print("连接的client_addr:", client_addr)
#     5. 为该客户端服务
    service_client(new_socke)


if __name__ == '__main__':
    main()