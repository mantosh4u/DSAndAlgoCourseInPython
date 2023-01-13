# Compute shortest paths from 0(or any edge) to all vertices.

# Practical Example
# Transport finished product from factory(single source) to all retail outlets.
# Courier company delivers items from distribution center(single source) to addresses.

# This is also known as Dijkstra's Algorithm. One of the best algorithms ever designed.


import numpy as np
import WeightedGraph


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



def min_value_index(fvShortestDistanceList, fvVisitedList):
    """min_value_index from kind of unvisited index."""

    tvSecondValueIndex = -1

    if(len(fvShortestDistanceList) > 0):
        tvSecondValue = fvShortestDistanceList[0]

        for index in range(1, len(fvShortestDistanceList)):
            if(fvVisitedList[index] == True):
                continue
            tvCurrentValue = fvShortestDistanceList[index]
            if(tvCurrentValue != 0):
                if( (tvCurrentValue <= tvSecondValue) or (tvSecondValue == 0) ):
                    tvSecondValueIndex = index
                    tvSecondValue = tvCurrentValue


    return tvSecondValueIndex




def dijkstra_singlesource_shortestdistance_initializer(fvAInput, fvShortestDistanceList, fvVisitedList):
    """ dijkstra_singlesource_shortestdistance_initializer """

    tvLen = 0

    if( isinstance(fvAInput, dict) == True):
        tvLen = len(fvAInput)
    elif( isinstance(fvAInput, np.ndarray) == True):
        (tvRows, tvCols) = fvAInput.shape
        tvLen = tvRows

    # Initialize all distance from 'fvSourceNode' is very very big number(999999).
    for index in range(0, tvLen):
        fvShortestDistanceList.append(999999)
        fvVisitedList.append(False)







def dijkstra_singlesource_shortestdistance(fvAMatrix, fvSourceNode):
    """ dijkstra_singlesource_shortestdistance """

    tvShortestDistanceList = []
    tvVisitedList          = []

    # Initialize all distance from 'fvSourceNode' is very very big number(999999).
    dijkstra_singlesource_shortestdistance_initializer(fvAMatrix, tvShortestDistanceList, tvVisitedList)

    # Now let's initialze the 'fvSourceNode' shortest distance is 0. Its so simple!!
    tvShortestDistanceList[fvSourceNode] = 0
    tvVisitedList[fvSourceNode] = True

    tvNeighboursList = WeightedGraph.neighbours(fvAMatrix, fvSourceNode)
    for aNeighbour in tvNeighboursList:
        tvWeightValue = get_weightValue(fvAMatrix, fvSourceNode, aNeighbour)
        tvShortestDistanceList[aNeighbour] = tvWeightValue


    # Loop until we have some finite value in tvShortestDistanceList
    while True:
        tvMinDistanceValIndex = min_value_index(tvShortestDistanceList, tvVisitedList)
        if(tvMinDistanceValIndex == -1):
            break
        else:
            tvVisitedList[tvMinDistanceValIndex] = True
            tvNeighboursList = WeightedGraph.neighbours(fvAMatrix, tvMinDistanceValIndex)
            for aNeighbour in tvNeighboursList:
                tvWeightValue = get_weightValue(fvAMatrix, tvMinDistanceValIndex, aNeighbour)
                tvTotalWeightOfCurrentNeighbour = tvShortestDistanceList[tvMinDistanceValIndex] + tvWeightValue
                if(tvTotalWeightOfCurrentNeighbour < tvShortestDistanceList[aNeighbour]):
                    tvShortestDistanceList[aNeighbour] = tvTotalWeightOfCurrentNeighbour


    return tvShortestDistanceList






###########################################################################################
######################################__main__#############################################
###########################################################################################


tvGraphNumber = 1
tvSourceNode = 0
# tvSourceNode = 1


tvAdjecenyMatrix  = WeightedGraph.create_graph_into_adjacency_matrix(tvGraphNumber)
# print(tvAdjecenyMatrix)

tvshortestPathToAllNodesAdjancenyMatrixList = dijkstra_singlesource_shortestdistance(tvAdjecenyMatrix, tvSourceNode)
print(tvshortestPathToAllNodesAdjancenyMatrixList)

# tvInDegreeEdgeList  = WeightedGraph.incomingEdgesAMatrix(tvAdjecenyMatrix, 4)
# tvOutDegreeEdgeList = WeightedGraph.neighboursAMatrix(tvAdjecenyMatrix, 4)
# print(tvInDegreeEdgeList, tvOutDegreeEdgeList)




tvAdjecenyList  = WeightedGraph.create_graph_into_adjacency_list(tvGraphNumber)
# print(tvAdjecenyList)

tvshortestPathToAllNodesAdjancyListList = dijkstra_singlesource_shortestdistance(tvAdjecenyList, tvSourceNode)
print(tvshortestPathToAllNodesAdjancyListList)

# tvInDegreeEdgeList  = WeightedGraph.incomingEdgesAlist(tvAdjecenyList, 4)
# tvOutDegreeEdgeList = WeightedGraph.neighboursAList(tvAdjecenyList, 4)
# print(tvInDegreeEdgeList, tvOutDegreeEdgeList)

print("Completed Sucessfully")
