class Quick_Union():
    '''
    Use Quick_Union method to connect and find connection between objects
    When initialize give size if the objects.
    '''
    
    def __init__(self, size):
        '''
        Initialize the objects
        '''
        self.size = size
        self.array = []
        for i in range(size):
            self.array.append(i)
            
    def root(self, obj):
        '''
        Give one object as parameter, returns the root of that object
        '''
        while(self.array[obj] != obj):
            obj = self.array[obj]
        return obj
            
    
    def find(self, objA, objB):
        '''
        Give 2 object as parameter, returns True/False if they are connected
        '''
        return(self.root(self.array[objA]) == self.root(self.array[objB]))
    
    
    def union(self, objA, objB):
        '''
        Give 2 objects as parameter, connects these 2 objects
        '''
        m = self.root(self.array[objA])
        n = self.root(self.array[objB])
        self.array[m] = n
