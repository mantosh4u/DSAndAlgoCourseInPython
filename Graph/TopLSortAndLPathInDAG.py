# A vertex with no dependencies has no incoming edges indegree(v) = 0
# Every DAG has a vertex with indegree 0
# Start with any vertex with indegree(v) = 0 and then remove that vertex
# and post that update the all other remaining vertex indegree(v) and then
# start with other vertex with 0 indegree(v)

# This is the esence of the toplogical sorting of a DAG graph. There could be
# multiple solution for the same graph.

# Along with this, we need to update longest path of that particular node.
# longest-path-to(ik) = 1 + max{longest-path-to(ij)}


import CommonGraph


gVertexToIndegreeVal = {}




##################################
# Adjacency Matrix Based Alogrithm
##################################

def calculate_and_print_indegree_of_matrix(fvAMatrix):
    """ calculate_and_print_indegree_of_matrix """

    global gVertexToIndegreeVal
    
    (tvRows, tvCols) = fvAMatrix.shape

    if(len(gVertexToIndegreeVal) != 0):
        gVertexToIndegreeVal = {}

    for rowIndex in range(tvCols):
        tvIndegreeVal = CommonGraph.indegreeVal(fvAMatrix, rowIndex)
        # print(str(rowIndex) + ": " + str(tvIndegreeVal))
        gVertexToIndegreeVal[rowIndex] = tvIndegreeVal


    # for k in sorted(gVertexToIndegreeVal, key = gVertexToIndegreeVal.get):
    #     print(k, gVertexToIndegreeVal[k])

    

################################
# Adjacency List Based Alogrithm
################################

def calculate_and_print_indegree_of_list(fvAList):
    """ calculate_and_print_indegree_of_list """

    global gVertexToIndegreeVal

    if(len(gVertexToIndegreeVal) != 0):
        gVertexToIndegreeVal = {}

    for i in range(len(fvAList)):
        gVertexToIndegreeVal[i] = 0


    for i in range(len(fvAList)):
        tvCurrentIndexNeighbourList = CommonGraph.neighbours(fvAList, i)
        for aNeighbour in range(len(tvCurrentIndexNeighbourList)):
            # if present get current value and then increment by one.
            aNeighbourVertexIndexValue = tvCurrentIndexNeighbourList[aNeighbour]
            gVertexToIndegreeVal[aNeighbourVertexIndexValue] = gVertexToIndegreeVal[aNeighbourVertexIndexValue] + 1

  




