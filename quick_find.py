class Quick_Find():
    '''
    Use Quick_Find method to connect and find connection between objects
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
    
    
    def find(self, objA, objB):
        '''
        Give 2 object as parameter, returns True/False if they are connected
        '''
        return self.array[objA] == self.array[objB]
    
    def union(self, objA, objB):
        '''
        Give 2 objects as parameter, connects these 2 objects
        '''
        m = self.array[objA]
        n = self.array[objB]
        for i in range(self.size):
            if(self.array[i] == m):
                self.array[i] = n