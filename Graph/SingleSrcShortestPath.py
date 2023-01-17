# Compute shortest paths from 0(or any edge) to all vertices.

# Practical Example:
# Transport finished product from factory(single source) to all retail outlets.
# Courier company delivers items from distribution center(single source) to addresses.

# This is also known as Dijkstra's Algorithm. One of the best algorithms ever designed.



# Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a
# graph, which may represent, for example, road networks. It was conceived by computer 
# scientist Edsger W. Dijkstra in 1956 and published three years later.

# The algorithm exists in many variants. Dijkstra's original algorithm found the shortest 
# path between two given nodes,[6] but a more common variant fixes a single node as the 
# "source" node and finds shortest paths from the source to all other nodes in the graph, 
# producing a shortest-path tree.





import numpy as np
import WeightedGraph




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







def dijkstra_singlesource_shortestdistance(fvAInput, fvSourceNode):
    """ dijkstra_singlesource_shortestdistance """

    tvShortestDistanceList = []
    tvVisitedList          = []

    # Initialize all distance from 'fvSourceNode' is very very big number(999999).
    dijkstra_singlesource_shortestdistance_initializer(fvAInput, tvShortestDistanceList, tvVisitedList)

    # Now let's initialze the 'fvSourceNode' shortest distance is 0. Its so simple!!
    tvShortestDistanceList[fvSourceNode] = 0
    tvVisitedList[fvSourceNode] = True

    tvNeighboursList = WeightedGraph.neighbours(fvAInput, fvSourceNode)
    for aNeighbour in tvNeighboursList:
        tvWeightValue = WeightedGraph.get_weightValue(fvAInput, fvSourceNode, aNeighbour)
        tvShortestDistanceList[aNeighbour] = tvWeightValue


    # Loop until we have some finite value in tvShortestDistanceList
    while True:
        tvMinDistanceValIndex = min_value_index(tvShortestDistanceList, tvVisitedList)
        if(tvMinDistanceValIndex == -1):
            break
        else:
            tvVisitedList[tvMinDistanceValIndex] = True
            tvNeighboursList = WeightedGraph.neighbours(fvAInput, tvMinDistanceValIndex)
            for aNeighbour in tvNeighboursList:
                tvWeightValue = WeightedGraph.get_weightValue(fvAInput, tvMinDistanceValIndex, aNeighbour)
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
