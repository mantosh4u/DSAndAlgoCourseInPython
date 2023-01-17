# How to represent weighted graph where each edges would have different weights like 
# cost, time, distance...

import random
import time

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np



gDoWeNeedToInitialize    = True
gVertexToIncomingEdgeList = {}




def create_adjacency_matrix_helper(fvVerticesCount, fvEdgeList):
    """create_adjacency_matrix_helper"""

    # create tvA matrix with fvVerticesCountxfvVerticesCount length with empty(None) value
    # post this, initialize with (0,0)
    tvA = np.empty(shape=(fvVerticesCount,fvVerticesCount), dtype=tuple)
    tvA.fill((0,0))

    # now traverse the graph and update edge connection values if any.
    for ((i,j),k) in fvEdgeList:
        tvA[i,j] = (1,k)

    return tvA






def create_adjacency_list_helper(fvVerticesCount, fvEdgeList):
    """ create_adjacency_list_helper """

    tvAdjacencyList = {}
    for index in range(0, fvVerticesCount):
        tvAdjacencyList[index]= []    

    # let us traverse the graph and insert the data.
    for index in range(0, len(fvEdgeList)):
        ((i,j),k) = fvEdgeList[index]
        tvIndexValue = i
        tvWeightValue = (j,k)
        tvIndexValueList = tvAdjacencyList[tvIndexValue]
        tvIndexValueList.append(tvWeightValue)
        tvAdjacencyList[tvIndexValue] = tvIndexValueList
        

    return tvAdjacencyList









#########
# Graph#1
#########

# 0 -------80---------> 2 ---------70--------> 3
# |                    /|\
# |                     |6
# |_ _ _ _ _ 10 _ _ _ _>1_ _ _20 _ _ _>4 ------50------->5
#                                      |      _ _ _ _ _ /|\
#                                      |5    /
#                                      |    / 10
#                                     \|/  / 
#                                      6 /

# Weighted Adjacency Matrix representation of above graph in memory

# [
#     [(0, 0) (1, 10) (1, 80) (0, 0) (0, 0) (0, 0) (0, 0)]
#     [(0, 0) (0, 0) (1, 6) (0, 0) (1, 20) (0, 0) (0, 0)]
#     [(0, 0) (0, 0) (0, 0) (1, 70) (0, 0) (0, 0) (0, 0)]
#     [(0, 0) (0, 0) (0, 0) (0, 0) (0, 0) (0, 0) (0, 0)]
#     [(0, 0) (0, 0) (0, 0) (0, 0) (0, 0) (1, 50) (1, 5)]
#     [(0, 0) (0, 0) (0, 0) (0, 0) (0, 0) (0, 0) (0, 0)]
#     [(0, 0) (0, 0) (0, 0) (0, 0) (0, 0) (1, 10) (0, 0)]
#  ]



# Weighted Adjacency List representation of above graph in memory

# 0: [(1, 10), (2, 80)]
# 1: [(2, 6), (4, 20)]
# 2: [(3, 70)]
# 3: []
# 4: [(5, 50), (6, 5)]
# 5: []
# 6: [(5, 10)]





def create_graph_into_adjacency_matrix_or_list_one(fvType):
    """" create_graph_into_adjacency_matrix_or_list_one """

    # Number of vertices.
    tvVerticesCount = 7

    # represent a graph relation between the vertices and edge connection
    tvEdges = [((0,1),10), ((0,2),80),
               ((1,2),6),  ((1,4),20),
               ((2,3),70),
            
               ((4,5),50), ((4,6),5),

               ((6,5),10)
               ]
    
    # # All edges with equal weights to see how Algorithms works. It works as expected.
    # tvEdges = [((0,1),1), ((0,2),1),
    #            ((1,2),1),  ((1,4),1),
    #            ((2,3),1),
            
    #            ((4,5),1), ((4,6),1),

    #            ((6,5),1)
    #            ]
    

    
    if(fvType == "matrix"):
        return create_adjacency_matrix_helper(tvVerticesCount, tvEdges)
    elif(fvType == "list"):
        return create_adjacency_list_helper(tvVerticesCount, tvEdges)
    else:
        return None









#######################
# Graph#2(Negative Edge)
########################

