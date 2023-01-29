# Dynamic programming is both a mathematical optimization method and a computer programming method. The method was 
# developed by Richard Bellman in the 1950s and has found applications in numerous fields, from aerospace engineering 
# to economics.

# In both contexts it refers to simplifying a complicated problem by breaking it down into simpler sub-problems in a 
# recursive manner. While some decision problems cannot be taken apart this way, decisions that span several points 
# in time do often break apart recursively. Likewise, in computer science, if a problem can be solved optimally by 
# breaking it into sub-problems and then recursively finding the optimal solutions to the sub-problems, then it is 
# said to have optimal substructure.

# If sub-problems can be nested recursively inside larger problems, so that dynamic programming methods are applicable, 
# then there is a relation between the value of the larger problem and the values of the sub-problems.[1] In the 
# optimization literature this relationship is called the Bellman equation.


# In computing, memoization or memoisation is an optimization technique used primarily to speed up computer programs 
# by storing the results of expensive function calls and returning the cached result when the same inputs occur again. 
# Memoization has also been used in other contexts (and for purposes other than speed gains), such as in simple 
# mutually recursive descent parsing.[1] Although related to caching, memoization refers to a specific case of 
# this optimization, distinguishing it from forms of caching such as buffering or page replacement. In the context 
# of some logic programming languages, memoization is also known as tabling.[2]


gFibTable = {}


def fib(n):
    """fibonacci number calculation"""

    if n <= 1:
        value = n
    else:
        value = fib(n-1) + fib(n-2)

    return value



def memoization_fib(n):
    """fibonacci number calculation using memoization dynmaic programming techniques."""

    global gFibTable

    if(n in gFibTable):
        value = gFibTable[n]
    else:
        if n <= 1:
            value = n
        else:
            value = fib(n-1) + fib(n-2)
        
        gFibTable[n] = value
    
    return value






####################################################################################
##############################________main_________#################################
####################################################################################

tvNumberList = [0,1,2,3,4,5,6,7,8,9,10,20,30,40]
tvOutputList = []

for aNumber in tvNumberList:
    # tvOutput = fib(aNumber)
    tvOutput = memoization_fib(aNumber)
    tvOutputList.append(tvOutput)

for i in range(len(tvNumberList)):
    print(str(tvNumberList[i])+ ": " + str(tvOutputList[i]) )

print("Completed Sucessfully")



