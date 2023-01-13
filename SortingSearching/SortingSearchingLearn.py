import random
import time

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd




############################################################################################
######################################### Helper Routines###################################
############################################################################################


def generate_random_array(fvSize = 10, startValue = 2, EndValue = 30):
    """This method basically returns the list with random number. This list
    would have only unique entry just to make sorting algorithm understanding
    easier for now """

    tvOutPutList = []

    for i in range(0,fvSize):
        n = random.randint(startValue,EndValue)
        value = int(n)
        if(value in tvOutPutList):
            pass
        else:
            tvOutPutList.append(int(n))
    return tvOutPutList






def swap_value(fvArray, mIndex, nIndex):
    """ Swap the value in the given array/list and index positon provided."""
    if(mIndex != nIndex):
        mVal = fvArray[mIndex]
        nVal = fvArray[nIndex]
        fvArray[mIndex] = nVal
        fvArray[nIndex] = mVal






def delete_unamed_columns_in_panda_dataframe(dataFrameObject):
    """Scan all colunm names and delete if any unamed found"""
    # Delete any columns with unammed stuff. lets loop through it and 
    # check if we do have any such, in that case we would delete it.
    for columnName in list(dataFrameObject.columns.values):
        if(str(columnName).startswith("Unnamed:") == True):
            dataFrameObject.drop([str(columnName)], axis = 1, inplace = True)






class TimeError(Exception):
    """A custom exception used to report errors in use of Timer Class"""


class PeformanceTimer:
    """Basic timer class which would help us to measure the time taken by
    an algorithm. """

    def __init__(self):
        self._start_time   = None
        self._elapsed_time = None
    
    def start(self):
        """"Start a new timer"""
        if self._start_time is not None:
            raise TimeError("Timer is running. Use .stop()")
        self._start_time = time.perf_counter()

    def stop(self):
        """"Save the elapsed time and re-initialize timer """
        if self._start_time is None:
            raise TimeError("Time is not running. Use .start()")
        self._elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
    
    def elapsed(self):
        """Reported  elapsed time"""
        if self._elapsed_time is not None:
            raise TimeError("Timer has not been run yet. Use .start()")
        return(self._elapsed_time)

    def __str__(self):
        """ print() prints  elapsed time"""
        return(str(self._elapsed_time))







def test_performance_measurement_routine():
    """ For doing standalone calculation of performance measurement for any 
    block of code. """

    # Python executes 10^7 operations per seconds.
    # C/C++ typically executes 10^8 or more operations per seconds. This essentially
    # means that python is alomst 10x factor slower from C/C++ code. Need to understand
    # how 'PeformanceTimer' class is working internally and calculates the operations and
    # all.

    t = PeformanceTimer()

    for j in range(7, 10):
        t.start()
        n = 0
        for i in range(10**j):
            n = n + i
        t.stop()

        print(j, t)







###########################################################################################
################################### Naive Search ##########################################
###########################################################################################


def linear_search(fvAarray, fvValue):
    """" This is the naive way to search something. This is o(n) complexity."""

    tvRetValue = False
    for index in range(0, len(fvAarray)):
        if(fvAarray[index] == fvValue):
            tvRetValue = True
            break

    return tvRetValue





def binary_search(fvArray, fvValue):
    """This is the most practical way to search a value in input list. However the
    pre-condition of this is that it required input list to be sorted. """

    tvLength = len(fvArray)

    # base condition for the recursion.
    if(tvLength == 0):
        return False

    # get th middle of the list for doing divide and conquer approach.
    tvMiddleIndex = tvLength//2

    if(fvArray[tvMiddleIndex] == fvValue):
        return True
    
    if(fvValue < fvArray[tvMiddleIndex]):
        # Left half to search
        return binary_search(fvArray[:tvMiddleIndex], fvValue)
    else:
        # Right half to search
        return binary_search(fvArray[tvMiddleIndex+1:], fvValue)







############################################################################################
######################################### Bubble Sort ######################################
############################################################################################