#                       10                 1                    1
#            0 -------------------->1<-----------------2---------------------->3
#           /                     /|\|                /|\                      |
#         8/          _ _ _ _ _ _ _| |                 |                       |
#         /          /               |                 |                       |
#       </          /    _ _ _ _ _ _ |                 |                       |
#       7        -4/     |                             |                       |
#       |        /       |                             |                       |
#      1|      /         |                           -2|                      3|
#       |    /          2|                             |                       |
#      \|/ /             |                             |                       |
#       6                |                             |                       |
#        \     _ _ _ _ _ |                             |                       |
#       -1 \ \|/_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|                       |
#            \>5                                                               |
#             /|\                                                              |
#              |                                                               |
#              |                                                              \|/
#              |_ _ _ _ _ _ _ _ _ _ _ _-1 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _4



# Weighted Adjacency Matrix representation of above graph in memory

# [
#     [(0, 0), (1, 10), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 8)],
#     [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 2), (0, 0), (0, 0)],
#     [(0, 0), (1, 1), (0, 0), (1, 1), (0, 0), (0, 0), (0, 0), (0, 0)],
#     [(0, 0), (0, 0), (0, 0), (0, 0), (1, 3), (0, 0), (0, 0), (0, 0)],
#     [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, -1), (0, 0), (0, 0)],
#     [(0, 0), (0, 0), (1, -2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
#     [(0, 0), (1, -4), (0, 0), (0, 0), (0, 0), (1, -1), (0, 0), (0, 0)],
#     [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 1), (0, 0)]   
# ]
      


# Weighted Adjacency List representation of above graph in memory

# 0: [(1, 10), (7, 8)]
# 1: [(5, 2)]
# 2: [(1, 1), (3, 1)]
# 3: [(4, 3)]
# 4: [(5, -1)]
# 5: [(2, -2)]
# 6: [(1, -4), (5, -1)]
# 7: [(6, 1)]




def create_graph_into_adjacency_matrix_or_list_two(fvType):
    """" create_graph_into_adjacency_matrix_or_list_two """

    # Number of vertices.
    tvVerticesCount = 8

    # represent a graph relation between the vertices and edge connection
    tvEdges = [((0,1),10), ((0,7),8),
               ((1,5),2),
               ((2,1),1),  ((2,3),1),
			   ((3,4),3),
               ((4,5),-1),
			   ((5,2),-2),	
               ((6,1),-4), ((6,5),-1),
			   ((7,6),1)
               ]
    
    if(fvType == "matrix"):
        return create_adjacency_matrix_helper(tvVerticesCount, tvEdges)
    elif(fvType == "list"):
        return create_adjacency_list_helper(tvVerticesCount, tvEdges)
    else:
        return None











#########
# Graph#3(Undirected graph)
#########

#                   70
#         2 - - - - - - - - - - - - 3
#        /  \                         \
#    18 /    \ 6                        \ 8
#      /      \                           \
#    /          \                           \
#   /            \                           \   
# 0---------------1---------------------------4
#        10                     20


# Weighted Adjacency Matrix representation of above graph in memory

# [
#     [(0, 0) (1, 10) (1, 18) (0, 0) (0, 0)]
#     [(1, 10) (0, 0) (1, 6) (0, 0) (1, 20)]
#     [(1, 18) (1, 6) (0, 0) (1, 70) (0, 0)]
#     [(0, 0) (0, 0) (1, 70) (0, 0) (1, 8)]
#     [(0, 0) (1, 20) (0, 0) (1, 8) (0, 0)]
# ]



# Weighted Adjacency List representation of above graph in memory

# 0: [(1, 10), (2, 18)]
# 1: [(0, 10), (2, 6), (4, 20)]
# 2: [(0, 18), (1, 6), (3, 70)]
# 3: [(2, 70), (4, 8)]
# 4: [(1, 20), (3, 8)]



def create_graph_into_adjacency_matrix_or_list_three(fvType):
    """" create_graph_into_adjacency_matrix_or_list_three """

    # Number of vertices.
    tvVerticesCount = 5

    # represent a graph relation between the vertices and edge connection
    tvEdges = [((0,1),10), ((0,2),18),
               ((1,0),10),  ((1,2),6), ((1,4),20), 
               ((2,0),18),  ((2,1),6), ((2,3),70),
               ((3,2),70),  ((3,4),8),
               ((4,1),20),  ((4,3),8)
               ]
    
    
    if(fvType == "matrix"):
        return create_adjacency_matrix_helper(tvVerticesCount, tvEdges)
    elif(fvType == "list"):
        return create_adjacency_list_helper(tvVerticesCount, tvEdges)
    else:
        return None






