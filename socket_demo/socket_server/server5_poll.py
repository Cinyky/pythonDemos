import socket_demo,select

s= socket_demo.socket()

host = socket_demo.gethostname()
port = 1111

s.bind((host,port))

fdmap = {s.fileno():s}

s.listen(5)
p = select.poll()
p.register(s)

while True:
    events = p.poll()
    for fd,event in events:
        if fd in fdmap:
            c,addr = s.accept()
            print 'Got connection from', addr
            p.register(c)
            fdmap[c.fileno] = c
        elif event & select.POLLIN:
            data = fdmap[fd].getpeername().recv(1024)
            if not data:
                print fdmap[fd].getpeername(),'disconnected'
                p.unregister(fd)
                del fdmap[fd]
            else:
                print data

