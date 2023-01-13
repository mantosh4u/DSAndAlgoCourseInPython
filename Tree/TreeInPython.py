

class Tree:

    # Constructor
    def __init__(self, initval = None):
        self.value = initval
        if(self.value):
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


