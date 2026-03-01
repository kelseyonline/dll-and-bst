# Import the Node() class
from node import Node 

# Make the DLL() class
# I modeled this after my Queue from the other assignment
class DLL: 
    def __init__(self): 
        self.head = None 

    # is_empty method
    def is_empty(self): 
        if self.head == None: 
            return True
        else:
            return False
        
    # insert at front 
    def insf(self, data): 
        new_node = Node(data)

        # Makes sure this also counts as head
        if self.is_empty():
            # No extra work needed 
            self.head = new_node
        else:
            new_node.next = self.head 
            self.head.prev = new_node
            self.head = new_node

    # insert at end 
    def inse(self, data): 
        new_node = Node(data)

        if self.is_empty():
            # No extra work needed 
            self.head = new_node
        else: 
            current_node = self.head
            while current_node.next is not None: 
                current_node = current_node.next 
            new_node.prev = current_node 
            current_node.next = new_node 
            
    # insert in middle 
    def insm(self, location, data):
        new_node = Node(data)

        if self.is_empty(): 
            # No extra work needed 
            self.head = new_node
        else: 
            current_node = self.head
            # Iterate through til you find the location
            while current_node.data is not location: 
                current_node = current_node.next  

            # Now hook up all of the pointers correctly 
            new_node.next = current_node.next 
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node 

    # delete an element 
    def delete(self, data): 
        if self.is_empty(): 
            # No extra work needed 
            return "Data not found"
        else: 
            current_node = self.head
            # Iterate through til you find the data
            while current_node.data is not data: 
                current_node = current_node.next

            # Reconfigure the pointers around the node in question
            current_node.prev.next = current_node.next 
            current_node.next.prev = current_node.prev

            # Cut off the node 
            current_node.next = current_node.prev = None


    # delete the front 
    def delf(self):
        if self.is_empty(): 
            # No extra work needed 
            return "List is empty"
        else: 
            current_node = self.head

            # Reset head to element #2
            self.head = current_node.next
            
            # Make next node's prev equal to None
            current_node.next.prev = None 

    # print the list 
    def print_list(self):
        if self.is_empty(): 
            return "List is empty"
        else: 
            current_node = self.head
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
            print("\n")
        
# Example 

def main():
    # Initialize the DLL
    dll = DLL()

    dll.inse(1)
    dll.inse(2)
    dll.inse(3)
    dll.print_list() # 1 2 3

    dll.insf(4)
    dll.print_list() # 4 1 2 3

    dll.insm(2, 5)
    dll.print_list() # 4 1 2 5 3

    dll.delete(5)
    dll.print_list() # 4 1 2 3

    dll.delf()
    dll.print_list() # 1 2 3

main()