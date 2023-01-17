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
    tvParent  = {}

    (tvRows, tvCols) = fvAMatrix.shape

    # initialization of data structure
    for rowIndex in range(tvCols):
        tvVisited[rowIndex] = False
        tvParent[rowIndex]  = -1
    
    tvStack = CommonGraph.Stack()


    # start the proceedings with the given input vertix.
    tvVisited[fV] = True
    tvStack.push(fV)
    tvParent[fV] = -1


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
                    tvParent[k] = tvCurrProcessing
                    tvWhetherPushed = True
                    break
            # This one to take care when a node does have neighbours but all of them has
            # been visited already. In that case, we need to pop the top element from the stack.
            if(tvWhetherPushed == False):
                tvStack.pop()
        # This one is to take care when a node does not have neighbours at all. So we need to 
        # process next element from the stack. Without this, we would have stuck infinitely as
        # there would have been some node in the stack.
        elif(len(tvNeighboursList) == 0):
            tvStack.pop()

    return(tvVisited, tvParent)








###########################################################################################
######################################__main__#############################################
###########################################################################################

print("Started Successfully")


# CommonGraph.basic_learning_of_stack()
tvAdjecenyMatrix  = CommonGraph.create_graph_into_adjacency_matrix(2)
tvStartIndex  = 4
tvOut = dfs_startegy_for_adjacencyMatrix(tvAdjecenyMatrix, tvStartIndex)
print(tvOut.__str__())


#####################################################################################################
# Now record the path of vertix 7 from each node like (1-->0-->4-->7)
parentDic             = tvOut[1]
tvVertixToPathListDic = {}
tvDst                 = tvStartIndex

for vertixIndex in range(0, len(parentDic)):
    tvSrc = vertixIndex
    tvPathList = []
    tvPathList.append(tvSrc)    
    while True:
        if(tvSrc in parentDic):
            tvSrcParent = parentDic[tvSrc]
            if(tvSrcParent == -1):
                break
            tvPathList.append(tvSrcParent)
            if(tvSrcParent == tvDst):
                break
            else:
                tvSrc = tvSrcParent

    tvVertixToPathListDic[vertixIndex] = tvPathList

for item in sorted(tvVertixToPathListDic.keys()):
    print("Path Between " + str(item) + " & " + str(tvDst) + " is:" + str(tvVertixToPathListDic[item]))

########################################################################################################


print("Completed Successfully")
