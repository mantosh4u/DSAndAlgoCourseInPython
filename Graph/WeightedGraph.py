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









def create_graph_into_adjacency_matrix(fvSequence):
    """ choose which graph to use for creating the adjacency matrix to run alogrithms"""
    
    tvType = "matrix"
    
    if(fvSequence == 1):
        return (create_graph_into_adjacency_matrix_or_list_one(tvType))
    elif(fvSequence == 2):
        return (create_graph_into_adjacency_matrix_or_list_one(tvType))
    



def create_graph_into_adjacency_list(fvSequence):
    """ choose which graph to use for creating the adjacency list to run alogrithms"""

    tvType = "list"

    if(fvSequence == 1):
        return (create_graph_into_adjacency_matrix_or_list_one(tvType))
    elif(fvSequence == 2):
        return (create_graph_into_adjacency_matrix_or_list_one(tvType))
    

















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



############################################################################################
#################################### In-degree Calculation #################################
############################################################################################
def indegreeValAMatrix(fvAMatrix, i):
    """ finding out the indegree from the given Adjacency Matrix and a particular vertex. 
    Indegree basically denotes number of incoming edges to a particular vertex."""

    return len(incomingEdgesAMatrix(fvAMatrix, i)) 



############################################################################################
#################################### Out-degree Calculation ################################
############################################################################################
def outdegreeValAMatrix(fvAMatrix, i):
    """ finding out the outdegree from the given Adjacency Matrix and a particular vertex. 
    outdegree basically denotes number of outgoing edges to a particular vertex. So it is
    essentially the same as finding out neighbours of a given node."""

    return len(neighboursAMatrix(fvAMatrix, i))    









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
#################################### In-degree Calculation #################################
############################################################################################
def indegreeValAList(fvAList, i):
    """ finding out the indegree from the given Adjacency Matrix and a particular vertex. 
    Indegree basically denotes number of incoming edges to a particular vertex."""

    return len(incomingEdgesAlist(fvAList, i)) 



############################################################################################
#################################### Out-degree Calculation ################################
############################################################################################
def outdegreeValAList(fvAList, i):
    """ finding out the outdegree from the given Adjacency Matrix and a particular vertex. 
    outdegree basically denotes number of outgoing edges to a particular vertex. So it is
    essentially the same as finding out neighbours of a given node."""

    return len(neighboursAList(fvAList, i))    
    
