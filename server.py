import socket as s
def server():
    ## create the server socket
    ss = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_addr = ('localhost', 12345)
    try:
        ## bind the socket to an IP and port
        ss.bind(server_addr)
        ## start listening on that socket
        ss.listen(1)
        ## accept incoming requests
        conxn, addr = ss.accept()
        print("Accepted connection from: " + str(addr))
        while True:
            ## receive data from the client
            data = conxn.recv(1024).decode()
            if data:
                print("This is what the client sent: " + str(data))
    except:
        conxn.close()

if __name__ == '__main__':
    server()
