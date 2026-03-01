ot_tnode = self.root 

                if new_tnode.key <= root_tnode.key: 
                    if root_tnode.lc == None: 
                        root_tnode.lc = new_tnode
                    # Make the left child the new comparator
                    else: root_tnode = root_tnode.lc
                elif new_tnode.key > root_tnode.key: 
                    if root_tnode.rc == None: 
                        root_tnode.rc = new_tnode
                    # Make the right child the new comparator 
                    e