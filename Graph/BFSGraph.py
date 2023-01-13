import random
import time

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np



gDoWeNeedToInitialize    = True
gVertexToIncomingEdgeList = {}



############################################################################################
######################################### Basic Practices###################################
############################################################################################

def basic_matrix_operation():
    """"Basic matrix operations understanding and practice."""

    print(">> basic_matrix_operation")

    # seeds for reproducibility
    np.random.seed(0)

    x1 = np.random.randint(10, size = 6)      #1x6 matrix
    x2 = np.random.randint(10, size =(3,4))   #3x4 matrix
    x3 = np.random.randint(10, size =(4,4))   #4x4 matrix

    print("x1 ndim: ", x1.ndim)
    print("x2 shape:", x2.shape)
    print("x3 size: ", x3.size)

    # lets learn some slice stuff.
    # x[start:stop:step]
    # default start = 0
    # stop = size of dimenson
    # step = 1
    # x[::-1] means x[0:len:-1]
    # This means it would print the reverese list
    print(x1[::-1])

    print("<< basic_matrix_operation")




def create_adjacency_matrix_helper(fvVerticesCount, fvEdgeList):
    """create_adjacency_matrix_helper"""

    # intialize tvA matrix with fvVerticesCountxfvVerticesCount length
    tvA = np.zeros(shape=(fvVerticesCount,fvVerticesCount))

    # now traverse the graph and update edge connection values if any.
    for  (i,j) in fvEdgeList:
        tvA[i,j] = 1

    return tvA


def create_adjacency_list_helper(fvVerticesCount, fvEdgeList):
    """ create_adjacency_list_helper """

    tvAdjacencyList = {}
    for index in range(0, fvVerticesCount):
        tvAdjacencyList[index]= []    

    # let us traverse the graph and insert the data.
    for index in range(0, len(fvEdgeList)):
        tvValue = fvEdgeList[index]
        i = tvValue[0]
        j = tvValue[1]
        tvIndexValueList = tvAdjacencyList[i]
        tvIndexValueList.append(j)
        tvAdjacencyList[i] = tvIndexValueList
        

    # for index in range(0, fvVerticesCount):
    #     print(str(index) + ": " +  tvAdjacencyList[index].__str__() )

    return tvAdjacencyList






#########
# Graph#1
#########

#            0
#            |
#           \|/
#   1       2
#    \     / \                  8
#     \>3</   \>4               | 
#       \     /                \|/
#        \>5</                  9
#          | \                  | 
#         \|/   \               |
#          6       \            |
#          |          \         |
#         \|/             \    \|/
#          7                \> 10
#           \                  |
#            \                \|/
#             \                11
#               \              |
#                 \            |
#                    \         |
#                      \       |
#                        \    \|/
#                          \ > 12
#                              |
#                             \|/
#                             13


# Adjacency Matrix representation of above graph in memory

#   [ 
#   [0  0  1  0  0  0  0  0  0  0  0  0  0  0]
#   [0  0  0  1  0  0  0  0  0  0  0  0  0  0]
#   [0  0  0  1  1  0  0  0  0  0  0  0  0  0]
#   [0  0  0  0  0  1  0  0  0  0  0  0  0  0]
#   [0  0  0  0  0  1  0  0  0  0  0  0  0  0]
#   [0  0  0  0  0  0  1  0  0  0  1  0  0  0]
#   [0  0  0  0  0  0  0  1  0  0  0  0  0  0]
#   [0  0  0  0  0  0  0  0  0  0  0  0  1  0]
#   [0  0  0  0  0  0  0  0  0  1  0  0  0  0]
#   [0  0  0  0  0  0  0  0  0  0  1  0  0  0]
#   [0  0  0  0  0  0  0  0  0  0  0  1  0  0]
#   [0  0  0  0  0  0  0  0  0  0  0  0  1  0]
#   [0  0  0  0  0  0  0  0  0  0  0  0  0  1]
#   [0  0  0  0  0  0  0  0  0  0  0  0  0  0] 
#   ]


# Adjacency List representation of above graph in memory

# 0: [2]
# 1: [3]
# 2: [3, 4]
# 3: [5]
# 4: [5]
# 5: [6, 10]
# 6: [7]
# 7: [12]
# 8: [9]
# 9: [10]
# 10: [11]
# 11: [12]
# 12: [13]
# 13: []


