from abc import ABC,abstractmethod


class InvalidOperationError(exception):
      pass


class Stream(ABC):
    def __init__(self):
        self.opened = False
    
    def opened(self):
        if self.opened:
           self.opened = True
    def closed(self):
        if not self.opened:
            raise InvalidOperationError("stream is  already opeened") 
            
        
        self.opened = False
    # abstract method decorator
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def  read(self):
        print("reading the data from network")

class NetworkStream(Stream):
    def read(self):
        print("reading data from the stream")


stream = Stream()
stream.open()