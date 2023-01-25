# In computer science, a heap is a specialized tree-based data structure which is essentially an 
# almost complete[1] tree that satisfies the heap property: in a max heap, for any given node C, 
# if P is a parent node of C, then the key (the value) of P is greater than or equal to the key 
# of C. In a min heap, the key of P is less than or equal to the key of C.[2] The node at the 
# "top" of the heap (with no parents) is called the root node.


import math


def get_left_child(fvIndex):
    """ get_left_child """
    tvLeftChildIndex = 2*fvIndex + 1
    return tvLeftChildIndex



def get_right_child(fvIndex):
    """ get_right_child """
    tvRightChildIndex = 2*fvIndex + 2
    return tvRightChildIndex


def get_parent(fvIndex):
    """ get_parent """
    tvParentIndex = (fvIndex-1)//2
    return tvParentIndex



def swap_value(fvArray, mIndex, nIndex):
    """ Swap the value in the given array/list and index positon provided."""
    if(mIndex != nIndex):
        mVal = fvArray[mIndex]
        nVal = fvArray[nIndex]
        fvArray[mIndex] = nVal
        fvArray[nIndex] = mVal




def do_max_heapify(fvArray, fvStartIndex = 0):
    """ do_max_heapify """

    tvHeapSize = len(fvArray) - 1
    tvleftChildIndex  = get_left_child(fvStartIndex)
    tvRightChildIndex = get_right_child(fvStartIndex)

    tvLargestValueIndex = fvStartIndex

    if( (tvleftChildIndex <= tvHeapSize) and (fvArray[tvleftChildIndex] > fvArray[tvLargestValueIndex]) ):
        tvLargestValueIndex = tvleftChildIndex
    
    if( (tvRightChildIndex <= tvHeapSize) and (fvArray[tvRightChildIndex] > fvArray[tvLargestValueIndex]) ):
        tvLargestValueIndex = tvRightChildIndex
    
    # Now we have largest value stored at 'tvLargestValueIndex' on this particular level. 
    # Let us check in case it voilates the heap property. In that case swap the values 
    # and call recurrive with next level index.
    if(tvLargestValueIndex != fvStartIndex):
        swap_value(fvArray, tvLargestValueIndex, fvStartIndex)
        do_max_heapify(fvArray, tvLargestValueIndex)
    
    return




def build_max_heap(fvArray):
    """ build_max_heap """

    tvHeapHalfIndex = math.ceil(len(fvArray)/2) - 1

    for i in range(tvHeapHalfIndex,-1, -1):
        print("calling do_max_heapify with: " + str(i))
        do_max_heapify(fvArray, i)
        print("After do_max_heapify with: " + str(i) + " " + str(fvArray) )
    







def do_min_heapify(fvArray, fvStartIndex = 0):
    """ do_min_heapify """

    tvHeapSize = len(fvArray) - 1
    tvleftChildIndex  = get_left_child(fvStartIndex)
    tvRightChildIndex = get_right_child(fvStartIndex)

    tvLargestValueIndex = fvStartIndex

    if( (tvleftChildIndex <= tvHeapSize) and (fvArray[tvleftChildIndex] < fvArray[tvLargestValueIndex]) ):
        tvLargestValueIndex = tvleftChildIndex
    
    if( (tvRightChildIndex <= tvHeapSize) and (fvArray[tvRightChildIndex] < fvArray[tvLargestValueIndex]) ):
        tvLargestValueIndex = tvRightChildIndex
    
    # Now we have largest value stored at 'tvLargestValueIndex' on this particular level. 
    # Let us check in case it voilates the heap property. In that case swap the values 
    # and call recurrive with next level index.
    if(tvLargestValueIndex != fvStartIndex):
        swap_value(fvArray, tvLargestValueIndex, fvStartIndex)
        do_min_heapify(fvArray, tvLargestValueIndex)
    return





def build_min_heap(fvArray):
    """ build_min_heap """

    tvHeapHalfIndex = math.ceil(len(fvArray)/2) - 1

    for i in range(tvHeapHalfIndex,-1, -1):
        # print("calling do_min_heapify with: " + str(i))
        do_min_heapify(fvArray, i)
        # print("After do_min_heapify with: " + str(i) + " " + str(fvArray) )
    