def create_graph_into_adjacency_matrix_or_list_one(fvType):
    """" create_graph_into_adjacency_matrix_or_list_one """

    # Number of vertices.
    tvVerticesCount = 14

    # represent a graph relation between the vertices and edge connection
    tvEdges = [(0,2),
               (1,3),
               (2,3), (2,4),
               (3,5),
               (4,5),
               (5,6), (5,10),
               (6,7),
               (7,12),
               (8,9),
               (9,10),
               (10,11),
               (11, 12),
               (12, 13)
               ]

    if(fvType == "matrix"):
        return create_adjacency_matrix_helper(tvVerticesCount, tvEdges)
    elif(fvType == "list"):
        return create_adjacency_list_helper(tvVerticesCount, tvEdges)
    else:
        return None



    






#########
# Graph#2
#########

#           >0
#          / >/\
#         /  /  \
#        /  /    >1
#       /  /    /
#      /  /   /
#     /  /_ _/_ _ _ _
#     |    /        /
#     2 < /       /
#     /         /
#    /        /
#   /  <----/
#  4 <- - - - - - - - -> 3
# <\                 >/  \
#   \               /      \
#     \            /        \>
#      \          5<- - - - -6
#       \        / <\
#         \     /    \
#         >\  </      \
#          7 / - -- - ->8
#                      >/
#                     /
#                    /
#                   /
#                 </
#                 9

def create_graph_into_adjacency_matrix_or_list_two(fvType):
    """" create_graph_into_adjacency_matrix_or_list_two """

    # Number of vertices.
    tvVerticesCount = 10

    # represent a graph relation between the vertices and edge connection
    tvEdges = [(0,1),(0,4),
               (1,2),
               (2,0),
               (3,4), (3,6),
               (4,0), (4,3), (4,7),
               (5,3), (5,7),
               (6,5),
               (7,4), (7,8),
               (8,5), (8,9),
               (9,8)
               ]

    if(fvType == "matrix"):
        return create_adjacency_matrix_helper(tvVerticesCount, tvEdges)
    elif(fvType == "list"):
        return create_adjacency_list_helper(tvVerticesCount, tvEdges)
    else:
        return None





#########
# Graph#3
#########

#   0---->1
#   |
#   |
#  \|/
#   2----> 4
#   |
#   |
#  \|/
#   3
#   

def create_graph_into_adjacency_matrix_or_list_three(fvType):
    """" create_graph_into_adjacency_matrix_or_list_three """


    # Number of vertices.
    tvVerticesCount = 5

    # represent a graph relation between the vertices and edge connection
    tvEdges = [(0,1),(0,2),
               
               (2,3), (2,4)
               
               ]

    if(fvType == "matrix"):
        return create_adjacency_matrix_helper(tvVerticesCount, tvEdges)
    elif(fvType == "list"):
        return create_adjacency_list_helper(tvVerticesCount, tvEdges)
    else:
        return None





#########
# Graph#4
#########

#   0----->1        2- - - - - - ->3
#   |               |<\          /
#   |               |    \       /
#  \|/             \|/      \   </
#   4      5        6--------->\> 7
#   |<\           /|\         /  |
#   |   \           |        /   |
#   |    \          |       /    |
#  \|/    \        |<--- /     \|/ 
#   8----->9       10           11
#   


def create_graph_into_adjacency_matrix_or_list_four(fvType):
    """" create_graph_into_adjacency_matrix_or_list_four """

    # Number of vertices.
    tvVerticesCount = 12

    # represent a graph relation between the vertices and edge connection
    tvEdges = [(0,1),(0,4),
               
               (2,3), (2,6),
               (3,7),
               (4,8),

               (6,7),
               (7,2), (7,10), (7,11),
               (8,9),
               (9,4),
               (10,6)
               ]

    if(fvType == "matrix"):
        return create_adjacency_matrix_helper(tvVerticesCount, tvEdges)
    elif(fvType == "list"):
        return create_adjacency_list_helper(tvVerticesCount, tvEdges)
    else:
        return None




#########
# Graph#5
#########

