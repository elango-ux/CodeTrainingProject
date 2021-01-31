class TagCould:
    def __init__(self):
       #__tag ={} private member
        self.__tags = {}
    
    def add(self, tag):
        self.tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1 

    def __getitem__self(self, tag):
        return self.__tags.get(tag.lower(),0)
    
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    def __iter__(self):
        return iter(self.__tags)


cloud = TagCould()
print(cloud.__dict__)
# print(cloud.__tags)
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
# print(cloud.__tags["PYHON"])
