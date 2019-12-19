import socket

class Client:
    
    def __init__(self, host_ip, port):
        self.host_ip = host_ip
        self.port = port

    def send(self):        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host_ip, self.port))
            s.sendall(b'Hello, world')
            data = s.recv(1024)

        print('Received', repr(data))

cl = Client('127.0.0.1', 2137)
cl.send()