def perform_toplogicalsorting_and_longest_path_of_matrix_or_list(fvAdjacency):
    """ perform_toplogicalsorting_and_longest_path_of_matrix_or_list"""

    global gVertexToIndegreeVal

    tvToplogicalSortedList = []
    tvLongestPathList      = {}

    # check in case we can perform topological sorting on this graph.
    if( 0 not in list(gVertexToIndegreeVal.values()) ):
        return (tvToplogicalSortedList, tvLongestPathList)
    
    # check and queue all '0' in-degree nodes from graph. Also initialize longest path for each
    # node to '0'.
    tvZeroDegreeQueue = CommonGraph.Queue()
    for key, value in gVertexToIndegreeVal.items():
        if(value == 0):
            tvZeroDegreeQueue.addq(key)
        tvLongestPathList[key]= 0


    # start processing the queue
    while (not tvZeroDegreeQueue.isEmpty()):
        tvCurrProcessing = tvZeroDegreeQueue.delq()
        tvToplogicalSortedList.append(tvCurrProcessing)
        gVertexToIndegreeVal[tvCurrProcessing]= gVertexToIndegreeVal[tvCurrProcessing] - 1

        # # This is not required
        # # This place, we need to require to put the logic for longest path for each node.
        # if(tvLongestPathList[tvCurrProcessing] == 0):
        #     tvLongestPathList[tvCurrProcessing] = 0

        tvNeighboursList = []
        tvNeighboursList = CommonGraph.neighbours(fvAdjacency, tvCurrProcessing)
        
        for aNeighbour in tvNeighboursList:
            gVertexToIndegreeVal[aNeighbour] =  gVertexToIndegreeVal[aNeighbour] - 1
            # check in case there is 0 in-degree nodes after updating it and store it into queue.
            if(gVertexToIndegreeVal[aNeighbour] == 0):
                tvZeroDegreeQueue.addq(aNeighbour)
            
            # Get max value in all incoming edges current longest distance
            tvIncomingEdgesList = []
            tvIncomingEdgesList = CommonGraph.incomingEdges(fvAdjacency, aNeighbour)
            
            tvIncomingEdgesLongestDistanceList = []
            for edgeIndex in tvIncomingEdgesList:
                tvIncomingEdgesLongestDistanceList.append(tvLongestPathList[edgeIndex])

            tvMaxDistanceValue = 0
            if(len(tvIncomingEdgesLongestDistanceList) != 0):
                tvMaxDistanceValue = max(tvIncomingEdgesLongestDistanceList)

            # Update all the neighbours of 'tvCurrProcessing' by 1. Below is not required as in case
            # current edges does not have any incoming edges(indegree 0), then 'tvMaxDistanceValue'value
            # would be 0 anyway.

            # tvLongestPathList[aNeighbour] = tvLongestPathList[aNeighbour] + 1
            tvLongestPathList[aNeighbour] = tvMaxDistanceValue + 1           



    return (tvToplogicalSortedList, tvLongestPathList)






###########################################################################################
######################################__main__#############################################
###########################################################################################

tvGraphNumberList = [1,2,3,4,5]
for tvGraphNumber in tvGraphNumberList:
    print(">> " + str(tvGraphNumber))
    # Topological Sorting Using Adjacency List
    tvAdjecenyList  = CommonGraph.create_graph_into_adjacency_list(tvGraphNumber)
    calculate_and_print_indegree_of_list(tvAdjecenyList)
    tvOutput = perform_toplogicalsorting_and_longest_path_of_matrix_or_list(tvAdjecenyList)
    tvTopologicalListSortList = tvOutput[0]
    tvLongestPathDic = tvOutput[1]

    print(tvTopologicalListSortList)
    tvLongestPathList = []
    for aSingleNode in tvTopologicalListSortList:
        tvLongestPathList.append(tvLongestPathDic[aSingleNode])

    print(tvLongestPathList)

    print("<< " + str(tvGraphNumber))





# print(" >> Adjacency List")
# for index in range(len(tvAdjecenyList)):
#     tvIncomingEdgesList = CommonGraph.incomingEdges(tvAdjecenyList, index)
#     print("For Index: " + str(index) + ", IncomingEdge List is: " + str(tvIncomingEdgesList))
   
#     tvNeighBoursList = CommonGraph.neighbours(tvAdjecenyList, index) 
#     print("For Index: " + str(index) + ", OutgoingEdge List is: " + str(tvNeighBoursList))
# print(" << Adjacency List")


# # Topological Sorting Using Adjacency List
# tvAdjecenyMatrix  = CommonGraph.create_graph_into_adjacency_matrix(tvGraphNumber)
# calculate_and_print_indegree_of_matrix(tvAdjecenyMatrix)
# (tvRows, tvCols) = tvAdjecenyMatrix.shape

# print(" >> Adjacency Matrix")
# for rowIndex in range(tvRows):
#     tvIncomingEdgesList = CommonGraph.incomingEdges(tvAdjecenyMatrix, rowIndex)
#     print("For Index: " + str(rowIndex) + ", IncomingEdge List is: " + str(tvIncomingEdgesList))
   
#     tvNeighBoursList = CommonGraph.neighbours(tvAdjecenyMatrix, rowIndex) 
#     print("For Index: " + str(rowIndex) + ", OutgoingEdge List is: " + str(tvNeighBoursList))
# print(" << Adjacency Matrix")

print("Completed Successfully")




