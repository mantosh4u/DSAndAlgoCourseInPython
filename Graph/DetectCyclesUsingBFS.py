"""How to algorithmically identify whether graph does contains cycles or acycles. For this,
we need to create some sort of tree from the given graph. Post that we need to check whether
there are some edge left in the graph while creating the tree. If this is the case, then graph
does have cycles. Otherwise graph does not have cyclers.  For this, we can either use BFS or DFS.
"""

""" How to algorithmically indentify whether graph is connected or not. Here component 
number represents the maximum subsets of vertices that are connected. """


import CommonGraph

gComponentNumber        = {}
gCurrentComponentNumber = 0
gNonTreeEdgesList       = []




def bfs_startegy_for_adjacencyMatrix_connectivitycheck_helper(fvAMatrix, fV):
    """Helper method for the main implementation."""

    global gComponentNumber
    global gCurrentComponentNumber
    global gNonTreeEdgesList


    tvQueue = CommonGraph.Queue()

    # start the proceedings with the given input vertix. The initial value would be 0.
    gComponentNumber[fV] = gCurrentComponentNumber
    tvQueue.addq(fV)


    while(not tvQueue.isEmpty()):
        tvCurrProcessing = tvQueue.delq()
        tvNeighboursList = CommonGraph.neighboursAMatrix(fvAMatrix, tvCurrProcessing)
        for k in tvNeighboursList:
            if(gComponentNumber[k] == -1):
                gComponentNumber[k] = gCurrentComponentNumber
                tvQueue.addq(k)
            else:
                # store these edges as they would not be part of tree as they got skipped.
                gNonTreeEdgesList.append((tvCurrProcessing, k))





def bfs_startegy_for_adjacencyMatrix_connectivitycheck(fvAMatrix):
    """" Assign each vertex a component number & start BFS/DFS from vertex 0.
        Initialize component number to 0. Now as usual BFS/DFS starts executing. Post
        that see if we have got any unvisited vertex and if there is pick the smallest
        and run BFS/DFS on that particular vertex. This time increment component number
        by 1. This way we need to run the BFS/DFS until there is no unvisited vertex left.
        Post that there would be component number for each vertex and based on that we can
        determine whether graph is connected or disconnected one. If there is only one component
        number for all vertix then graph is connected and if there is more that one component
        number then graph is disconnected. With this we can also identify number of connecte

        This is what we need to implement in this alogrithm. """

    global gComponentNumber
    global gCurrentComponentNumber


    (tvRows, tvCols) = fvAMatrix.shape

    # initialization of data structure
    for rowIndex in range(tvCols):
        gComponentNumber[rowIndex] = -1


    tvStartIndex = 0
    while True:
        bfs_startegy_for_adjacencyMatrix_connectivitycheck_helper(tvAdjecenyMatrix, tvStartIndex)
        # reset to 0 as we would be rely upon this value to find out whether to proceed or not.
        tvStartIndex = 0
        tvSortedKeyList = sorted(gComponentNumber.keys())
        for aKey in tvSortedKeyList[1:]:
            if ( gComponentNumber[aKey] == -1 ):
                tvStartIndex = aKey
                gCurrentComponentNumber += 1
                break
        
        if(tvStartIndex == 0):
            break






def check_whether_graph_acyclic():
    """In case there is non tree edge present while exploring the graph,
    those are the reason of cycle in the graph. In case there is none, then
    graph does not not have any cycle. """

    global gNonTreeEdgesList

    tvLen = len(gNonTreeEdgesList)
    if(tvLen == 0):
        print("Current graph does not have any cycle")
    else:
        print("Current graph seems to have " + str(tvLen) + " cycle")




###########################################################################################
######################################__main__#############################################
###########################################################################################
tvAdjecenyMatrix  = CommonGraph.create_graph_into_adjacency_matrix(5)
bfs_startegy_for_adjacencyMatrix_connectivitycheck(tvAdjecenyMatrix)


# check out in case graph does have cycles and whats the sequence of that cycle.
check_whether_graph_acyclic()

print("Completed Successfully")
