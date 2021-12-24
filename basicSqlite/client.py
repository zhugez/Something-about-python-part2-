class Client:
    def __init__(self, ip: str, port: int) -> object:
        self.ip = ip
        self.port = port
    def __str__(self):
        return f"Client {self.ip} : {self.port}"