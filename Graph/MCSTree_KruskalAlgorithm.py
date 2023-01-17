# Kruskal's algorithm finds a minimum spanning forest of an undirected edge-weighted graph. If the graph 
# is connected, it finds a minimum spanning tree. (A minimum spanning tree of a connected graph is a subset 
# of the edges that forms a tree that includes every vertex, where the sum of the weights of all the edges 
# in the tree is minimized. For a disconnected graph, a minimum spanning forest is composed of a minimum 
# spanning tree for each connected component.) 

# It is a greedy algorithm in graph theory as in each step it adds the next lowest-weight edge that will 
# not form a cycle to the minimum spanning forest.


import numpy as np
import WeightedGraph



def sort_based_on_edge_weight_matrix(fvAInput):
    """ sort_based_on_edge_weight_matrix. This list would look like [((source,Index),weight),((1,3),10)] """

    tvNonZeroEdgeList = []

    # Find out the all edges with non zero weight value complete adjacency matrix. It is kind of reverse
    # operation from building the edgeList to Adjacency matrix.
    (tvRows, tvCols) = fvAInput.shape

    for cIndex in range(0, tvCols):
        for rIndex in range(0, tvRows):
            tvCurrCellValue = fvAInput[cIndex, rIndex]
            if( (tvCurrCellValue[0] == 0) ):
                continue
            else:
                tvNonZeroEdgeList.append( ((cIndex, rIndex), tvCurrCellValue[1]) )

    # This is sorting being done based on lambda function which would use the 2nd value of tuple in which we
    # have stored the weight value.
    tvNonZeroEdgeList = sorted(tvNonZeroEdgeList, key=lambda x: x[1])
    return tvNonZeroEdgeList




def sort_based_on_edge_weight_list(fvAInput):
    """"sort_based_on_edge_weight_list """

    tvNonZeroEdgeList = []
    # Find out all nozero edges from all index and then find out the minimum among them.
    for srcIndex in range(len(fvAInput)):
        tvNeighbourList = fvAInput[srcIndex]
        for dstIndex in range(len(tvNeighbourList)):
            tvCurrCellValue = tvNeighbourList[dstIndex]
            if( (tvCurrCellValue[0] == 0) ):
                continue
            else:
                tvNonZeroEdgeList.append( ((srcIndex, tvCurrCellValue[0]), tvCurrCellValue[1]) )

    # This is sorting being done based on lambda function which would use the 2nd value of 
    # tuple in which we have stored the weight value.
    tvNonZeroEdgeList = sorted(tvNonZeroEdgeList, key = lambda x: x[1])
    return tvNonZeroEdgeList






def miminimum_cost_spanning_tree_kruskal_algorithm(fvAInput):
    """miminimum_cost_spanning_tree_kruskal_algorithm"""

    tvEdgeList       = []
    tvTotalCostValue = 0

    tvSortedEdgesList = []
    tvComponentList   = { }
    tvLen = 0


    # Get the outerloop to execute iteration and also minimum edges to begin with.
    if( isinstance(fvAInput, dict) == True):
        tvSortedEdgesList = sort_based_on_edge_weight_list(fvAInput)
        tvLen = len(fvAInput)
    elif( isinstance(fvAInput, np.ndarray) == True):
        tvSortedEdgesList = sort_based_on_edge_weight_matrix(fvAInput)
        (tvRows, tvCols) = fvAInput.shape
        tvLen = tvRows
    

    # Initialize the component number for each vertex.
    for index in range(0, tvLen):
        tvComponentList[index] = index 
    


    for tvMinCellValue in tvSortedEdgesList:
        tvSrcIndex  = tvMinCellValue[0][0]
        tvDestIndex = tvMinCellValue[0][1]
        tvWeightVal = tvMinCellValue[1]
                
        # Now check about component numbers of 'tvSrcIndex' & 'tvDestIndex'
        if( (tvComponentList[tvSrcIndex]) != (tvComponentList[tvDestIndex]) ):
            tvEdgeList.append(tvMinCellValue[0])
            tvTotalCostValue = tvTotalCostValue + tvWeightVal

            # Merge the components numbers appropritely. Store 'tvSrcIndex' component number value
            # and scan in the entire tvComponentList to find all values with 'tvSrcIndex' component
            # number and update it with component number with 'tvDestIndex'
            
            # For Grpah#3, Below is how components numbers gets updated and eventually converge to
            # 4 for all indices.
            # tvComponentList {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
            # tvComponentList {0: 0, 1: 2, 2: 2, 3: 3, 4: 4}
            # tvComponentList {0: 0, 1: 2, 2: 2, 3: 4, 4: 4}
            # tvComponentList {0: 2, 1: 2, 2: 2, 3: 4, 4: 4}
            # tvComponentList {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
            # ...
            # ...
            # tvComponentList {0: 4, 1: 4, 2: 4, 3: 4, 4: 4}
            tvCValue = tvComponentList[tvSrcIndex]
            for index in range(0, len(tvComponentList) ):
                if(tvComponentList[index] == tvCValue):
                    tvComponentList[index] = tvComponentList[tvDestIndex]


    return (tvEdgeList, tvTotalCostValue)









###########################################################################################
######################################__main__#############################################
###########################################################################################

tvGraphNumberList = [3, 4]

for tvGraphNumber in tvGraphNumberList:
    tvAdjecenyMatrix  = WeightedGraph.create_graph_into_adjacency_matrix(tvGraphNumber)
    tvMatOutput = miminimum_cost_spanning_tree_kruskal_algorithm(tvAdjecenyMatrix)
    print(tvMatOutput[0])
    print(tvMatOutput[1])


    tvAdjecenyList  = WeightedGraph.create_graph_into_adjacency_list(tvGraphNumber)
    tvListOutput = miminimum_cost_spanning_tree_kruskal_algorithm(tvAdjecenyList)
    print(tvListOutput[0])
    print(tvListOutput[1])

print("Completed Sucessfully")
