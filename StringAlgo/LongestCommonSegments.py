# A longest common subsequence (LCS) is the longest subsequence common to all sequences in a set of 
# sequences (often just two sequences). It differs from the longest common substring: unlike substrings, 
# subsequences are not required to occupy consecutive positions within the original sequences. The problem 
# of computing longest common subsequences is a classic computer science problem, the basis of data comparison 
# programs such as the diff utility, and has applications in computational linguistics and bioinformatics. It 
# is also widely used by revision control systems such as Git for reconciling multiple changes made to a 
# revision-controlled collection of files.


# Some examples.
# "secret"  "secretary" ===>    "secret"
# "bisect"   "trisect"  ===>    "isect"
# "bisect"   "secret"   ===>     "sec"


# Formally
# u = a0a1a2......am-1
# v = b0b1b2......bn-1
# common subword of length k - for some positions i and j,
# a(i)a(i+1)..a(i+k-1) == b(j)b(j+1)..b(j+k-1)
# Find the largest such k -- length of the longest common subwords.



import numpy as np





def find_common_subwords_bruteforce(fvFirst, fvSecond):
    """ find_common_subwords_bruteforce"""

    tvLongestSubwordList = []

    tvMinLenString   = ""
    tvMaxLenString   = ""

    tvFirstLen = len(fvFirst)
    tvSecondLen = len(fvSecond)
    tvMinLen = min(tvFirstLen, tvSecondLen)

    if(tvMinLen == tvFirstLen):
        tvMinLenString = fvFirst
        tvMaxLenString = fvSecond
    else:
        tvMinLenString = fvSecond
        tvMaxLenString = fvFirst

    tJ = 0
    tvLongestSubword = ""

    for tI in range(len(tvMinLenString)):
        tvCurChar = tvMinLenString[tI]

        if(len(tvLongestSubword) == 0):
            tJ = 0
        
        while tJ < len(tvMaxLenString):
            if(tvCurChar == tvMaxLenString[tJ]):
                tvLongestSubword = tvLongestSubword + tvMaxLenString[tJ]
                tJ = tJ + 1
                break
            else:
                # check in case we have something common in 'tvLongestSubword'
                if( (len(tvLongestSubword) >= 2) and (tJ == (len(tvMaxLenString) -1)) ):
                    tvLongestSubwordList.append(tvLongestSubword)
                    tvLongestSubword = ""
                tJ = tJ + 1


    if(len(tvLongestSubword) >= 2):
        tvLongestSubwordList.append(tvLongestSubword)


    return tvLongestSubwordList







def find_common_subwords_dynamic_approach(fvFirst, fvSecond):
    """ find_common_subwords_dynamic_approach. The LCW(i,j) = 1 + LCW(i+1, j+1)"""

    tvLongestSubwordList = []
    tvIndexPostList      = []
    tvCurrentMax         = 0

    tvFirstLen = len(fvFirst)
    tvSecondLen = len(fvSecond)

    # intialize tvMatrix matrix with tvFirstLen+1 & tvSecondLen+1 length with zero values.
    tvMatrix = np.zeros(shape=(tvFirstLen+1,tvSecondLen+1), dtype=int)

    (tvRows, tvCols) = tvMatrix.shape
    for colIndex in range(tvCols-2, -1, -1):
        for rowIndex in range(tvRows-2, -1, -1):
            if(fvFirst[rowIndex] == fvSecond[colIndex]):
                tvMatrix[rowIndex, colIndex] = 1 + tvMatrix[rowIndex+1, colIndex+1]
                if(tvMatrix[rowIndex, colIndex] >= tvCurrentMax):
                    tvCurrentMax = tvMatrix[rowIndex, colIndex]
                    tvPosIndex = (rowIndex,colIndex)
                    if(tvPosIndex  not in tvIndexPostList):
                        tvIndexPostList.append(tvPosIndex)

    # print(tvMatrix)
    # print(tvIndexPostList)

    # Now scan all non-zero values and see which one have the maximum value.
    # Post that we need either row or column ways to extract the substring.
    # In case we use 'aPosIndex[0]' we are doing row ways calculation and we need
    # to use 'fvFirst' to extract string.
    for aPosIndex in tvIndexPostList:
        if(tvMatrix[aPosIndex[0], aPosIndex[1]] == int(tvCurrentMax)):
            tvLongestSubString = ""
            for tI in range(aPosIndex[0], aPosIndex[0]+ int(tvCurrentMax)):
                tvLongestSubString = tvLongestSubString + fvFirst[tI]
            tvLongestSubwordList.append(tvLongestSubString)


    return tvLongestSubwordList








def find_common_subsequence_dynamic_approach(fvFirst, fvSecond):
    """ find_common_subsequence_dynamic_approach. When char are
    equals then we need to define like LCS(i,j) = 1 + LCS(i+1, j+1).
    else LCS(i,j) = max(LCS(i+1,j) + LCS(i, j+1))"""

    tvFirstLen = len(fvFirst)
    tvSecondLen = len(fvSecond)

    # intialize tvMatrix matrix with tvFirstLen+1 & tvSecondLen+1 length with zero values.
    tvMatrix = np.zeros(shape=(tvFirstLen+1,tvSecondLen+1), dtype=int)

    (tvRows, tvCols) = tvMatrix.shape
    for colIndex in range(tvCols-2, -1, -1):
        for rowIndex in range(tvRows-2, -1, -1):
            # Based on inductive 
            if(fvFirst[rowIndex] == fvSecond[colIndex]):
                tvMatrix[rowIndex, colIndex] = 1 + tvMatrix[rowIndex+1, colIndex+1]
            else:
                tvMatrix[rowIndex, colIndex] = max( tvMatrix[rowIndex+1, colIndex], tvMatrix[rowIndex, colIndex+1])

    print(tvMatrix)          
    return int(tvMatrix[0][0])






####################################################################################
##############################________main_________#################################
####################################################################################


tvFirst  = "abcd"
tvSecond = "becd"
# tvFirst  = "director"
# tvSecond = "secretary"
tvCommonSubWordsList = find_common_subwords_bruteforce(tvFirst, tvSecond)
print(str(tvCommonSubWordsList) + " common words in " + tvFirst +  " and " + tvSecond + " word")


tvCommonSubWordsDynamicApproachList = find_common_subwords_dynamic_approach(tvFirst, tvSecond)
print(str(tvCommonSubWordsDynamicApproachList) + " common words in " + tvFirst +  " and " + tvSecond + " word")


tvCommonSubWordsDynamicApproachList = find_common_subwords_dynamic_approach(tvFirst, tvSecond)
print(str(tvCommonSubWordsDynamicApproachList) + " common words in " + tvFirst +  " and " + tvSecond + " word")


tvOutput = find_common_subsequence_dynamic_approach(tvFirst, tvSecond)
print(str(tvOutput) + " common subsquence index position(3,3) " + tvFirst +  " and " + tvSecond + " word")


print("Completed Sucessfully")
