import pandas as pd
import numpy as np
import random
import time



# Total maximum process
# gMaxProcessCount = 15625

# Flag to indicates whether random number is being initialized or not.
tvRandintFlag = True



def generate_random_array(fvListLength = 10, startValue = 2, EndValue = 30):
    """This method basically returns the list with random number. This list
    would have only unique entry just to make algorithm understanding
    easier for now """

    tvOutPutList = []
    while True:
        n = random.randint(startValue,EndValue)
        value = int(n)
        if(value in tvOutPutList):
            pass
        else:
            tvOutPutList.append(int(n))
            if(len(tvOutPutList) == fvListLength):
                break
    
    return tvOutPutList









def binary_search_for_finding_index(fvArray, fvStartIndex, fvEndIndex, fvValue):
    """This is the most practical way to search a value in input list. However the
    pre-condition of this is that it required input list to be sorted. This needs to
    be maintained by this 2D array. """

    tvMiddleIndex = 0

    # This seems to be buggy as I need to return the appropriate position of values.
    # TODO: Require some thoughts.
    if(fvStartIndex == fvEndIndex):
        if(fvStartIndex == len(fvArray)):
            fvStartIndex = fvStartIndex -1
        
        if(fvArray[fvStartIndex] < fvValue):
            tvMiddleIndex = fvStartIndex
            return tvMiddleIndex
        if(fvArray[fvStartIndex] >= fvValue):
            tvMiddleIndex = fvStartIndex
            return tvMiddleIndex


    # get th middle of the list for doing divide and conquer approach.
    tvMiddleIndex = (fvStartIndex + fvEndIndex)//2

    if(fvArray[tvMiddleIndex] == fvValue):
        return tvMiddleIndex
    
    if(fvValue < fvArray[tvMiddleIndex]):
        # Left half to search
        return binary_search_for_finding_index(fvArray, fvStartIndex, tvMiddleIndex, fvValue)
    else:
        # Right half to search
        return binary_search_for_finding_index(fvArray, tvMiddleIndex+1, fvEndIndex, fvValue)






# priority queue using moving from 1D to 2D approach
def priority_queue_using_2d_initialize():
    """ priority_queue_using_2d_initialize """

    print(">> priority_queue_using_2d_initialize")

    ###############################
    # initialization
    ###############################

    gMaxProcessCount     = 25
    gRowCount            = int(gMaxProcessCount**(1/2))
    gColumnCount         = int(gMaxProcessCount**(1/2))
    gProcessGrid = np.zeros(shape=(gRowCount, gColumnCount), dtype=int)
    gRowIndexToLengthMap = {}
    
    tvCurrentRowLength = gRowCount - 2 

    # fill with some random test case data so that we can actually
    # debug and implement and see how insert() & delete_max() methods
    # actually works. 
    for tvSingleRowIndex in range(0,gRowCount):
        tvRowList = generate_random_array(tvCurrentRowLength)
        # we need sorted array
        tvRowList = sorted(tvRowList)
        for tvInnerRowIndex in range(0, len(tvRowList)):
            gProcessGrid[tvSingleRowIndex,tvInnerRowIndex] = tvRowList[tvInnerRowIndex]
        
        gRowIndexToLengthMap[tvSingleRowIndex] = len(tvRowList)

    print(gProcessGrid)
    print(gRowIndexToLengthMap)



    #################################
    # insert operation understanding
    #################################

    # do it with 4 items to understand the proceeding.
    tvInsertValueList = [11, 22, 33, 44, 55]

    for item in tvInsertValueList:
        tvInsertValue = item

        # first get the row index where something is available.
        tvRowIndexForUse = -1
        for rowIndex, rowLength in gRowIndexToLengthMap.items():
            if(rowLength < gRowCount):
                tvRowIndexForUse = rowIndex
                break
        
        # now we have valid index of row where slots are available.
        tvColumnIndex = gRowIndexToLengthMap[tvRowIndexForUse]

        # now update the length.
        tvCurrentLength = gRowIndexToLengthMap[tvRowIndexForUse]
        tvUpdatedLength = tvCurrentLength + 1
        gRowIndexToLengthMap[tvRowIndexForUse] = gRowIndexToLengthMap[tvRowIndexForUse] + 1

        # now we need to scan through entire row to find the appropriate position and shift if required.
        gProcessGrid[tvRowIndexForUse, tvColumnIndex] = tvInsertValue

        tvUpdatedRowValueList = []
        for tvColumnIndex in range(0, tvUpdatedLength):
            # print(gProcessGrid[tvRowIndexForUse, tvColumnIndex])
            tvUpdatedRowValueList.append(gProcessGrid[tvRowIndexForUse, tvColumnIndex])

        # now lets us sort it before copying back to the list.
        tvUpdatedRowValueList =  sorted(tvUpdatedRowValueList)

        # now update the 2D grid with latest value.
        for tvColumnIndex in range(0, tvUpdatedLength):
            gProcessGrid[tvRowIndexForUse, tvColumnIndex] = tvUpdatedRowValueList[tvColumnIndex]




        print(gProcessGrid)
        print(gRowIndexToLengthMap)


    ####################################
    # delete-max operation
    #####################################


    # do it twice to see how things are proceeding.
    for operationIndex in range(0, 19):
        tvMaxOfMaxValueList = []

        for tvRowIndex in range(0, gRowCount):
            tvColumnIndex = gRowIndexToLengthMap[tvRowIndex] - 1
            tvRowMaxValue = gProcessGrid[tvRowIndex, tvColumnIndex]
            tvMaxOfMaxValueList.append(tvRowMaxValue)

        # now let us find the index position where maximum value are.
        tvMaxPriorityValueIndex = 0
        tvMaxPriorityValue = tvMaxOfMaxValueList[0]
        for index in range(1, len(tvMaxOfMaxValueList)):
            if(tvMaxOfMaxValueList[index] >= tvMaxPriorityValue):
                tvMaxPriorityValueIndex = index
                tvMaxPriorityValue = tvMaxOfMaxValueList[index]


        print("delete-Max Operation, Highest Priority Value: " + str(tvMaxPriorityValue))
        
        # now clean-up the 2D structure and dictionary values as we have updated the maximum.
        tvColumnIndex = gRowIndexToLengthMap[tvMaxPriorityValueIndex] - 1
        gProcessGrid[tvMaxPriorityValueIndex, tvColumnIndex] = 0

        gRowIndexToLengthMap[tvMaxPriorityValueIndex] = gRowIndexToLengthMap[tvMaxPriorityValueIndex] - 1

        print(gProcessGrid)
        print(gRowIndexToLengthMap)




    print("<< priority_queue_using_2d_initialize")







##################################################################################################
###################################___ main ___###################################################
##################################################################################################
print("Started Successfully")
priority_queue_using_2d_initialize()

tvInputList = [5, 10, 20, 30, 40, 50]
tvLength = len(tvInputList)
tvValue = 70
tvOutIndex = binary_search_for_finding_index(tvInputList, 0, tvLength-1, tvValue)
print(tvOutIndex)

print("Completed Successfully")
