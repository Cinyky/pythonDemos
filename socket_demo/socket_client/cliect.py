import socket_demo

s = socket_demo.socket()

host = socket_demo.gethostname()
port = 1111

s.connect((host,port))
while 1:
    print 'enter something:',
    ent = raw_input()
    if ent == '':
        break
    s.send(ent)
    # data = s.recv(1024)
    # print 'echo=>', data
