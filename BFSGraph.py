import CommonGraph



############################################################################################
########################### Breadth First Search(BFS) Startegy #############################
############################################################################################


# Breadth first -- propagate marks in "layers".
# Depth first   -- explores a path till it dies out, then backtrace.

# comparing representations between adjacency matrix and adjacney list.
#   Adjacency list typically requires less space.
#   Is j a neighbour of i ?
#       check if A[i,i] == 1 in adjacency matrix
#       scan all neighbours of i in adjacency list

#   which are the neighbours of i?
#   scan all n entries in row i in adjacency matrix
#   takes times proportional to (out) degree of i in adjaency list



# To operate on graphs, we need  to represent them
# Ajacency matrix
#   n X n matrix  AMat[i,j] =  1 if (i,j) (- E
# Ajacency list
#   Dictionary of lists
#   For each vertex i, AList[i] is the list of neighbour of i





# Explore the graph level by level
#   First visit vertices one step away
#   Then two steps away
#   .......

# Each visited vertex has to be explored.











def bfs_startegy_for_adjacencyMatrix(fvAMatrix, fV):
    """" Breadth First Search Startegy on the Adjacency matrix from given vertix indexs.
    Exploring a vertex i
      For each edge (i,j), if visited(j) is False
          Set visited(j) to True
          Append j to the queue

    This is what we need to implement in this alogrithm. """

    tvVisited = {}
    (tvRows, tvCols) = fvAMatrix.shape

    # initialization of data structure
    for rowIndex in range(tvCols):
        tvVisited[rowIndex] = False
    
    tvQueue = CommonGraph.Queue()


    # start the proceedings with the given input vertix.
    tvVisited[fV] = True
    tvQueue.addq(fV)


    while(not tvQueue.isEmpty()):
        tvCurrProcessing = tvQueue.delq()
        tvNeighboursList = CommonGraph.neighbours(fvAMatrix, tvCurrProcessing)
        for k in tvNeighboursList:
            if(not tvVisited[k]):
                tvVisited[k] = True
                tvQueue.addq(k)

    return(tvVisited)












def bfs_startegy_for_adjacencyList(fvAList, fV):
    """" Breadth First Search Startegy on the Adjacency list from given vertix indexs.
    Exploring a vertex i
      For each edge (i,j), if visited(j) is False
          Set visited(j) to True
          Append j to the queue

    This is what we need to implement in this alogrithm. """

    tvVisited = {}
    tvParent  = {}

    # initialization of data structure
    for rowIndex in  fvAList.keys():
        tvVisited[rowIndex] = False
        tvParent[rowIndex]  =  -1
    
    
    tvQueue = CommonGraph.Queue()


    # start the proceedings with the given input vertix.
    tvVisited[fV] = True
    tvQueue.addq(fV)


    while(not tvQueue.isEmpty()):
        tvCurrProcessing = tvQueue.delq()
        tvNeighboursList = fvAList[tvCurrProcessing]
        for k in tvNeighboursList:
            if(not tvVisited[k]):
                tvVisited[k] = True
                tvParent[k] = tvCurrProcessing
                tvQueue.addq(k)

    return(tvVisited, tvParent)








def bfs_startegy_for_adjacencyList_levelcalculation(fvAList, fV):
    """" Breadth First Search Startegy on the Adjacency list from given vertix indexs.
    Exploring a vertex i
      For each edge (i,j), if visited(j) is False
          Set visited(j) to True
          Append j to the queue

    This is what we need to implement in this alogrithm. """

    tvLeval  = {}
    tvParent  = {}

    # initialization of data structure
    for rowIndex in  fvAList.keys():
        tvLeval[rowIndex]   = -1
        tvParent[rowIndex]  =  -1
    
    
    tvQueue = CommonGraph.Queue()


    # start the proceedings with the given input vertix.
    tvLeval[fV] = 0
    tvQueue.addq(fV)


    while(not tvQueue.isEmpty()):
        tvCurrProcessing = tvQueue.delq()
        tvNeighboursList = fvAList[tvCurrProcessing]
        for k in tvNeighboursList:
            if(tvLeval[k] == -1) :
                tvLeval[k] = tvLeval[tvCurrProcessing] + 1
                tvParent[k] = tvCurrProcessing
                tvQueue.addq(k)

    return(tvLeval, tvParent)








###########################################################################################
######################################__main__#############################################
###########################################################################################


print("Started Successfully")

tvAdjecenyMatrix  = CommonGraph.create_graph_into_adjacency_matrix(2)

# CommonGraph.basic_learning_of_queue()
# CommonGraph.neighbours(tvAdjecenyMatrix, 6)
# CommonGraph.neighbours(tvAdjecenyMatrix, 7)


tvOut = bfs_startegy_for_adjacencyMatrix(tvAdjecenyMatrix, 7)
print(tvOut.__str__())


# vAdjecenyList  = CommonGraph.create_graph_into_adjacency_list(1)
# tvOut = bfs_startegy_for_adjacencyList(tvAdjecenyList, 2)
# print(tvOut.__str__())
# tvOut = bfs_startegy_for_adjacencyList_levelcalculation(tvAdjecenyList, 2)
# print(tvOut.__str__())

print("Completed Successfully")
