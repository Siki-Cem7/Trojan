import socket


class Server():

    def __init__(self):

        self.host = "0.0.0.0"
        self.port = 42111

        self.victim = ""
        self.addres = ""

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    def listen(self):

        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        self.victim, self.addres = self.socket.accept()
        self.data = self.victim.recv(1024).decode("utf-8")











if __name__ == "__main__":
    server = Server()
    server.listen()
