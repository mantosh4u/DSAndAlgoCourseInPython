"""How to algorithmically identify whether graph does contains cycles or acycles. For this,
we need to create some sort of tree from the given graph. Post that we need to check whether
there are some edge left in the graph while creating the tree. If this is the case, then graph
does have cycles. Otherwise graph does not have cyclers.  For this, we can either use BFS or DFS.
"""

import CommonGraph


gVisited                = {}
gPreAndPostNumber       = {}
gCurrentStepNumber      = 0
gComponentNumber        = {}
gCurrentComponentNumber = 0



def dfs_startegy_for_adjacencyMatrix(fvAMatrix, fV):
    """" Depth First Search Startegy on the Adjacency matrix from given vertix indexs. """
    
    global gVisited, gPreAndPostNumber, gCurrentStepNumber, gComponentNumber, gCurrentComponentNumber
    
    
    tvStack = CommonGraph.Stack()
    # start the proceedings with the given input vertix.
    gVisited[fV] = True
    gComponentNumber[fV] = gCurrentComponentNumber
    tvStack.push(fV)


    while(not tvStack.isEmpty()):
        tvCurrProcessing = tvStack.top()
        gComponentNumber[tvCurrProcessing] = gCurrentComponentNumber

        if (gPreAndPostNumber[tvCurrProcessing]['pre'] == -1):
            gPreAndPostNumber[tvCurrProcessing]['pre'] = gCurrentStepNumber
            gCurrentStepNumber = gCurrentStepNumber + 1
        
        tvNeighboursList = CommonGraph.neighboursAMatrix(fvAMatrix, tvCurrProcessing)
        if(len(tvNeighboursList) > 0):
            tvWhetherPushed = False
            for k in tvNeighboursList:
                if(not gVisited[k]):
                    tvSmallestIndex = k
                    gVisited[tvSmallestIndex] = True
                    tvStack.push(tvSmallestIndex)
                    tvWhetherPushed = True
                    break
            # This one to take care when a node does have neighbours but all of them has
            # been visited already. In that case, we need to pop the top element from the stack.
            if(tvWhetherPushed == False):
                
                if (gPreAndPostNumber[tvCurrProcessing]['post'] == -1):
                    gPreAndPostNumber[tvCurrProcessing]['post'] = gCurrentStepNumber
                    gCurrentStepNumber = gCurrentStepNumber + 1
                
                tvStack.pop()
        
        # This one is to take care when a node does not have neighbours at all. So we need to 
        # process next element from the stack. Without this, we would have stuck infinitely as
        # there would have been some node in the stack.
        elif(len(tvNeighboursList) == 0):
        
            if (gPreAndPostNumber[tvCurrProcessing]['post'] == -1):
                gPreAndPostNumber[tvCurrProcessing]['post'] = gCurrentStepNumber
                gCurrentStepNumber = gCurrentStepNumber + 1
            
            tvStack.pop()





def dfs_startegy_for_adjacencyMatrix_connectivitycheck(fvAMatrix):
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

    global gVisited, gPreAndPostNumber, gCurrentStepNumber, gComponentNumber, gCurrentComponentNumber


    (tvRows, tvCols) = fvAMatrix.shape

    # initialization of data structure
    for rowIndex in range(tvCols):
        gVisited[rowIndex] = False
        gPreAndPostNumber[rowIndex] = {'pre':-1, 'post':-1}
        gComponentNumber[rowIndex] = -1

    tvStartIndex = 0
    while True:
        dfs_startegy_for_adjacencyMatrix(tvAdjecenyMatrix, tvStartIndex)
        # reset to 0 as we would be rely upon this value to find out whether to proceed or not.
        tvStartIndex = 0
        tvSortedKeyList = sorted(gVisited.keys())
        for aKey in tvSortedKeyList[1:]:
            if ( gVisited[aKey] == False ):
                tvStartIndex = aKey
                gCurrentComponentNumber += 1
                break
        if(tvStartIndex == 0):
            break



def printDfsTree():
    """"print DFS Tree with component number as cateogory"""

    global gPreAndPostNumber, gComponentNumber


    # check out in case graph is connected or disconnected.
    tvUniqueComponentNumberList = []
    for aKey in sorted(gComponentNumber.keys()):
        tvComponentNumber = gComponentNumber[aKey]
        if(tvComponentNumber not in tvUniqueComponentNumberList):
            tvUniqueComponentNumberList.append(tvComponentNumber)


    tvComponentIdToVertexDic = {}
    for index in range(len(tvUniqueComponentNumberList)):
        tvComponentIdToVertexDic[index] = []
    

    for key,value in gComponentNumber.items():
        # print(key,value)
        tvComponentIdToVertexDic[value].append(key)


    for key, value in tvComponentIdToVertexDic.items():
        print("Component Number: " + str(key))
        for aNode in value:
            print("Vertex: " + str(aNode) + " with pre: " + str(gPreAndPostNumber[aNode]['pre']) + " & post: " + str(gPreAndPostNumber[aNode]['post']) )




###########################################################################################
######################################__main__#############################################
###########################################################################################


tvAdjecenyMatrix  = CommonGraph.create_graph_into_adjacency_matrix(5)
dfs_startegy_for_adjacencyMatrix_connectivitycheck(tvAdjecenyMatrix)

# print pre and post number of each vertex based on current component number. So we would be
# relying upon the pre and post number and component number.
printDfsTree()


print("Completed Successfully")
