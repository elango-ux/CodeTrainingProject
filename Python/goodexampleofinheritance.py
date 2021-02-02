class Elango(Exception):
    pass  
  

class Stream:
    def __init__(self):
        self.opened = False
    
    def open(self):
        if self.opened:
            raise Elango("stream is  already opened") 
        
        self.opened = True
    def closed(self):
        if not self.opened:
            raise Elango("stream is  already closed") 
        
        self.opened = False

class FileStream(Stream):
    def  read(self):
        print("reading the data from network")