def bubble_sort(fvArray):
    """ Implementation of bubble sort algorithm."""

    # We need to loop through [0:tvLength-1] index to reach all entry in the list
    # Inner loop would be[0:tvLength-1-indexMain]. This is so because after each outer
    # iteration, the last index would have maximum value(bubbled) so we do not need to
    # consider it in the next iteration. The effective array size would keep on shrinking
    # after every outer interation.

    # inputArray         [5, 21, 20, 29, 30, 27, 22, 3]
    #                    [-----------------------------]
    # After 1 iteration :[5, 20, 21, 29, 27, 22, 3, 30]
    #                    [------------------------]
    # After 2 iteration :[5, 20, 21, 27, 22, 3, 29, 30]
    #                    [--------------------]
    # After 3 iteration :[5, 20, 21, 22, 3, 27, 29, 30]
    #                    [----------------]
    # After 4 iteration :[5, 20, 21, 3, 22, 27, 29, 30]
    #                    [------------]
    # After 5 iteration :[5, 20, 3, 21, 22, 27, 29, 30]
    #                    [--------]
    # .....
    # ...
    # SortedArray        [3, 5, 20, 21, 22, 27, 29, 30]
    
    # In the implementation I have also kept logging which can be used to understand how the input 
    # array is changing post each iteration.


    tvLength = len(fvArray)
    
    for indexMain in range(0, tvLength):
        for indexInner in range(0, tvLength-1 -indexMain):
            if(fvArray[indexInner] > fvArray[indexInner+1]):
                swap_value(fvArray, indexInner, indexInner+1)
        # print("After " + str(indexMain) + " iteration :" + fvArray.__str__())














############################################################################################
######################################### selection sort ###################################
############################################################################################

def selection_sort(fvArray):
    """ Implementation of selection sort algorithm."""
    
    # We need to loop through [0:tvLength-1] index to reach all entry in the list
    # Inner loop would be[indexMain+1:tvLength-1]. This is so because after each outer
    # index, we would sawap the miminum value with the current index(indexMain). So after
    # each outer iteration, the inner iteration would shrink effective array to consider.
    # inputArray         [5, 21, 20, 29, 30, 27, 22, 3]
    #                    [----------------------------] 
    # After 1 iteration :[3, 21, 20, 29, 30, 27, 22, 5]
    #                        [------------------------] 
    # After 2 iteration :[3, 5, 20, 29, 30, 27, 22, 21]
    #                           [---------------------]
    # After 3 iteration :[3, 5, 20, 29, 30, 27, 22, 21]
    #                               [-----------------]
    # After 4 iteration :[3, 5, 20, 21, 30, 27, 22, 29]
    #                                   [-------------]
    # After 5 iteration :[3, 5, 20, 21, 22, 27, 30, 29]
    #                                       [---------]
    # ...
    # ..
    # SortedArray        [3, 5, 20, 21, 22, 27, 29, 30]

    # In the implementation I have also kept logging which can be used to understand how the input 
    # array is changing post each iteration.

    tvLength = len(fvArray)

    for indexMain in range(0, tvLength):
        minValIndex = indexMain
        for indexInner in range(indexMain+1, tvLength):
            if(fvArray[minValIndex] > fvArray[indexInner]):
                minValIndex = indexInner
        
        swap_value(fvArray, indexMain, minValIndex)
        # print("After " + str(indexMain) + " iteration :" + fvArray.__str__())











############################################################################################
######################################### insertion sort ###################################
############################################################################################

def insertion_sort(fvArray):
    """ Implementation of insertion sort algorithm."""

    # We need to loop through [1:tvLength-1] index to reach all entry in the list.
    # This means in case there is only one element in array, its already sorted!!
    
    # so we have [minValIndex, indexMain] where things needs to be shifted to insert the 
    # pivotValue at the appropriate position in the smaller list. Basically we need to
    # create the position for the pivotValue in the list for accomadation. For that we
    # need to right shift the elements to one postion so that it can be accomdated.
    # The innermost reverse loop does the shift operation and then lastly we accomdate
    # it pivotValue at the appropriate position. 
    
    # inputArray         [17, 16, 22, 30, 18, 2, 27, 7, 24]
    #                    [--------------------------------] 
    # After 1 iteration :[16, 17, 22, 30, 18, 2, 27, 7, 24]
    #                    [-----]
    # After 2 iteration :[16, 17, 22, 30, 18, 2, 27, 7, 24]
    #                    [---------]  
    # After 3 iteration :[16, 17, 22, 30, 18, 2, 27, 7, 24]
    #                    [-------------]
    # After 4 iteration :[16, 17, 18, 22, 30, 2, 27, 7, 24]
    #                    [-----------------]
    # After 5 iteration :[2, 16, 17, 18, 22, 30, 27, 7, 24]
    #                    [--------------------]
    # ....
    # ..
    # SortedArray        [2, 7, 16, 17, 18, 22, 24, 27, 30]


    tvLength = len(fvArray)

    for indexMain in range(1, tvLength):
        minValIndex = 0
        tvPivotValue = fvArray[indexMain]
        # finding out the minValue
        for indexInner in range(0, indexMain+1):
            if(fvArray[indexInner] > tvPivotValue):
                minValIndex = indexInner
                # shifting operation and inserting pivotValue
                for insertIndex in range(indexMain, minValIndex, -1):
                    fvArray[insertIndex] = fvArray[insertIndex-1]
                fvArray[minValIndex] = tvPivotValue
                break
        # print("After " + str(indexMain) + " iteration :" + fvArray.__str__())
            