#       0                 1--------------------
#      /| \             / |                   |
#     /_| _ \ _ _ _ _ _/  |                   |
#   </< |     \           |                   |
#  2    |       \         |                   |
#       |        \> /_ _ _|                   |
#      \|/        4 \                         |
#       3            |                        |
#       | \          |                        |
#       |  \         |_ _ _ _ _ _ _ _         | 
#       |   \_ _ _ _ _ _ _ _ _       |        |
#       |                    |       |        |
#      \|/                  \|/      |        |
#       5 ------> 6 -------> 7<------|        |
#                           /|\               |               
#                            |_ _ _ _ _ _ _ _ |
#



def create_graph_into_adjacency_matrix_or_list_five(fvType):
    """" create_graph_into_adjacency_matrix_or_list_five """

    # Number of vertices.
    tvVerticesCount = 8

    # represent a graph relation between the vertices and edge connection
    tvEdges = [(0,2),(0,3), (0,4), 
               (1,2), (1,7),
               (2,5),
               (3,5),(3,7),
               (4,7),
               (5,6),
               (6,7)

               ]

    if(fvType == "matrix"):
        return create_adjacency_matrix_helper(tvVerticesCount, tvEdges)
    elif(fvType == "list"):
        return create_adjacency_list_helper(tvVerticesCount, tvEdges)
    else:
        return None




















class Queue:
    """Queue implementation using list data structures as member. """

    def __init__(self):
        self.ivQueue = []
    
    def addq(self, fvValue):
        self.ivQueue.append(fvValue)
    
    def delq(self):
        tvValue = None
        if not self.isEmpty():
            tvValue = self.ivQueue[0]
            self.ivQueue = self.ivQueue[1:]
        return tvValue
    
    def isEmpty(self):
        return (len(self.ivQueue) == 0)

    def __str__(self):
        return (str(self.ivQueue))








class Stack:
    """Stack implementation using list data structures as member. """

    def __init__(self):
        self.ivStack = []
    
    def push(self, fvValue):
        self.ivStack.append(fvValue)
    
    def pop(self):
        tvValue = None
        if not self.isEmpty():
            tvValue = self.ivStack[-1]
            self.ivStack = self.ivStack[0:len(self.ivStack)-1]
        return tvValue
    
    def top(self):
        tvValue = None
        if not self.isEmpty():
            tvValue = self.ivStack[-1]
        return tvValue
    
    def isEmpty(self):
        return (len(self.ivStack) == 0)

    def __str__(self):
        return (str(self.ivStack))







def basic_learning_of_queue():
    """ Basic usages of queue data structure."""
    tvQ = Queue()

    for i in range(0,3):
        tvQ.addq(i)
        print(tvQ)

    print(tvQ.isEmpty())

    for i in range(0,3):
        print(tvQ.delq(), tvQ)
    
    print(tvQ.isEmpty())






def basic_learning_of_stack():
    """ Basic usages of stack data structure."""

    tvS = Stack()

    for index in range(1, 7):
        tvS.push(index)
        print(tvS)
    
    print(tvS.isEmpty())

    for index in range(1, 7):
        print(tvS.pop(), tvS)
    
    print(tvS.isEmpty())









def create_graph_into_adjacency_matrix(fvSequence):
    """ choose which graph to use for creating the adjacency matrix to run alogrithms"""
    
    tvType = "matrix"
    
    if(fvSequence == 1):
        return (create_graph_into_adjacency_matrix_or_list_one(tvType))
    elif(fvSequence == 2):
        return (create_graph_into_adjacency_matrix_or_list_two(tvType))
    elif(fvSequence == 3):
        return (create_graph_into_adjacency_matrix_or_list_three(tvType))
    elif(fvSequence == 4):
        return (create_graph_into_adjacency_matrix_or_list_four(tvType))
    elif(fvSequence == 5):
        return (create_graph_into_adjacency_matrix_or_list_five(tvType))





def create_graph_into_adjacency_list(fvSequence):
    """ choose which graph to use for creating the adjacency list to run alogrithms"""

    tvType = "list"

    if(fvSequence == 1):
        return (create_graph_into_adjacency_matrix_or_list_one(tvType))
    elif(fvSequence == 2):
        return (create_graph_into_adjacency_matrix_or_list_two(tvType))
    elif(fvSequence == 3):
        return (create_graph_into_adjacency_matrix_or_list_three(tvType))
    elif(fvSequence == 4):
        return (create_graph_into_adjacency_matrix_or_list_four(tvType))
    elif(fvSequence == 5):
        return (create_graph_into_adjacency_matrix_or_list_five(tvType))





