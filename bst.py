# Import tnode 
from tnode import Tnode 

# Create bst class 
class BST: 
    def __init__(self): 
        # Initialize the BST with no root yet 
        self.root = None

    # is_empty method 
    def is_empty(self): 
        if self.root == None: 
            return True
        else:
            return False
        
    # insert method 
    def insert(self, key): 
        new_tnode = Tnode(key)

        if self.is_empty(): 
            # If the tree is empty, make the new node the root
            self.root = new_tnode 
        else: 
            root_tnode = self.root 
            while True: 
                if new_tnode.key <= root_tnode.key: 
                    if root_tnode.lc == None: 
                        root_tnode.lc = new_tnode
                        break
                    # Make the left child the new comparator
                    else: root_tnode = root_tnode.lc
                elif new_tnode.key > root_tnode.key: 
                    if root_tnode.rc == None: 
                        root_tnode.rc = new_tnode
                        break
                    # Make the right child the new comparator 
                    else: root_tnode = root_tnode.rc

    # search method 
    def search(self, key): 
        # This will not be that different from the insert method 

        if self.is_empty(): 
            # If the tree is empty, make the new node the root
            return False
        else: 
            root_tnode = self.root 

            # If key found at root node 
            while True: 
                if key == root_tnode.key: 
                    return True 
                else:
                    if key <= root_tnode.key: 
                        if root_tnode.lc is None: 
                            return False
                        else: 
                            root_tnode = root_tnode.lc
                    elif key > root_tnode.key: 
                        if root_tnode.rc is None: 
                            return False
                        else: 
                            root_tnode = root_tnode.rc

    def inorder(self, current_tnode):
        # You have to do this recursively
        if current_tnode is not None: 
            self.inorder(current_tnode.lc)
            print (f"{current_tnode.key}" + " ->", end=" ")
            self.inorder(current_tnode.rc)

    def preorder(self, current_tnode):
        if current_tnode is not None: 
            print (f"{current_tnode.key}" + " ->", end=" ")
            self.preorder(current_tnode.lc)
            self.preorder(current_tnode.rc)

    def postorder(self, current_tnode):
        if current_tnode is not None: 
            self.postorder(current_tnode.lc)
            self.postorder(current_tnode.rc)
            print (f"{current_tnode.key}" + " ->", end=" ")

    # minimum method 
    def treeMIN(self, start_node): 
        if self.is_empty(): 
            return "Tree is empty"
        
        # Start from root
        current_node = start_node

        while True: 
            if current_node.lc is None: 
                return current_node.key 
            else: 
                current_node = current_node.lc

    # parent method 
    def parent(self, key): 
        if self.is_empty(): 
            return "Tree is empty" 
        
        current_node = self.root

        while current_node is not None:
            if current_node.key == key: 
                return "Key is the root node"

            elif key < current_node.key: 
                if current_node.lc.key == key:
                    return current_node.key
                else: 
                    current_node = current_node.lc

            else: 
                if key > current_node.key: 
                    if current_node.rc.key == key:
                        return current_node.key
                    else: 
                        current_node = current_node.rc	

    # successor method 
    def succ(self, current_tnode):
        if self.is_empty(): 
            return "Tree is empty" 
        
        if current_tnode.rc is not None: 
            return self.treeMIN(current_tnode.rc)
        else: 
            parent_tnode = self.parent(current_tnode.key) 

            while parent_tnode is not None and current_tnode == parent_tnode.rc:
                current_tnode = parent_tnode
                parent_tnode = self.parent(parent_tnode.key)

            return parent_tnode
    
    # height method 
    def height(self, current_tnode):

        if current_tnode == None: 
            height = 0 
            return height 
        # Go left, recursively 
        left_height = self.height(current_tnode.lc)
        # Go right, recursively
        right_height = self.height(current_tnode.rc)

        return 1 + max(left_height, right_height)

    # delete method
    def delete(self, key): 
        if self.is_empty(): 
            # If the tree is empty, make the new node the root
            return ("Tree is empty")
        else: 
            root_tnode = self.root 

            # If key found at root node 
            while True: 
                if key == root_tnode.key: 
                    if root_tnode.rc is None: 
                        # Make the key None
                        root_tnode = None
                    elif root_tnode.rc is not None: 
                        root_tnode = root_tnode.rc 
                else:
                    if key <= root_tnode.key: 
                        if root_tnode.lc is None: 
                            return "Key not in tree"
                        else: 
                            root_tnode = root_tnode.lc
                    elif key > root_tnode.key: 
                        if root_tnode.rc is None: 
                            return "Key not in tree"
                        else: 
                            root_tnode = root_tnode.rc
        
        

def main(): 
    bst = BST()

    bst.insert(1)

    print(bst.search(1)) # True

    print(bst.search(2)) # False

    bst.insert(2)

    print(bst.search(2)) # True

    bst.inorder(bst.root) # 1 -> 2 ->
    print("\n")

    bst.insert(3)
    bst.insert(4)
    bst.insert(5) 

    bst.inorder(bst.root) # 1 -> 2 -> 3 -> 4 -> 5 ->
    print("\n")

    bst.preorder(bst.root) # 1 -> 2 -> 3 -> 4 -> 5 ->
    print("\n")

    bst.postorder(bst.root) # 5 -> 4 -> 3 -> 2 -> 1 ->
    print("\n")

    print(bst.treeMIN(bst.root)) # 1

    print(bst.parent(3)) # 2

    print(f"Height: {bst.height(bst.root)}") # Height: 5
main()