def insert_into_max_heap(fvArray, fvValue):
    """ insert_into_max_heap """

    # We need to extend the list by one and last index should be the one 
    # where we keep this value.
    tvNewIndex = len(fvArray)
    fvArray.append(fvValue)

    # Now we need to traverse parents until we reach the top. We need to
    # break when there is no mismatch between the its value with parents value.
    tvParentIndex = get_parent(tvNewIndex)

    while tvParentIndex >= 0:
        tvLastValue = fvArray[tvNewIndex]
        tvParentValue = fvArray[tvParentIndex]
        if(tvLastValue > tvParentValue):
            swap_value(fvArray,tvNewIndex,tvParentIndex)
        else:
            break
        # Update index so that we can go upward
        tvNewIndex = tvParentIndex
        tvParentIndex = get_parent(tvNewIndex)





def delete_into_max_heap(fvArray, fvStartIndex, fvEndIndex):
    """ delete_into_max_heap """

    tvMaxVal  = fvArray[fvStartIndex]
    tvLastVal = fvArray[fvEndIndex]

    # Let us swap value and delete last element. delete here means adjusting
    # 'fvEndIndex'
    swap_value(fvArray, fvStartIndex, fvEndIndex)
    # del fvArray[fvEndIndex]
    fvEndIndex = fvEndIndex -1


    # Now heap is voilated at top so need to fix it with resepect
    # to its children until it comes down end.

    tvStartIndex = fvStartIndex
    tvLen = (fvEndIndex - fvStartIndex) + 1

    while (tvStartIndex < tvLen/2):
        tvLeftChildIndex  = get_left_child(tvStartIndex)
        tvRightChildIndex = get_right_child(tvStartIndex)

        # if both child Index is outside of array, break from here as it happens to be
        # leaf node.
        if( (tvLeftChildIndex >=tvLen) and (tvRightChildIndex >=tvLen) ):
            break

        tvStartValue      = fvArray[tvStartIndex]

        tvLeftChildValue  = None
        tvRightChildValue = None
        if(tvLeftChildIndex < tvLen):
            tvLeftChildValue  = fvArray[tvLeftChildIndex]
        if(tvRightChildIndex < tvLen):
            tvRightChildValue = fvArray[tvRightChildIndex]

        
        # see which child is bigger and accordingly need to swap it with parent/startIndex.
        # This shall gets executed when we have both childs.
        if( (tvLeftChildValue != None) and (tvRightChildValue != None) ):
            if(tvRightChildValue > tvLeftChildValue):
                tvMaxValChildIndex = tvRightChildIndex
            if(tvLeftChildValue > tvRightChildValue):
                tvMaxValChildIndex = tvLeftChildIndex

        elif( (tvLeftChildValue != None) and (tvRightChildValue == None) ):
            if(tvLeftChildValue > tvStartValue):
                tvMaxValChildIndex = tvLeftChildIndex

        elif( (tvLeftChildValue == None) and (tvRightChildValue != None) ):
            if(tvRightChildValue > tvStartValue):
                tvMaxValChildIndex = tvRightChildIndex


        if(fvArray[tvMaxValChildIndex] > tvStartValue):
            swap_value(fvArray, tvStartIndex,tvMaxValChildIndex)
        else:
            break

        # Update index so that we can go downward and fix if required
        tvStartIndex = tvMaxValChildIndex

    return tvMaxVal






