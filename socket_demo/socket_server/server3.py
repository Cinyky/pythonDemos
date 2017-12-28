#! /usr/env/bin python
# coding=utf-8
import socket_demo


# Server
def Server():
    sock = socket_demo.socket(socket_demo.AF_INET, socket_demo.SOCK_STREAM)
    while 1:
        sock.bind(('localhost', 1236))
        sock.listen(5)  # 监听，最大链接数
        connection, address = sock.accept()  # 开始接受请求,进入等待阻塞状态，直到有链接到达
        print 'Got connection ',address
        while 1:
            data = connection.recv(1024)  # 接收客户端发过来的数据
            if not data:
                break
            print data, address
            connection.send(data)  # 发送数据到客户端，即上面到connection
        connection.close()
        sock.close()


if __name__ == '__main__':
    Server()