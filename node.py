# Make the Node() class

# When you create the node, you add in the data 
# supplied by the user as well as the 'next' attribute
# which points to the next node
class Node: 
    def __init__(self, data): 
        self.data = data
        # Set to None originally
        self.next = None
        self.prev = None