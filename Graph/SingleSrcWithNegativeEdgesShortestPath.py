# Compute shortest paths from 0(or any edge) to all vertices. There could be edges
# with negative weight value. However negative cycles are not allowed in the graph
# as with this, forverevr looping through it would reduce the path/cost.


# This is also known as Bellman-Ford Algorithm. It is more versatile than Dijkstra's
# algorithm as it work with negative edge as well. However it its complexity is O(n^3)
# as compared to Dijkstra O(n^2).

# Initialization (source vertex 0)
# D(j) : minimum distance known so far to vertex j
# D(j) = 0 if j = 0
#       = infinity, otherwise

# Repeat n-1 times
# for each vertex j  {0,1,....n-1}
#   for each edge (j, k)
#       D(k) = min(D(k) + D(j) + W(j, k))

# This algorithms works for directed as well undirected graph.



import numpy as np
import WeightedGraph




def bellman_ford_moore_singlesource_shortestdistance_initializer(fvAInput, fvShortestDistanceList):
    """ bellman_ford_moore_singlesource_shortestdistance_initializer """

    tvLen = 0
    if( isinstance(fvAInput, dict) == True):
        tvLen = len(fvAInput)
    elif( isinstance(fvAInput, np.ndarray) == True):
        (tvRows, tvCols) = fvAInput.shape
        tvLen = tvRows

    # Initialize all distance from 'fvSourceNode' is very very big number(999999).
    for index in range(0, tvLen):
        fvShortestDistanceList[index] = 999999
        





def bellman_ford_moore_singlesource_shortestdistance(fvAInput, fvSourceNode):
    """ bellman_ford_moore_singlesource_shortestdistance algorithm implementation"""

    tvShortestDistanceDic = {}

    # Initialize all distance from 'fvSourceNode' is very very big number(999999).
    bellman_ford_moore_singlesource_shortestdistance_initializer(fvAInput, tvShortestDistanceDic)

    # Now let's initialze the 'fvSourceNode' shortest distance is 0.
    tvShortestDistanceDic[fvSourceNode] = 0


    for i in range(0, len(tvShortestDistanceDic)):
        
        # Let us see what are known to us after each iteration.
        tvKnownVertexList = []
        for (key,value) in tvShortestDistanceDic.items():
            if(value != 999999):
                tvKnownVertexList.append(key)

        # Now iterate through the known vertex and update if there is minimum value then previous one.
        for knownIndexVal in tvKnownVertexList:
            tvNeighboursList = WeightedGraph.neighbours(fvAInput, knownIndexVal)
            for aNeighbour in tvNeighboursList:
                tvWeightValue = WeightedGraph.get_weightValue(fvAInput, knownIndexVal, aNeighbour)
                tvTotalWeightOfCurrentNeighbour = tvShortestDistanceDic[knownIndexVal] + tvWeightValue

                if(tvTotalWeightOfCurrentNeighbour < tvShortestDistanceDic[aNeighbour]):
                    tvShortestDistanceDic[aNeighbour] = tvTotalWeightOfCurrentNeighbour

    return tvShortestDistanceDic









###########################################################################################
######################################__main__#############################################
###########################################################################################

tvGraphNumber = 2



tvAdjecenyMatrix  = WeightedGraph.create_graph_into_adjacency_matrix(tvGraphNumber)
# print(tvAdjecenyMatrix)
# tvInDegreeEdgeList  = WeightedGraph.incomingEdges(tvAdjecenyMatrix, 1)
# tvOutDegreeEdgeList = WeightedGraph.neighbours(tvAdjecenyMatrix, 1)
# print(tvInDegreeEdgeList, tvOutDegreeEdgeList)

for tvSourceNode in range(0, tvAdjecenyMatrix.shape[0]):
    tvshortestPathToAllNodesAdjancenyMatrixDic = bellman_ford_moore_singlesource_shortestdistance(tvAdjecenyMatrix, tvSourceNode)
    tvLongestPathList = []
    for index in range(0, len(tvshortestPathToAllNodesAdjancenyMatrixDic)):
        tvLongestPathList.append(tvshortestPathToAllNodesAdjancenyMatrixDic[index])

    print("SourceIndex: " + str(tvSourceNode) + " " + str(tvLongestPathList) )



tvAdjecenyList  = WeightedGraph.create_graph_into_adjacency_list(tvGraphNumber)
# print(tvAdjecenyList)
# tvInDegreeEdgeList  = WeightedGraph.incomingEdges(tvAdjecenyList, 5)
# tvOutDegreeEdgeList = WeightedGraph.neighbours(tvAdjecenyList, 5)
# print(tvInDegreeEdgeList, tvOutDegreeEdgeList)

for tvSourceNode in range(0, len(tvAdjecenyList)):
    tvshortestPathToAllNodesAdjancyListDic = bellman_ford_moore_singlesource_shortestdistance(tvAdjecenyList, tvSourceNode)
    print(tvshortestPathToAllNodesAdjancyListDic)

    tvLongestPathList = []
    for index in range(0, len(tvshortestPathToAllNodesAdjancenyMatrixDic)):
        tvLongestPathList.append(tvshortestPathToAllNodesAdjancenyMatrixDic[index])

    print(tvLongestPathList)


print("Completed Sucessfully")