#########
# Graph#4(Undirected graph)
#########

#
#                             70
#         2 -------------------------------3
#        /  \                         
#    18 /    \ 6                        
#      /      \                           
#    /          \                           
#   /            \                           
# 0---------------1---------------------------4-------------- 5
#        10                    20              \     10      /
#                                                \          /    
#                                              10 \        / 5
#                                                  \      /
#                                                   \    /
#                                                    \6/
#


# Weighted Adjacency Matrix representation of above graph in memory

# [
#     [(0, 0), (1, 10), (1, 18), (0, 0), (0, 0), (0, 0), (0, 0)],
#     [(1, 10), (0, 0), (1, 6), (0, 0), (1, 20), (0, 0), (0, 0)],
#     [(1, 18), (1, 6), (0, 0), (1, 70), (0, 0), (0, 0), (0, 0)],
#     [(0, 0), (0, 0), (1, 70), (0, 0), (0, 0), (0, 0), (0, 0)],
#     [(0, 0), (1, 20), (0, 0), (0, 0), (0, 0), (1, 10), (1, 10)],
#     [(0, 0), (0, 0), (0, 0), (0, 0), (1, 10), (0, 0), (1, 5)],
#     [(0, 0), (0, 0), (0, 0), (0, 0), (1, 10), (1, 5), (0, 0)]
# ]



# Weighted Adjacency List representation of above graph in memory

# 0: [(1, 10), (2, 18)]
# 1: [(0, 10), (2, 6), (4, 20)]
# 2: [(0, 18), (1, 6), (3, 70)]
# 3: [(2, 70)]
# 4: [(1, 20), (5, 10), (6, 10)]
# 5: [(4, 10), (6, 5)]
# 6: [(4, 10), (5, 5)]




def create_graph_into_adjacency_matrix_or_list_four(fvType):
    """" create_graph_into_adjacency_matrix_or_list_four """

    # Number of vertices.
    tvVerticesCount = 7

    # represent a graph relation between the vertices and edge connection
    tvEdges = [((0,1),10), ((0,2),18),
               ((1,0),10),  ((1,2),6), ((1,4),20), 
               ((2,0),18),  ((2,1),6), ((2,3),70),
               ((3,2),70),
               ((4,1),20),  ((4,5),10), ((4,6),10),
               ((5,4),10),  ((5,6),5),
               ((6,4),10),  ((6,5),5)
               ]
    
    
    if(fvType == "matrix"):
        return create_adjacency_matrix_helper(tvVerticesCount, tvEdges)
    elif(fvType == "list"):
        return create_adjacency_list_helper(tvVerticesCount, tvEdges)
    else:
        return None







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
        if(fvAMatrix[i,ColIndex][0] == 1):
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
        if(fvAMatrix[rowIndex, i][0] == 1):
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
    tvArrowList = fvAList[i]

    for index in range(len(tvArrowList)):
        tvCurrentNode = tvArrowList[index]
        tvNeighboursList.append(tvCurrentNode[0])    
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
                aNeighbourVertexIndexValue = tvCurrentIndexNeighbourList[aNeighbour][0]
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





def get_weightValue_of_matrixedge(fvAMatrix, fvFirstNode, fvSecondNode):
    """ get_weightValue_of_matrixedge """

    tvWeightValue = 0

    tvCellValue = fvAMatrix[fvFirstNode, fvSecondNode]
    tvWeightValue =  tvCellValue[1]
    return tvWeightValue




def get_weightValue_of_listedge(fvAList, fvFirstNode, fvSecondNode):
    """ get_weightValue_of_listedge """

    tvWeightValue = 0
    tvEdgeList = fvAList[fvFirstNode]
    for (index, weight) in tvEdgeList:
        if(fvSecondNode == index):
            tvWeightValue = weight
            break

    return tvWeightValue





def get_weightValue(fvAInput, fvFirstNode, fvSecondNode):
    """" call appropriate get_weightValue based on type."""

    tvWeightValue = 0
    if( isinstance(fvAInput, dict) == True):
        tvWeightValue = get_weightValue_of_listedge(fvAInput, fvFirstNode, fvSecondNode)
    elif( isinstance(fvAInput, np.ndarray) == True):
        tvWeightValue = get_weightValue_of_matrixedge(fvAInput, fvFirstNode, fvSecondNode)
    return tvWeightValue

