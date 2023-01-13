

def remove_duplicates(fvText):
    """input: HHello  Worldd and output: Helo World """

    tvIndexPosToCharLength = {}
    tvLength       = 0
    tvInitialIndex = 0
    tvInitialChar  = None

    for i in range(0, len(fvText)-1):
        if(fvText[i] == fvText[i+1]):
            if(tvLength == 0):
                tvInitialIndex = i
                tvInitialChar  = fvText[tvInitialIndex]
            if(tvInitialChar == fvText[i]):
                tvLength = tvLength + 1
                tvIndexPosToCharLength[tvInitialIndex] = tvLength + 1
        else:
            tvLength = 0
            tvInitialIndex = 0
            tvInitialChar  = None
            continue


    i = 0
    tvOuput = ""
    if(len(tvIndexPosToCharLength) == 0):
        tvOuput = fvText
    else:
        while(i < len(fvText)):
            tvCurrentChar = fvText[i]
            if(i in tvIndexPosToCharLength):
                i = i + tvIndexPosToCharLength[i]
            else:
                i = i + 1
            
            tvOuput = tvOuput + tvCurrentChar

    return tvOuput





def find_sencondlargestvalue(fvInputList):
    """" input = [12, 35, 10, 34, 1]
        sortedInput = [1, 10, 12, 34, 35]
        2ndLargestValue = sortedInput[-2]
        2ndLargestValue = 34
        Task is to efficently find the value.
        https://www.geeksforgeeks.org/find-second-largest-element-array/
    """

    tvMaxValue    = fvInputList[0]
    tv2ndMaxValue = fvInputList[0]

    for i in range(0, len(fvInputList)):

        if(fvInputList[i] > tvMaxValue):
            tvMaxValue = fvInputList[i]

        elif( (fvInputList[i] > tv2ndMaxValue) & (fvInputList[i] < tvMaxValue) ):
            tv2ndMaxValue = fvInputList[i]

    if(tvMaxValue == tv2ndMaxValue):
        return None
    else:
        return tv2ndMaxValue





##############################################################################################################
##########################################____main____########################################################
##############################################################################################################

tvInput = "HHello  Worldd"
tvOuput = remove_duplicates(tvInput)
print(tvInput)
print(tvOuput)


inputList = [[12, 35, 10, 34, 1], [12, 10, 5, 3], [5, 10, 10]]
for input in inputList:
    tvSecondLargestVal = find_sencondlargestvalue(input)
    print(tvSecondLargestVal)

print("Completed Successfully")
