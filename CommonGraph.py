import random
import time

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np






############################################################################################
######################################### BasicS Practices##################################
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










def create_graph_into_adjacency_matrix_one():
    """" create_graph_into_adjacency_matrix_one """

    print(">> create_graph_into_adjacency_matrix_one")

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

    # intialize tvA matrix with 14x14 length
    tvA = np.zeros(shape=(tvVerticesCount,tvVerticesCount))



    # now traverse the graph and update edge connection values if any.
    for  (i,j) in tvEdges:
        tvA[i,j] = 1


    print(tvA)

    # Sample adjacency matrix representation in memory
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

    print("<< create_graph_into_adjacency_matrix_one")

    return tvA







def create_graph_into_adjacency_matrix_two():
    """" create_graph_into_adjacency_matrix_two """

    print(">> create_graph_into_adjacency_matrix_two")

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

    # intialize tvA matrix with 10x10 length
    tvA = np.zeros(shape=(tvVerticesCount,tvVerticesCount))



    # now traverse the graph and update edge connection values if any.
    for  (i,j) in tvEdges:
        tvA[i,j] = 1


    print(tvA)


    # Sample adjacency matrix representation in memory
    #   [0     1   2   3   4   5   6   7   8   9
    
    # 0 [0     1   0   0   1   0   0   0   0   0]
    # 1 [0     0   1   0   0   0   0   0   0   0]
    # 2 [1     0   0   0   0   0   0   0   0   0]
    # 3 [0     0   0   0   1   0   1   0   0   0]
    # 4 [1     0   0   1   0   0   0   1   0   0]
    # 5 [0     0   0   1   0   0   0   1   0   0]
    # 6 [0     0   0   0   0   1   0   0   0   0]
    # 7 [0     0   0   0   1   0   0   0   1   0]
    # 8 [0     0   0   0   0   1   0   0   0   1]
    # 9 [0     0   0   0   0   0   0   0   1   0]
    #   ]

    print("<< create_graph_into_adjacency_matrix_two")

    return tvA







def create_graph_into_adjacency_list_one():
    """ create_graph_into_adjacency_list_one"""
    
    print(">> create_graph_into_adjacency_list_one")
    
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

    # Graph representing using the list of tuples which represents the 
    # edges between the vertices. For example (8,9) is the valid edge

    tvGraph = [(0,2),
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

    # Number of vertices.
    tvVerticesCount = 14

    # create and initialize AdjacencyList members
    tvAdjacencyList = {}
    for index in range(0, tvVerticesCount):
        tvAdjacencyList[index]= []    

    # let us traverse the graph and insert the data.
    for index in range(0, len(tvGraph)):
        tvValue = tvGraph[index]
        i = tvValue[0]
        j = tvValue[1]
        tvIndexValueList = tvAdjacencyList[i]
        tvIndexValueList.append(j)
        tvAdjacencyList[i] = tvIndexValueList
    

    for index in range(0, tvVerticesCount):
        print(str(index) + ": " +  tvAdjacencyList[index].__str__() )

    # Sample adjacency list representation in memory( Hashtable)
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

    print("<< create_graph_into_adjacency_list_one")

    return tvAdjacencyList










def create_graph_into_adjacency_list_two():
    """ create_graph_into_adjacency_list_two"""
    
    print(">> create_graph_into_adjacency_list_two")
    
    
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
                        

    # Graph representing using the list of tuples which represents the 
    # edges between the vertices. For example (8,9) is the valid edge

     # Number of vertices.
    tvVerticesCount = 10

    # represent a graph relation between the vertices and edge connection
    tvGraph = [(0,1),(0,4),
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

    # create and initialize AdjacencyList members
    tvAdjacencyList = {}
    for index in range(0, tvVerticesCount):
        tvAdjacencyList[index]= []    

    # let us traverse the graph and insert the data.
    for index in range(0, len(tvGraph)):
        tvValue = tvGraph[index]
        i = tvValue[0]
        j = tvValue[1]
        tvIndexValueList = tvAdjacencyList[i]
        tvIndexValueList.append(j)
        tvAdjacencyList[i] = tvIndexValueList
    

    for index in range(0, tvVerticesCount):
        print(str(index) + ": " +  tvAdjacencyList[index].__str__() )

    # Sample adjacency list representation in memory( Hashtable)
    # 0: [1, 4]
    # 1: [2]
    # 2: [0]
    # 3: [4, 6]
    # 4: [0, 3, 7]
    # 5: [3, 7]
    # 6: [5]
    # 7: [4, 8]
    # 8: [5, 9]
    # 9: [8]
    
    print("<< create_graph_into_adjacency_list_two")

    return tvAdjacencyList









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
    """ choose which graph to use for running alogrithms."""
    if(fvSequence == 1):
        return (create_graph_into_adjacency_matrix_one())
    if(fvSequence == 2):
        return (create_graph_into_adjacency_matrix_two())





def create_graph_into_adjacency_list(fvSequence):
    """ choose which graph to use for running alogrithms."""
    if(fvSequence == 1):
        return (create_graph_into_adjacency_list_one())
    if(fvSequence == 2):
        return (create_graph_into_adjacency_list_two())









############################################################################################
#################################### Neighbours Finding ####################################
############################################################################################

def neighbours(fvAMatrix, i):
    """ finding out the neighbours from the given Adjacency Matrix and a particular vertex.
    For Adjacency List finding adjacency is just one loopup in the has table."""

    tvNeighboursList =  []

    (tvRows, tvCols) = fvAMatrix.shape

    for rowIndex in range(tvCols):
        if(fvAMatrix[i,rowIndex] == 1):
            tvNeighboursList.append(rowIndex)

    return tvNeighboursList
