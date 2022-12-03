import CommonGraph





############################################################################################
########################### Depth First Search(DFS) Startegy ###############################
############################################################################################


# Depth first   -- explores a path till it dies out, then backtrace.

#  Start from i, visit an unexplored neighbour j.
#  Suspend the exploration of i and explore j instead.
#  Continue till you reach a vertex with no unexplored neighbours.
#  Backtrace to the nearest suspend vertex that still has an unexplored neighbour.

# Suspend vertices are stored in a stack
#   Last in, first out
#   Most recently suspended is checked first


def dfs_startegy_for_adjacencyMatrix(fvAMatrix, fV):
    """" Depth First Search Startegy on the Adjacency matrix from given vertix indexs. """

    tvVisited = {}
    (tvRows, tvCols) = fvAMatrix.shape

    # initialization of data structure
    for rowIndex in range(tvCols):
        tvVisited[rowIndex] = False
    
    tvStack = CommonGraph.Stack()


    # start the proceedings with the given input vertix.
    tvVisited[fV] = True
    tvStack.push(fV)


    while(not tvStack.isEmpty()):
        tvCurrProcessing = tvStack.top()
        tvNeighboursList = CommonGraph.neighbours(fvAMatrix, tvCurrProcessing)
        if(len(tvNeighboursList) > 0):
            tvWhetherPushed = False
            for k in tvNeighboursList:
                if(not tvVisited[k]):
                    tvSmallestIndex = k
                    tvVisited[tvSmallestIndex] = True
                    tvStack.push(tvSmallestIndex)
                    tvWhetherPushed = True
                    break
            if(tvWhetherPushed == False):
                tvStack.pop()

        if(len(tvNeighboursList) == 0):
            tvStack.pop()

    return(tvVisited)



























###########################################################################################
######################################__main__#############################################
###########################################################################################


print("Started Successfully")

# CommonGraph.basic_learning_of_stack()
tvAdjecenyMatrix  = CommonGraph.create_graph_into_adjacency_matrix(1)
tvOut = dfs_startegy_for_adjacencyMatrix(tvAdjecenyMatrix, 0)
print(tvOut.__str__())

print("Completed Successfully")
