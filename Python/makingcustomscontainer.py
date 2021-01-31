class TagCould:
    # constructor
    def __init__(self):
        # intiallize tag attribute to empty dictionary 
        self.tags = {}
    #if we have this  tag in our   dictionary, if we don't have we set to 1 and if we have increment1
    def add(self, tag):
        #get(tag,0)+1 => to get item by the this key tag and supply default value we don't have that,+1 is increment by 1
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1 

    def __getitem__self(self, tag):
        return self.tags.get(tag.lower(),0)
    
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)
    #iterate 
    def __iter__(self):
        # iter is built in fuction to get iterated object,self.tags =>what we want to iterate
        return iter(self.tags)


cloud = TagCould()
cloud["python"] = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags )
