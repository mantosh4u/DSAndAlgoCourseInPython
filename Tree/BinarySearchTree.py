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


    # make current node empty.
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return


    # make current node assign all which is present in right side of node.
    def copyright(self):
        self.value = self.right.value
        self.left  = self.right.left
        self.right = self.right.right

    # make current node assign all which is present in left side of node.
    def copyleft(self):
        self.value = self.left.value
        self.right = self.left.right
        self.left  = self.left.left


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


    def insert(self,v):
        """ Find the positon of the v if it would have already be in the tree.
        thats the place it should be kept/insert. """

        # If current tree is empty and we call insert. 
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        
        # if value which needs to be inserted is already present. do nothing.
        if self.value == v:
            return
        
        # if value which needs to be inserted is smaller than current node value.
        if(v < self.value):
            self.left.insert(v)
            return
        
        # if value which needs to be inserted is greated than current node value.
        if(v > self.value):
            self.right.insert(v)
            return
    

    


    def delete(self, v):
        """ Find if it exists in the treee and in case found delete it. but after deleting 
        it, we need to rebalance it."""
    
        # If current tree is empty and we call delete, do nothing.
        if self.isempty():
            return

        # If value which needs to be deleted is smaller than current node value.
        if(v < self.value):
            self.left.delete(v)
            return
        
        # If value which needs to be deleted is greated than current node value.
        if(v > self.value):
            self.right.delete(v)
            return

        # If value is found, then we need to handle it more carefully and all cases should
        # be covered.
        if(v == self.value):
            # if current node is leaf node, then just delete is
            if(self.isleaf()):
                self.makeempty()
            
            # if current node is non leaf node with just right child presence.
            elif(self.left.isempty()):
                self.copyright()
            
            # if current node is non leaf node with just left child presence.
            elif(self.right.isempty()):
                self.copyleft()
            
            # if current node is non leaf node with both right and left child presence. Find the maximum value
            # in the left subtree region and keep it here. And now delete that particular node form the left
            # subtree regions.
            else:
                self.value = self.left.maxvalue()
                self.left.delete(self.left.maxvalue())

            return










####################################################################################
##############################________main_________#################################
####################################################################################


# tvRootTree = Tree(5)
# tvLeftChild = Tree(3)
# tvRightChild = Tree(8)

# tvRootTree.left = tvLeftChild
# tvRootTree.right = tvRightChild

# operationList = [tvRootTree.inorder(), tvRootTree.preorder(), tvRootTree.postorder(), \
#                 tvRootTree.find(20), tvRootTree.find(3), \
#                 tvRootTree.minvalue(), tvRootTree.maxvalue()]

# for singleOperation in operationList:
#     print(operationList)
#     break


# Create empty tree
tvRoot = Tree()

tvInputList = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 28, 0, 6, 44, -1]
for item in tvInputList:
    tvRoot.insert(item)

# sorted sequence in ascending order
print(tvRoot.inorder())
# print min value
print(tvRoot.minvalue())
# print max value
print(tvRoot.maxvalue())

# lets us delete max and min value and then print the sorted sequence.
tvRoot.delete(tvRoot.maxvalue())
tvRoot.delete(tvRoot.minvalue())

print(tvRoot.inorder())

print("Completed Successfully")
