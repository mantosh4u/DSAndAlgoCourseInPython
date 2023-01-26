# Stirng matching related alogrithms learning and implementations.


import os
from pathlib import Path
from os import path



def stringMatchForward(fvText, fvPattern):
    """ simple brute force approach for searching pattern in given text with forward looking."""

    tvPosIndexList = []

    for textIndex in range(0, (len(fvText)-len(fvPattern) ) + 1):

        for patternIndex in range(0, len(fvPattern)):
            if(fvPattern[patternIndex] == fvText[patternIndex + textIndex]):
                continue
            else:
                # shift back the index as we found mismatch here
                patternIndex = patternIndex -1
                break

        # check in case we really got complete match    
        if(patternIndex == len(fvPattern) -1):
            tvPosIndexList.append(textIndex)

    return tvPosIndexList






def stringMatchBackward(fvText, fvPattern):
    """ simple brute force approach for searching pattern in given text with backward looking."""

    tvPosIndexList = []

    for textIndex in range(0, (len(fvText)-len(fvPattern) ) + 1):

        for patternIndex in range(len(fvPattern)-1, -1, -1):
            if(fvPattern[patternIndex] == fvText[patternIndex + textIndex]):
                continue
            else:
                # shift forward the index as we found mismatch here
                patternIndex = patternIndex + 1
                break

        # check in case we really got complete match    
        if(patternIndex == 0):
            tvPosIndexList.append(textIndex)

    return tvPosIndexList








def boyermoore_stringmatch(fvText, fvPattern):
    """Boyer Moore Algorithms basically does intelligent skipping based on some
    additional logic."""

    tvPosIndexList = []
    tvLastPosDic   = {}
    for patternIndex in range(0, len(fvPattern)):
        tvLastPosDic[fvPattern[patternIndex]] = patternIndex

    # print(tvLastPosDic)

    textIndex = 0
    while textIndex < (len(fvText) - len(fvPattern) + 1):
        # print(textIndex)
        for patternIndex in range(len(fvPattern)-1, -1, -1):
            if(fvPattern[patternIndex] == fvText[patternIndex + textIndex]):
                continue
            else:
                # shift forward the index as we found mismatch here
                patternIndex = patternIndex + 1
                break

        # check in case we really got complete match    
        if(patternIndex == 0):
            tvPosIndexList.append(textIndex)
            textIndex = textIndex + 1
        else:
            patternIndex = patternIndex - 1 
            # now intelligent skipping logic needs to be put so that we can skip if we can.

            # first check in case the current mismatched characters is not present in pattern.
            # in that case shift it by the size of the pattern.
            tvCurMismatchedIndex   = patternIndex + textIndex
            tvCurCharVal = fvText[tvCurMismatchedIndex]

            if(tvCurCharVal not in tvLastPosDic):
                tvDeltaIndex = (len(fvPattern) - 1) - patternIndex
                textIndex = textIndex + len(fvPattern) - tvDeltaIndex
            else:
                # second situation when current mismatched characters is present in pattern.
                # in that case shift it by the index so that mismatched characters could be align.
                tvLastPosIndex = tvLastPosDic[tvCurCharVal]
                tvDiffInIndex  =  patternIndex - tvLastPosIndex
                textIndex = textIndex + tvDiffInIndex


        if(textIndex > len(fvText)):
            break


    return tvPosIndexList











def rabincarp_stringmatch(fvText, fvPattern):
    """This one implements rabin carp algorithms for string matching. """

    tvPosIndexList = []

    tvNumt = 0
    tvNump = 0
    for i in range(0,len(fvPattern)):
        tvNumt = 10*tvNumt + ord(fvText[i])
        tvNump = 10*tvNump + ord(fvPattern[i])

    if(tvNumt == tvNump):
        tvPosIndexList.append(0)


    for i in range(1, len(fvText) - len(fvPattern) +1):
        tvNumt = tvNumt - ord(fvText[i-1])*(10**(len(fvPattern)-1))
        tvNumt = 10*tvNumt + ord(fvText[i+len(fvPattern) -1])
    
        if(tvNumt == tvNump):
            tvPosIndexList.append(i)


    return tvPosIndexList














##############################################################################################################
##########################################____main____########################################################
##############################################################################################################

tvTextList    = ["abcabaabcabac", "aaa", "which finally halts.  at that point"]
tvPatternList = ["abac", "aa", "at that"]

# read some file text into memory which is present in the same directory where 
# current python file resides.
tvPath = Path(__file__)

txtFileName = "inputText.txt"
tvTextFromFile  = ""
txtFilePath = path.join(tvPath.parent, txtFileName)

tvTextFromFile  = ""
with open(txtFilePath, "r") as fHandle:
    tvTextFromFile = fHandle.read()


if(len(tvTextFromFile)> 0):
    tvTextList.append(tvTextFromFile)
    tvPatternList.append("friendship")


for i in range(0, len(tvTextList)):
    tvText = tvTextList[i]
    tvPattern = tvPatternList[i]

    tvForPosIndexList = stringMatchForward(tvText, tvPattern)
    print(tvForPosIndexList)

    tvBackPosIndexList = []
    tvBackPosIndexList = stringMatchBackward(tvText, tvPattern)
    print(tvBackPosIndexList)

    tvBoyerMoorePosIndexList = []
    tvBoyerMoorePosIndexList = boyermoore_stringmatch(tvText, tvPattern)
    print(tvBoyerMoorePosIndexList)


    if( (len(tvForPosIndexList) == len(tvBackPosIndexList)) and ( len(tvBackPosIndexList) == len(tvBoyerMoorePosIndexList)) ):
        print("Completed Successfully with " + str(len(tvBackPosIndexList)) + " search")
    else:
        print("Problem in implementation")


    tvrabinCarpPosIndexList = []
    tvrabinCarpPosIndexList = rabincarp_stringmatch(tvText, tvPattern)
    print(tvrabinCarpPosIndexList)


    
print("Completed Successfully")


