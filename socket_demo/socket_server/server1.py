import socket_demo

s = socket_demo.socket()

host = socket_demo.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)

while True:
    c,addr = s.accept()
    print 'Got connection from' , addr
    c.send('Thank you for listening')
    c.close()
    