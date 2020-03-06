## client code
import socket as s
class client:
    def __init__(self):
        ## create the client socket
        self.cs = s.socket(s.AF_INET, s.SOCK_STREAM)
        server_addr = ('localhost', 12345)
        ## connect to the running server we created
        self.cs.connect(server_addr)
        self.msg_elems = []
    def send_msg(self):
    """ A method to send user input to the server """
        msg = input('->')
        self.cs.send(msg.encode())
        self.msg_elems = msg.split()
    def start_chat(self):
    """ A method to send send messages to the server
    until the user types bye """
        while 'bye' not in self.msg_elems:
            self.send_msg()
        self.cs.close()

if __name__ == '__main__':
    cl = client()
    cl.start_chat()
