# Compute shortest paths from each edge to to all vertices. There could be edges
# with negative weight value. However negative cycles are not allowed in the graph
# as with this, forverevr looping through it would reduce the path/cost.

# This alogrithms gets used in travelling stuff where customer wants to know minimum
# distance between each vertex. his is also known as Floyd-Warshall Algorithm. It is 
# more versatile than Dijkstra's or Bellman-Ford algorithm as it finds out all vertex 
# shortest path combination.

# This algorithms works for directed as well undirected graph.

# In computer science, the Floyd–Warshall algorithm (also known as Floyd's algorithm, the 
# Roy–Warshall algorithm, the Roy–Floyd algorithm, or the WFI algorithm) is an algorithm for 
# finding shortest paths in a directed weighted graph with positive or negative edge weights 
# (but with no negative cycles).[1][2] A single execution of the algorithm will find the lengths 
# (summed weights) of shortest paths between all pairs of vertices. Although it does not return 
# details of the paths themselves, it is possible to reconstruct the paths with simple modifications
# to the algorithm. Versions of the algorithm can also be used for finding the transitive closure 
# of a relation.



import numpy as np
import WeightedGraph



# Below is output of this algorithm. Each row represents the shortest
# path between that particular vertex to each vertex. For an example,
# 0 row represents shortest path between 0th vertex to each other vertex.
# This is same as single source shortest path problem and output should be same
# as previous one. Similarly 1th row represents shortest path between 1st vertex to
# all remaining vertex. Any big number(infinity) means that there is no shortest path
# possible(exists) between those vertices.


# Output
#-------

#      0     1    2    3    4    5    6    7     
# 0:  [999    5    5    6    9    7    9    8 ]
# 1:  [999    1    0    1    4    2  999  999 ]
# 2:  [999    1    1    1    4    3  999  999 ]
# 3:  [999    1    0    1    3    2  999  999 ]
# 4:  [996   -2   -3   -2    1   -1  996  996 ]
# 5:  [997   -1   -2   -1    2    1  997  997 ]
# 6:  [995   -4   -4   -3    0   -2  995  995 ]
# 7:  [996   -3   -3   -2    1   -1    1  996 ]




def floyd_warshall_allpair_shortest_distance(fvAInput):
    """ floyd_warshall_allpair_shortest_distance """

    # I kind of borrowed it from sir lectures as I did not understood it completely!!!

    (tvRows, tvCols) = fvAInput.shape
    
    tvSP = np.zeros(shape = (tvRows, tvCols, tvCols+1))

    # 999 is kind of infinity here. Create and assign each cell with this infinity value.
    for i in range(tvRows):
        for j in range(tvCols):
            tvSP[i,j,0] = 999
    
    
    # Initialization means all weights of graph to be simply put in 0th iteration of tvSP matrix.
    for i in range(tvRows):
        for j in range(tvCols):
            if(fvAInput[i,j][0] == 1):
                tvSP[i,j,0] = fvAInput[i][j][1]


    for k in range(1, tvCols+1):
        for i in range(tvRows):
            for j in range(tvCols):
                tvSP[i,j,k] = min(tvSP[i,j,k-1], tvSP[i, k-1, k-1] + tvSP[k-1,j,k-1])

    tvReturn = tvSP[:,:,tvCols]
    return tvReturn













###########################################################################################
######################################__main__#############################################
###########################################################################################

tvGraphNumberList = [2]

for tvGraphNumber in tvGraphNumberList:
    tvAdjecenyMatrix  = WeightedGraph.create_graph_into_adjacency_matrix(tvGraphNumber)
    tvMatOutput = floyd_warshall_allpair_shortest_distance(tvAdjecenyMatrix)
    print(tvMatOutput)

print("Completed Sucessfully")



