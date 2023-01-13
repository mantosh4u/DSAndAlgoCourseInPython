# Compute shortest paths from 0(or any edge) to all vertices.

# Practical Example
# Transport finished product from factory(single source) to all retail outlets.
# Courier company delivers items from distribution center(single source) to addresses.

# This is also known as Dijkstra's Algorithm. One of the best algorithms ever designed.



import WeightedGraph


def get_weightValue_of_matrixedge(fvAMatrix, fvFirstNode, fvSecondNode):
    """ get_weightValue_of_matrixedge """

    tvWeightValue = 0

    tvCellValue = fvAMatrix[fvFirstNode, fvSecondNode]
    tvWeightValue =  tvCellValue[1]
    return tvWeightValue





def min_value_index(fvShortestDistanceList, fvVisitedList):
    """min_value_index from kind of unvisited index."""

    tvSecondValueIndex = -1

    if(len(fvShortestDistanceList) > 0):
        tvSecondValueIndex = 0
        tvSecondValue = fvShortestDistanceList[0]

        for index in range(0, len(fvShortestDistanceList)):
            if(fvVisitedList[index] == True):
                continue
            tvCurrentValue = fvShortestDistanceList[index]
            if(tvCurrentValue != 0):
                if(tvCurrentValue <= tvSecondValue):
                    tvSecondValueIndex = index

    return tvSecondValueIndex









def dijkstra_singlesource_shortestdistance(fvAMatrix, fvSourceNode):
    """ dijkstra_singlesource_shortestdistance """

    tvShortestDistanceList = []
    tvVisitedList          = []

    # Initialize all distance from 'fvSourceNode' is very very big number(999999).
    (tvRows, tvCols) = fvAMatrix.shape
    for rowIndex in range(tvRows):
        tvShortestDistanceList.append(999999)
        tvVisitedList.append(False)

    # Now let's initialze the 'fvSourceNode' shortest distance is 0. Its so simple!!
    tvShortestDistanceList[fvSourceNode] = 0
    tvVisitedList[fvSourceNode] = True

    tvNeighboursList = WeightedGraph.neighboursAMatrix(fvAMatrix, fvSourceNode)
    for aNeighbour in tvNeighboursList:
        tvWeightValue = get_weightValue_of_matrixedge(fvAMatrix, fvSourceNode, aNeighbour)
        tvShortestDistanceList[aNeighbour] = tvWeightValue


    # Loop until we have some finite value in tvShortestDistanceList
    while True:
        tvMinDistanceValIndex = min_value_index(tvShortestDistanceList, tvVisitedList)
        if(tvMinDistanceValIndex == -1):
            break
        else:
            tvVisitedList[tvMinDistanceValIndex] = True
            tvNeighboursList = WeightedGraph.neighboursAMatrix(fvAMatrix, tvMinDistanceValIndex)
            for aNeighbour in tvNeighboursList:
                tvWeightValue = get_weightValue_of_matrixedge(fvAMatrix, tvMinDistanceValIndex, aNeighbour)
                tvTotalWeightOfCurrentNeighbour = tvShortestDistanceList[tvMinDistanceValIndex] + tvWeightValue
                if(tvTotalWeightOfCurrentNeighbour < tvShortestDistanceList[aNeighbour]):
                    tvShortestDistanceList[aNeighbour] = tvTotalWeightOfCurrentNeighbour


    return tvShortestDistanceList










###########################################################################################
######################################__main__#############################################
###########################################################################################


tvGraphNumber = 1
tvAdjecenyMatrix  = WeightedGraph.create_graph_into_adjacency_matrix(tvGraphNumber)
print(tvAdjecenyMatrix)

tvSourceNode = 0
tvshortestPathToAllNodesList = dijkstra_singlesource_shortestdistance(tvAdjecenyMatrix, tvSourceNode)
print(tvshortestPathToAllNodesList)


# tvInDegreeEdgeList  = WeightedGraph.incomingEdgesAMatrix(tvAdjecenyMatrix, 4)
# tvOutDegreeEdgeList = WeightedGraph.neighboursAMatrix(tvAdjecenyMatrix, 4)
# print(tvInDegreeEdgeList, tvOutDegreeEdgeList)

tvAdjecenyList  = WeightedGraph.create_graph_into_adjacency_list(tvGraphNumber)
print(tvAdjecenyList)


# tvInDegreeEdgeList  = WeightedGraph.incomingEdgesAlist(tvAdjecenyList, 4)
# tvOutDegreeEdgeList = WeightedGraph.neighboursAList(tvAdjecenyList, 4)
# print(tvInDegreeEdgeList, tvOutDegreeEdgeList)


print("Completed Sucessfully")