def update_into_max_heap(fvHeapArray, fvOldVal, fvNewVal):
    """update_into_max_heap """
    
    # first get index where 'fvOldVal' value is located. Post that
    # we would have to do fix heap either downward or upward based on
    # new value.
    
    tvIndex = None
    try:
        tvIndex = fvHeapArray.index(fvOldVal)
    except ValueError as e:
        return

    # Update with new value. Now do real logic of fixing heap
    fvHeapArray[tvIndex] = fvNewVal

    # Fix parent(upwards). similar to insert_into_max_heap approach
    if(fvNewVal > fvOldVal):
        tvParentIndex = get_parent(tvIndex)
        while tvParentIndex >= 0:
            tvIndexValue = fvHeapArray[tvIndex]
            tvParentValue = fvHeapArray[tvParentIndex]
            if(tvIndexValue > tvParentValue):
                swap_value(fvHeapArray,tvIndex,tvParentIndex)
            else:
                break
            # Update index so that we can go upward
            tvIndex = tvParentIndex
            tvParentIndex = get_parent(tvIndex)


    # Fix children(downwards). similar to delete_into_max_heap approach
    elif(fvOldVal > fvNewVal):
        tvLen = len(fvHeapArray)
        while (tvIndex < tvLen/2):
            tvLeftChildIndex  = get_left_child(tvIndex)
            tvRightChildIndex = get_right_child(tvIndex)

            # if both child Index is outside of array, break from here as it happens to be
            # leaf node.
            if( (tvLeftChildIndex >=tvLen) and (tvRightChildIndex >=tvLen) ):
                break

            tvStartValue = fvHeapArray[tvIndex]

            tvLeftChildValue  = None
            tvRightChildValue = None
            if(tvLeftChildIndex < tvLen):
                tvLeftChildValue  = fvHeapArray[tvLeftChildIndex]
            if(tvRightChildIndex < tvLen):
                tvRightChildValue = fvHeapArray[tvRightChildIndex]

            
            # see which child is bigger and accordingly need to swap it with parent/startIndex.
            # This shall gets executed when we have both childs.
            if( (tvLeftChildValue != None) and (tvRightChildValue != None) ):
                if(tvRightChildValue > tvLeftChildValue):
                    tvMaxValChildIndex = tvRightChildIndex
                if(tvLeftChildValue > tvRightChildValue):
                    tvMaxValChildIndex = tvLeftChildIndex

            elif( (tvLeftChildValue != None) and (tvRightChildValue == None) ):
                if(tvLeftChildValue > tvStartValue):
                    tvMaxValChildIndex = tvLeftChildIndex

            elif( (tvLeftChildValue == None) and (tvRightChildValue != None) ):
                if(tvRightChildValue > tvStartValue):
                    tvMaxValChildIndex = tvRightChildIndex


            if(fvHeapArray[tvMaxValChildIndex] > tvStartValue):
                swap_value(fvHeapArray, tvIndex,tvMaxValChildIndex)
            else:
                break

            # Update index so that we can go downward and fix if required
            tvIndex = tvMaxValChildIndex




def do_max_heap_sort(fvHeapArray):
    """ do_max_heap_sort"""
    
    print("Before calling delete_into_max_heap in loop for heap sort " + str(fvHeapArray))
    for i in range(0, len(fvHeapArray)):
        # We need to shrink the array size by one as that should not be considered in "Heap" array.
        # We would be using that memory to place the maximum deleted value and in end we would get
        # O(nlogn) in-place sorting algorithm. The other O(nlogn) sorting is merge sort however it
        # is not in-place algorithm as it require seprate memory to merge arrays to get final sorted
        # list.
        tvStartIndex = 0
        tvEndIndex = (len(fvHeapArray)-1) -i
        delete_into_max_heap(fvHeapArray, tvStartIndex, tvEndIndex)

    print("Heap Sort Output " + str(fvHeapArray))








##################################################################################################
###################################___ main ___###################################################
##################################################################################################

print("Started Successfully")

for i in range(0,2):
    tvInputList = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 28, 0, 6, 44, -1]
    tvLength = len(tvInputList)

    print("Original Array: " + str(tvInputList) + " with length: " + str(len(tvInputList)))

    if(i == 0):
        # tvStartIndex = 1
        # do_max_heapify(tvInputList, tvStartIndex)
        build_max_heap(tvInputList)
        print("After max_heapify array: " + str(tvInputList))

    elif(i == 1):
        # tvStartIndex = 1
        # do_min_heapify(tvInputList, tvStartIndex)
        build_min_heap(tvInputList)
        print("After min_heapify array: " + str(tvInputList))



tvInputList = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7, 28, 0, 6, 44, -1]
tvLength = len(tvInputList)
build_max_heap(tvInputList)

# insert couple of new data post building heap from initial array.

# insert 12 into above heap data
tvNewVal = 12
insert_into_max_heap(tvInputList, tvNewVal)

# insert max value plus 1 so that this value can go on top and we can test 
# that looping is indeed working fine.
tvMaxVal = max(tvInputList) + 1
insert_into_max_heap(tvInputList, tvMaxVal)


# implement heap sort using main delete_into_max_heap() method. There is very
# decent cleaver tweak required to get in place implementations with O(nlogn)
# complexity.

tvInputList1 = [ 6, 5, 3, 1, 8, 7, 2, 4 ]
build_max_heap(tvInputList1)
do_max_heap_sort(tvInputList1)


update_into_max_heap(tvInputList,-1, 11)
print(tvInputList)


update_into_max_heap(tvInputList, 45, -2)
print(tvInputList)

# do_max_heap_sort(tvInputList)
print("Completed Successfully")
