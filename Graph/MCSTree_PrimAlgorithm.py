# In computer science, Prim's algorithm (also known as Jarník's algorithm) is a greedy algorithm that 
# finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the 
# edges that forms a tree that includes every vertex, where the total weight of all the edges in the 
# tree is minimized. The algorithm operates by building this tree one vertex at a time, from an 
# arbitrary starting vertex, at each step adding the cheapest possible connection from the tree 
# to another vertex.


import numpy as np
import WeightedGraph




def minimum_edge_find_matrix(fvAInput):
    """"minimum_edge_find_matrix """

    # Find out the smallest edge in complete adjacency matrix
    (tvRows, tvCols) = fvAInput.shape

    tvMinCellValue = ((0,0),0)
    tvInitialize   = True

    for cIndex in range(0, tvCols):
        for rIndex in range(0, tvRows):
            tvCurrCellValue = fvAInput[cIndex, rIndex]
            if( (tvCurrCellValue[0] == 0) ):
                continue
            else:
                if(tvInitialize == True):
                    tvMinCellValue = ((cIndex, rIndex), tvCurrCellValue[1])
                    tvInitialize = False
                elif (tvCurrCellValue[1] < tvMinCellValue[1]):
                    tvMinCellValue = ((cIndex, rIndex), tvCurrCellValue[1])

    return tvMinCellValue





def minimum_edge_find_list(fvAInput):
    """"minimum_edge_find_list """

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
    return tvNonZeroEdgeList[0]






def miminimum_cost_spanning_tree_prim_algorithm(fvAInput):
    """miminimum_cost_spanning_tree_prim_algorithm"""

    tvVertexList     = []
    tvEdgeList       = []
    tvTotalCostValue = 0

    tvMinEdgeValue = None
    tvLen = 0
    
    # Get the outerloop to execute iteration and also minimum edges to begin with.
    if( isinstance(fvAInput, dict) == True):
        tvLen = len(fvAInput) -2
        tvMinEdgeValue = minimum_edge_find_list(fvAInput)
    elif( isinstance(fvAInput, np.ndarray) == True):
        (tvRows, tvCols) = fvAInput.shape
        tvLen = tvRows -2
        tvMinEdgeValue = minimum_edge_find_matrix(fvAInput)
    

    tvMinEdgeList  = tvMinEdgeValue[0]
    tvMinWeightVal = tvMinEdgeValue[1]

    tvVertexList.append(tvMinEdgeList[0])
    tvVertexList.append(tvMinEdgeList[1])
    tvEdgeList.append(tvMinEdgeList)
    tvTotalCostValue = tvMinWeightVal


    # Now we need to loop through until we have complete vertex in the list.
    # Also we need to ensure that there is no looping. Until then we need to find
    # neighbours and see if they are ok to be added in minimum cost spanning tree.
    for i in range(0, tvLen):
        tvNeighboursIndexWeightList = []
        for aVertexIndex in tvVertexList:
            tvNeighboursList = WeightedGraph.neighbours(fvAInput, aVertexIndex)
            for aNeighbour in tvNeighboursList:
                tvWeightValue = WeightedGraph.get_weightValue(fvAInput, aVertexIndex, aNeighbour)
                tvNeighboursIndexWeightList.append(((aVertexIndex, aNeighbour),tvWeightValue))

        # Out of tvNeighboursIndexWeightList, we need to select the ones with minimum value and 
        # also which does not form the cycles.
        if(len(tvNeighboursIndexWeightList) == 0):
            continue
        else:
            # This is sorting being done based on lambda function which would use the 2nd value of tuple in which we
            #  have stored the weight value.
            tvNeighboursIndexWeightList = sorted(tvNeighboursIndexWeightList, key = lambda x: x[1])
            for tvMinCellValue in tvNeighboursIndexWeightList:
                tvSrcIndex  = tvMinCellValue[0][0]
                tvDestIndex = tvMinCellValue[0][1]
                tvWeightVal = tvMinCellValue[1]
                
                tvIsSourceIndex = tvSrcIndex in tvVertexList
                tvIsDestIndex   = tvDestIndex in tvVertexList
                # These index edges would create a cycle so need to skip them.
                if( tvIsSourceIndex and tvIsDestIndex ):
                    continue
                else:
                    # We need to break the loop to find out the updated tvNeighboursIndexWeightList as there has been
                    # newer index being added. This is all about greedy approach.
                    if(tvIsSourceIndex == False):
                        tvVertexList.append(tvSrcIndex)
                    if(tvIsDestIndex == False):
                        tvVertexList.append(tvDestIndex)
                    tvEdgeList.append(tvMinCellValue[0])
                    tvTotalCostValue = tvTotalCostValue + tvWeightVal
                    break

            

    return ( (tvVertexList,tvEdgeList), tvTotalCostValue)





###########################################################################################
######################################__main__#############################################
###########################################################################################

tvGraphNumberList = [3, 4]
for tvGraphNumber in tvGraphNumberList:
    tvAdjecenyMatrix  = WeightedGraph.create_graph_into_adjacency_matrix(tvGraphNumber)
    tvMatOutput = miminimum_cost_spanning_tree_prim_algorithm(tvAdjecenyMatrix)
    print(tvMatOutput[0])
    print(tvMatOutput[1])


    tvAdjecenyList  = WeightedGraph.create_graph_into_adjacency_list(tvGraphNumber)
    tvListOutput = miminimum_cost_spanning_tree_prim_algorithm(tvAdjecenyList)
    print(tvListOutput[0])
    print(tvListOutput[1])

print("Completed Sucessfully")
