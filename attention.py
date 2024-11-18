import numpy as np

class Node:
    def __init_(self):
        # the vector store a this node
        self.data = np.random.randn(20)

        # weights governing how this node interacts with other nodes
        self.wkey = np.random.randn(20,20)
        self.wquery = np.random.randn(20,20)
        self.wvalue = np.random.randn(20,20)

    def key(self):
        # what do i have?
        return self.wkey @ self.data
    
    def query(self):
        # what i am looking for?
        return self.wquery @ self.data
    
    def value(self):
        # what do i publicly reveal/broadcast to others?
        return self.wvalue @ self.data
    


