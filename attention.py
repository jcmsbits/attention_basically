import numpy as np

class Node:
    def __init__(self):
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
    

class Graph:
    
    def __init__(self):
        # make 10 nodes
        self.nodes = [Node() for _ in range(10)]
        print("Todos los nodos", self.nodes)
        # make 40 edges
        randi = lambda: np.random.randint(len(self.nodes))
        self.edges = [[randi(), randi()] for _ in range(40)]
        print("Self edges", self.edges)


    def run(self):
        updates = []
        for i, n in enumerate(self.nodes):
            print("Nodo #:", i)
            print("Token #:", n.data)
            # what is this node looking for?
            q = n.query()


            # find all edges that are input to this node
            inputs = [self.nodes[ifrom] for (ifrom, ito) in self.edges if ito==i]
            print("All edges", inputs)
            if len(inputs) == 0:
                continue # ignore

            # gather their keys, i.e. what they hold
            keys = [m.key() for m in inputs]
            print("Keys", keys)
            # calculate the compatibilities
            scores = [k.dot(q) for k in keys]
            print("Scores: ", scores)
            # softmax them so they sum to 1
            scores = np.exp(scores)
            scores = scores / np.sum(scores)
            print("Scores Softmax: ", scores)
            # gather the appropriate values with a weigthed sum
            values = [m.value() for m in inputs]
            print("Values: ", values)
            update = sum([s * v for s,v in zip(scores, values)])
            print("Sum update:")
            updates.append(update)
        
        for n, u in zip(self.nodes,updates):
            n.data = n.data + u # residual connection


grafo = Graph()
grafo.run()