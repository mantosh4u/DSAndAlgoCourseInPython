# In computer science, a binary search tree (BST), also called an ordered or sorted binary tree, is a rooted binary 
# tree data structure with the key of each internal node being greater than all the keys in the respective node's 
# left subtree and less than the ones in its right subtree. The time complexity of operations on the binary search 
# tree is directly proportional to the height of the tree.

# Binary search trees allow binary search for fast lookup, addition, and removal of data items. Since the nodes in 
# a BST are laid out so that each comparison skips about half of the remaining tree, the lookup performance is 
# proportional to that of binary logarithm. BSTs were devised in the 1960s for the problem of efficient storage 
# of labeled data and are attributed to Conway Berners-Lee and David Wheeler.
    

# For each node with value v.
#   All values to left subtree are   < v
#   All values to right subtree are  > v
#   No duplicates values are allowed in binary search tree.




class Tree:

    # Constructor
    def __init__(self, initval = None):
        self.value = initval
        if(self.value != None):
            self.left  = Tree()
            self.right = Tree()
        else:
            self.left  = None
            self.right = None

        return
    

    # only empty node has value None
    def isempty(self):
        return (self.value == None)
    
    # Leaf node have both children empty
    def isleaf(self):
        return (self.value != None  and
                self.left.isempty() and
                self.right.isempty() )
    

    # In order traversal
    def inorder(self):
        if(self.isempty()):
            return ([])
        else:
            return (self.left.inorder() +
                    [self.value] +
                    self.right.inorder() )



    # Display Tree as a string
    def __str__(self):
        return (str(self.inorder() ) )
    


    # Pre order traversal
    def preorder(self):
        if(self.isempty()):
            return ([])
        else:
            return ([self.value] + 
                    self.left.preorder() +
                    self.right.preorder() )


    # Post order traversal
    def postorder(self):
        if(self.isempty()):
            return ([])
        else:
            return ( self.left.postorder() +
                    self.right.postorder() +
                    [self.value] )


    # check if value v occurs in a tree
    def find(self, v):
        if(self.isempty()):
            return False
        if(self.value == v):
            return True
        
        if(v < self.value):
            return (self.left.find(v))
        
        if(v > self.value):
            return (self.right.find(v))
        

    # go to the left most last value where we find minimum
    def minvalue(self):
        if(self.left.isempty()):
            return self.value
        else:
            return(self.left.minvalue())


    # go to the right most last value where we find maximum
    def maxvalue(self):
        if(self.right.isempty()):
            return self.value
        else:
            return(self.right.maxvalue())


    # find the positon of the v if it would have already be in the tree.
    # thats the place it should be kept/insert.
    def insert(self,v):
        pass
    

    # find if it exists in the treee and in case found delete it.
    # but after deleting it, we need to rebalance it.
    def delete(self, v):
        pass












####################################################################################
##############################________main_________#################################
####################################################################################


tvRootTree = Tree(5)
tvLeftChild = Tree(3)
tvRightChild = Tree(8)

tvRootTree.left = tvLeftChild
tvRootTree.right = tvRightChild

operationList = [tvRootTree.inorder(), tvRootTree.preorder(), tvRootTree.postorder(), \
                tvRootTree.find(20), tvRootTree.find(3), \
                tvRootTree.minvalue(), tvRootTree.maxvalue()]

for singleOperation in operationList:
    print(operationList)
    break

print("Completed Successfully")
