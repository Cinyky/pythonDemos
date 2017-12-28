#! /usr/env/bin python  
# codinf=utf-8
import socket_demo
import time


def Client():
    sock = socket_demo.socket(socket_demo.AF_INET, socket_demo.SOCK_STREAM)
    sock.connect((socket_demo.gethostname(), 1234))
    while 1:
        print 'enter something:',
        ent = raw_input()
        if ent == '':
            break
        sock.send(ent)
        time.sleep(1)
        data = sock.recv(1024)
        print 'echo=>', data
    sock.close()


if __name__ == '__main__':
    Client()