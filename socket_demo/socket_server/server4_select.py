import socket_demo,select

s= socket_demo.socket()

host = socket_demo.gethostname()
port = 1111
s.bind((host,port))
s.listen(5)
inputs = [s]
while True:
    rs,ws,es = select.select(inputs,[],[])
    for r in rs:
        if r is s:
            c,addr = s.accept()
            print 'Got connection from' ,addr
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket_demo.error:
                disconnected = True

            if disconnected:
                print r.getpeername(),'disconnected'
                inputs.remove(r)
            else:
                print data

