class Elango(Exception):
  
  
 

#stream 
class Stream:
    def __init__(self):
        self.opened = False
    
    def opened(self):
        if self.opened:
            raise Elango("stream is  already opeened") 
        
        self.opened = True
    def closed(self):
        if not self.opened:
            raise Elango("stream is  already closed") 
        
        self.opened = False

class FileStream(Stream):
    def  read(self):
        print("reading the data from network")