############################################################################################
######################################### Merge Sort #######################################
############################################################################################

def merge_arrays(fvArrayA, fvArrayB):
    """Merge routine for two input arrays which are sorted. It assumes that both arrays 
    are sorted and this routine only take care to merge it into one. """

    # fvArrayA   [9, 20, 21, 29]
    #  indexA--->(0)
    # fvArrayB   [4, 9, 11, 16, 21, 27, 30]
    #  indexB--->(0)
    # After 1 iteration :[4]

    # fvArrayA   [9, 20, 21, 29]
    #  indexA--->(0)
    # fvArrayB   [4, 9, 11, 16, 21, 27, 30]
    #  indexB------>(1)
    # After 2 iteration :[4, 9]

    # ......
    # ...
    # So on


    tvOutPutList = []

    tvLengthA = len(fvArrayA)
    tvLengthB = len(fvArrayB)

    indexA    = 0
    indexB    = 0
    while ((tvLengthA > 0) and (tvLengthB > 0)):
        if(fvArrayA[indexA] < fvArrayB[indexB]):
            tvOutPutList.append(fvArrayA[indexA])
            indexA = indexA +1
            if(indexA == tvLengthA):
                break
        else:
            tvOutPutList.append(fvArrayB[indexB])
            indexB = indexB + 1
            if(indexB == tvLengthB):
                break

    if(indexA < tvLengthA):
        for indexRemain in range(indexA, tvLengthA):
            tvOutPutList.append(fvArrayA[indexRemain])
           
    if(indexB < tvLengthB):
        for indexRemain in range(indexB, tvLengthB):
            tvOutPutList.append(fvArrayB[indexRemain])
           

    # print("After completion of merge routine :" + tvOutPutList.__str__())
    return tvOutPutList







