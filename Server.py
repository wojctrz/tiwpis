import socket
from enum import Enum
import threading
import time

class Status(Enum):
    NOT_CONFIGURED = 0
    CONFIGURED = 1
    LISTENING = 2
    ERROR = 3

class Server:

    def __init__(self, host_ip, port):
        self._server_status = Status
        self._server_status = Status.NOT_CONFIGURED
        self.host_ip = host_ip
        self.port = port
        self._server_status = Status.CONFIGURED

    def __del__(self):
        self.server_sock.close()

    def _listen(self):
        while(True):
            if self._server_status != Status.LISTENING:
                break
            self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_sock.bind((self.host_ip, self.port))
            self.server_sock.listen()
            conn, addr = self.server_sock.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)

    def start(self):
        self._server_status = Status.LISTENING
        self._listening_thread = threading.Thread(target=self._listen)
        print('starting thr')
        self._listening_thread.start()

    def stop(self):
        self._server_status = Status.CONFIGURED
        print('stoping thr')
        self._listening_thread.join()

serv = Server('127.0.0.1', 2137)
serv.start()

time.sleep(60)

serv.stop()