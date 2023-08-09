from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.open = False

    def open(self):
        if self.open:
            raise InvalidOperationError("Stream is already opened")
        
    def close(self):
        if self.close:
            raise InvalidOperationError("Stream is already closed")
        self.open = False
    
    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory")

stream = MemoryStream()
stream.read()