def merge_sort(fvArray):
    """ Implementation of merge sort algorithm."""

    # This is pretty simple as almost all logic is inside the merge_arrays.
    # So pay attention to that. This simply breaks(divide) the bigger problem
    # to the smallest easiest issue and then keep up(conquer) using those work
    # and gets things done. 
    
    # fvArrayA       [4, 5, 9, 29, 24, 20, 13, 14]
    # After completion of merge routine :[4, 5]
    # After completion of merge routine :[9, 29]
    # After completion of merge routine :[4, 5, 9, 29]
    # After completion of merge routine :[20, 24]
    # After completion of merge routine :[13, 14]
    # After completion of merge routine :[13, 14, 20, 24]
    # After completion of merge routine :[4, 5, 9, 13, 14, 20, 24, 29]
    # fvArrayA      [4, 5, 9, 13, 14, 20, 24, 29]


    tvLength = len(fvArray)
    # base condition for the recursion.
    if(tvLength <= 1):
        return fvArray

    leftArray  = merge_sort(fvArray[:tvLength//2])
    rightArray = merge_sort(fvArray[tvLength//2:])

    tvMergeList = merge_arrays(leftArray, rightArray)
    return tvMergeList






# def test_merge_rotuine():
#     """ For doing standalone testing for merge routine."""

#     print(">> test_merge_rotuine")
    
#     arrayA = generate_random_array(5)
#     arrayB = generate_random_array(8)

#     insertion_sort(arrayA)
#     selection_sort(arrayB)

#     print("Sorted ArrayA: " + arrayA.__str__())
#     print("Sorted ArrayB: " + arrayB.__str__())

#     mergedArray = merge_arrays(arrayA, arrayB)
#     print("Merged Array: " + mergedArray.__str__())

#     print("<< test_merge_rotuine")








############################################################################################
######################################### Quick Sort #######################################
############################################################################################


def quicksort_partition_routine(fvArray, fvStartIndex, fvEndIndex):
    """ partition routine which would be helper for quicksort algorithm. """

    finalPivotIndex  = 0
    # print("Before completion of partition routine :" + fvArray[fvStartIndex:fvEndIndex].__str__())

    # Basically quick sort moves the work from merging(post) to the partition(before). This causes
    # nothig to be done in post work.
    # In order to understand it, switch on(uncomment) the loggingt/tracing logic from below part.
    

    # base condition!!
    if( (fvEndIndex - fvStartIndex ) <= 1):
        return finalPivotIndex

    # as pivot is first, everything starts with 1 till finaindex + 1
    tvPivotValue = fvArray[fvStartIndex]
    tvLowerEndIndex  = fvStartIndex + 1
    tvHigherEndIndex = fvStartIndex + 1

    for index in range(fvStartIndex+1, fvEndIndex):
        if(fvArray[index] < tvPivotValue):
            if(tvHigherEndIndex != 1):
                swap_value(fvArray, tvLowerEndIndex, index)
            tvLowerEndIndex += 1
            tvHigherEndIndex += 1
        
        elif(fvArray[index] >= tvPivotValue):
            tvHigherEndIndex += 1
    

    # once partition is done, we need to insert pivot at approprite position and then return
    # to its caller. As tvLowerEndIndex maintains the end of boundary, we would require to adjust
    # by 1 while doing actual swap.
    tvLowerEndIndex -= 1
    swap_value(fvArray, fvStartIndex, tvLowerEndIndex)
    finalPivotIndex = tvLowerEndIndex

    # print("After completion of partition routine :" + fvArray[fvStartIndex:fvEndIndex].__str__())
    return finalPivotIndex









def quick_sort(fvArray, fvStartIndex, fvEndIndex):
    """ Implementation of quick sort algorithm."""

    # This is pretty simple as almost all logic is inside the quicksort_partition_routine.
    # So pay attention to that. 


    tvLength = fvEndIndex - fvStartIndex
    # base condition for the recursion.
    if(tvLength <= 1):
        return fvArray

    pivotIndex = quicksort_partition_routine(fvArray, fvStartIndex, fvEndIndex)

    quick_sort(fvArray, fvStartIndex, pivotIndex)
    quick_sort(fvArray, pivotIndex+1, fvEndIndex)

    return fvArray














############################################################################################
####################################### Algorithms Sample Execution ########################
############################################################################################

def linear_search_execution(fvArray, fvValue, fvSortTimeList):
    """ linear search execution measurement. """

    t = PeformanceTimer()
    t.start()
    tvRetValue = linear_search(fvArray, fvValue)
    t.stop()
    print("Time Taken In LinearSearch: "+ str(t))
    print(tvRetValue)
    fvSortTimeList.append(t._elapsed_time)




def binary_search_exeuction(fvArray, fvValue, fvSortTimeList):
    """ binary search execution measurement. """

    t = PeformanceTimer()
    t.start()
    tvRetValue = binary_search(fvArray, fvValue)
    t.stop()
    print("Time Taken In BinarySearch: "+ str(t))
    print(tvRetValue)
    fvSortTimeList.append(t._elapsed_time)







def quick_sort_execution(fvArray, fvSortTimeList):
    """ quick sort execution measurement. """

    t = PeformanceTimer()
    t.start()
    # print(">> Before Sorting(QuickSort): " + fvArray.__str__())
    quick_sort(fvArray, 0, len(fvArray))
    # print("<< Afteer Sorting(QuickSort): " + fvArray.__str__())
    t.stop()
    print("Time Taken In QuickSort: "+ str(t))
    fvSortTimeList.append(t._elapsed_time)








def merge_sort_exeuction(fvArray, fvSortTimeList):
    """ merge sort execution measurement. """

    t = PeformanceTimer()
    t.start()
    # print(">> Before Sorting(MergeSort): " + fvArray.__str__())
    tvOutputMergeSortArray = merge_sort(fvArray)
    # print("<< Afteer Sorting(MergeSort): " + tvOutputMergeSortArray.__str__())
    t.stop()
    print("Time Taken In MergeSort: "+ str(t))
    fvSortTimeList.append(t._elapsed_time)




def insertion_sort_exeuction(fvArray, fvSortTimeList):
    """ insertion sort execution  measurement."""

    t = PeformanceTimer()
    t.start()
    # print(">> Before Sorting(InsertionSort): " + fvArray.__str__())
    insertion_sort(fvArray)
    # print("<< Afteer Sorting(InsertionSort): " + fvArray.__str__())
    t.stop()
    print("Time Taken In InsertionSort: "+ str(t))
    fvSortTimeList.append(t._elapsed_time)



def selection_sort_execution(fvArray, fvSortTimeList):
    """ selection sort execution measurement."""
    
    t = PeformanceTimer()
    t.start()
    # print(">> Before Sorting(SelectionSort): " + fvArray.__str__())
    selection_sort(fvArray)
    # print("<< Afteer Sorting(SelectionSort): " + fvArray.__str__())
    t.stop()
    print("Time Taken In SelectionSort: "+ str(t))
    fvSortTimeList.append(t._elapsed_time)




def bubble_sort_execution(fvArray, fvSortTimeList):
    """ bubble sort execution measurement. """

    t = PeformanceTimer()
    t.start()
    # print(">> Before Sorting(BubleSort): " + fvArray.__str__())
    bubble_sort(fvArray)
    # print("<< Afteer Sorting(BubleSort): " + fvArray.__str__())
    t.stop()
    print("Time Taken In BubbleSort: " + str(t))
    fvSortTimeList.append(t._elapsed_time)





###########################################################################################
######################################__main__#############################################
###########################################################################################


##############
print(">> started generting very large list with random number")
fvSize = 100000
startValue = 2
EndValue = 10*fvSize
gvInputArray = generate_random_array(fvSize, startValue, EndValue)
gvLength = len(gvInputArray)
print(">> completed generting large list with random number with size: " + str(gvLength))
##############



###############
print("Searching")

tvHeaderNameList = ["InputSize", "Linear", "Binary"]
tvInputSizeList         = []
tvLinearSearchTimeList  = []
tvBinarySearchTimeList  = []


for index in range(1,6):
    fvSize = index*10000
    tvInputArray = gvInputArray[:fvSize]
    print("Input is generated with length: " + str(len(tvInputArray)))
    tvInputSizeList.append(len(tvInputArray))

    tvInputForSortArray = tvInputArray.copy()
    quick_sort(tvInputForSortArray, 0, len(tvInputForSortArray))
    # tvInputValue = (startValue + EndValue)//2
    tvInputValue = tvInputArray[-1]

    linear_search_execution(tvInputArray, tvInputValue, tvLinearSearchTimeList)
    binary_search_exeuction(tvInputForSortArray, tvInputForSortArray[-1], tvBinarySearchTimeList)




inputDic = {tvHeaderNameList[0]: tvInputSizeList, \
            tvHeaderNameList[1]: tvLinearSearchTimeList,\
            tvHeaderNameList[2]: tvBinarySearchTimeList
            }

tvDfPlotting = pd.DataFrame.from_dict(inputDic)
delete_unamed_columns_in_panda_dataframe(tvDfPlotting)
print(tvDfPlotting)
tvDfPlotting.to_csv("OutputSearch.csv")




###############
print("Sorting")

tvHeaderNameList = ["InputSize", "Quick", "Merge", "Insertion", "Selection", "Bubble"]
tvInputSizeList         = []
tvQuickSortTimeList     = []
tvMergeSortTimeList     = []
tvInsertionSortTimeList = []
tvSelectionSortTimeList = []
tvBubbleSortTimeList    = []


for index in range(1,6):
    fvSize = index*10000

    tvInputBubleSortArray     = gvInputArray[:fvSize]
    tvInputSelectionSortArray = tvInputBubleSortArray.copy()
    tvInputInsertionSortArray = tvInputBubleSortArray.copy()
    tvInputMergeSortArray     = tvInputBubleSortArray.copy()
    tvInputQuickSortArray     = tvInputBubleSortArray.copy()

    print("Input is generated with length: " + str(len(tvInputBubleSortArray)))
    tvInputSizeList.append(len(tvInputBubleSortArray))

    quick_sort_execution(tvInputQuickSortArray, tvQuickSortTimeList)
    merge_sort_exeuction(tvInputMergeSortArray, tvMergeSortTimeList)
    insertion_sort_exeuction(tvInputInsertionSortArray, tvInsertionSortTimeList)
    selection_sort_execution(tvInputSelectionSortArray, tvSelectionSortTimeList)
    bubble_sort_execution(tvInputBubleSortArray, tvBubbleSortTimeList)




inputDic = {tvHeaderNameList[0]: tvInputSizeList, \
            tvHeaderNameList[1]: tvQuickSortTimeList,\
            tvHeaderNameList[2]: tvMergeSortTimeList,\
            tvHeaderNameList[3]: tvInsertionSortTimeList,\
            tvHeaderNameList[4]: tvSelectionSortTimeList,\
            tvHeaderNameList[5]: tvBubbleSortTimeList
            }

tvDfPlotting = pd.DataFrame.from_dict(inputDic)
delete_unamed_columns_in_panda_dataframe(tvDfPlotting)
print(tvDfPlotting)

tvDfPlotting.to_csv("OutputSort.csv")

print("Completed Successfully")