### For Adjacency Matrix

############################################################################################
###################################### Neighbours(Outgoing)#################################
############################################################################################
def neighboursAMatrix(fvAMatrix, i):
    """ finding out the neighbours from the given Adjacency Matrix and a particular vertex.
    For Adjacency List finding adjacency is just one loopup in the has table."""

    tvNeighboursList =  []

    (tvRows, tvCols) = fvAMatrix.shape

    for ColIndex in range(tvCols):
        if(fvAMatrix[i,ColIndex] == 1):
            tvNeighboursList.append(ColIndex)

    return tvNeighboursList




############################################################################################
################################### IncomingEdges(Incoming) ################################
############################################################################################
def incomingEdgesAMatrix(fvAMatrix, i):
    """ finding out the incomingEdges from the given Adjacency Matrix and a particular vertex.
    It is same as calculating the indegreeVal"""

    tvIncomingEdgeList =  []

    (tvRows, tvCols) = fvAMatrix.shape

    for rowIndex in range(tvRows):
        if(fvAMatrix[rowIndex, i] == 1):
            tvIncomingEdgeList.append(rowIndex)

    return tvIncomingEdgeList









### For Adjacency List

############################################################################################
###################################### Neighbours(Outgoing)#################################
############################################################################################
def neighboursAList(fvAList, i):
    """ finding out the neighbours from the given Adjacency List and a particular vertex.
    For Adjacency List finding adjacency is just one loopup in the has table."""

    tvNeighboursList =  []
    tvNeighboursList = fvAList[i]
    return tvNeighboursList




############################################################################################
################################### IncomingEdges(Incoming) ################################
############################################################################################
def incomingEdgesAlist(fvAList, i):
    """ finding out the incomingEdges from the given Adjacency List and a particular vertex.
    It is same as calculating the indegreeVal"""
    
    global gDoWeNeedToInitialize, gVertexToIncomingEdgeList

    tvIncomingEdgeList =  []

    # Initialize and calculate only once
    if(gDoWeNeedToInitialize == True):
        for index in range(len(fvAList)):
            gVertexToIncomingEdgeList[index] = []

        for index in range(len(fvAList)):
            tvCurrentIndexNeighbourList = fvAList[index]
            for aNeighbour in range(len(tvCurrentIndexNeighbourList)):
                # if present get current value and then append into the appropriate index of list
                aNeighbourVertexIndexValue = tvCurrentIndexNeighbourList[aNeighbour]
                gVertexToIncomingEdgeList[aNeighbourVertexIndexValue].append(index)

        gDoWeNeedToInitialize = False
    
    
    tvIncomingEdgeList = gVertexToIncomingEdgeList[i]
    return tvIncomingEdgeList







############################################################################################
#################### Common Utility For Adjancency Matrix & List############################
############################################################################################

def neighbours(fvAInput, i):
    """ Check out the type of 'fvAInput and then call appropriately. Neighbours means outgoing
    edges from the given node index 'i' """

    tvReturnList = []

    if( isinstance(fvAInput, dict) == True):
        tvReturnList = neighboursAList(fvAInput, i)
    elif( isinstance(fvAInput, np.ndarray) == True):
        tvReturnList = neighboursAMatrix(fvAInput, i) 
    return tvReturnList




def incomingEdges(fvAInput, i):
    """ Check out the type of 'fvAInput and then call appropriately.incomingEdges means
    incoming egdes to the given node index 'i' """

    tvReturnList = []

    if( isinstance(fvAInput, dict) == True):
        tvReturnList = incomingEdgesAlist(fvAInput, i)
    elif( isinstance(fvAInput, np.ndarray) == True):
        tvReturnList = incomingEdgesAMatrix(fvAInput, i) 
    return tvReturnList




def outdegreeVal(fvAInput, i):
    """ Outdegree value of the given node 'i'"""

    tvLen = 0
    tvLen = neighbours(fvAInput, i)
    return tvLen




def indegreeVal(fvAInput, i):
    """ Indegree value of the given node 'i'"""

    tvLen = 0
    tvLen = incomingEdges(fvAInput, i)
    return tvLen

