#coding=utf-8

#import modules
from asyncore import dispatcher
from asynchat import async_chat
import socket_demo,asyncore

PORT = 5005
NAME = 'TestChat'

#chat session
class ChatSession(async_chat):
    '''
    处理服务器和一个用户之间的类。
    '''
    def __init__(self,server,sock):
        #标准设置任务。
        async_chat.__init__(self,sock)
        self.server = server
        self.set_terminator("\r\n")
        self.data = []

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        '''
        如果发现一个终止对象，也就意味着杜入了一个完整的行，将其广播给每一个人。
       '''
        line =''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

#chat server
class ChatServer(dispatcher):
    '''
    接受链接并且产生会话的类，它还会处理到其他会话的广播。
    '''
    def __init__(self,port,name):
        #standard setup tasks
        dispatcher.__init__(self)
        self.create_socket(socket_demo.AF_INET, socket_demo.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.name = name
        self.sessions = []

    def disconnect(self,session):
        self.sessions.remove(session)

    def broadcast(self,line):
        for session in self.sessions:
            session.push(line+'\r\n')

    def handle_accept(self):
        conn,addr = self.accept()
        self.sessions.append(ChatSession(self,conn))

if __name__ == '__main__':
    s = ChatServer(PORT,NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print 'end server'