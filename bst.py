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

main()