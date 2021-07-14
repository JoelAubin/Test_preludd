class Node(object):
    # You may have to define members of this class

    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.succeeding= succeeding
        self.previous = previous
        
        
        
        


class LinkedList(list):
    # You may have to define members of this class

    def __init__(self):
        self.first = None
        self.last = None
        
    def __iter__(self):
        return (self.get_values(x) for x in list.__iter__(self))
    
    def get_values(self,x):
        return x.value
    
    
    def push(self, value):
        No = Node(value, previous = self.last)
        if len(self)!=0:
            self[-1].succeeding = id(No)
        self.append(No)
        self.last = id(No)
    
    def pop(self):
        value = self[-1].value
        if len(self)>1:
            self[-2].succeeding = None
            self.last = id(self[-1])
        self.remove(self[-1])
        return value
    
    def shift(self):
        value = self[0].value
        if len(self)>2:
            self[1].previous = None
            self.first = id(self[0])
        self.remove(self[0])
        return value
    
    def unshift(self,value):
        No = Node(value, succeeding = self.first)
        if len(self)!=0:
            self[0].previous = id (No)
        self.insert(0, No)
        self.first = id(No)
        
    

# lst = LinkedList()


# lst.unshift(20)