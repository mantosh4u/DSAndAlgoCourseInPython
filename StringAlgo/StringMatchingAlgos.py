# In computer science, string-searching algorithms, sometimes called string-matching algorithms, are an important 
# class of string algorithms that try to find a place where one or several strings (also called patterns) are 
# found within a larger string or text.

# Naive string search
# -------------------
# A simple and inefficient way to see where one string occurs inside another is to check at each index, one by one. First, 
# we see if there's a copy of the needle starting at the first character of the haystack; if not, we look to see if there's 
# a copy of the needle starting at the second character of the haystack, and so forth. In the normal case, we only have to 
# look at one or two characters for each wrong position to see that it is a wrong position, so in the average case, 
# this takes O(n + m) steps, where n is the length of the haystack and m is the length of the needle; but in the worst 
# case, searching for a string like "aaaab" in a string like "aaaaaaaaab", it takes O(nm).


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       



import os
from pathlib import Path
from os import path



def stringMatchForward(fvText, fvPattern):
    """ simple brute force approach for searching pattern in given text with forward looking."""

    tvPosIndexList = []
    n = len(fvText)
    m = len(fvPattern)

    for tI in range(0, n-m+1):
        for pI in range(0, m):
            if(fvPattern[pI] == fvText[pI + tI]):
                continue
            else:
                break

        # check in case we really got complete match by checking out pI index got complete 
        # length of pattern.
        if(pI == (m -1) ):
            tvPosIndexList.append(tI)

    return tvPosIndexList






def stringMatchBackward(fvText, fvPattern):
    """ simple brute force approach for searching pattern in given text with backward looking."""

    tvPosIndexList = []
    n = len(fvText)
    m = len(fvPattern)

    # reverse processing of pattern. range(m-1, -1, -1) for m = 3 for fvPattern = "abc".
    # range(2,-1, -1) means fvPattern[2], fvPattern[1], fvPattern[0]. We can go just upto
    # 0 and not earlier.

    for tI in range(0, n-m+1):
        for pI in range(m-1, -1, -1):
            if(fvPattern[pI] == fvText[pI + tI]):
                continue
            else:
                break

        # check in case we really got complete match by checking out pI index got complete
        # length of pattern. 
        if(pI == 0):
            tvPosIndexList.append(tI)

    return tvPosIndexList








def boyermoore_stringmatch(fvText, fvPattern):
    """Boyer Moore Algorithms basically does intelligent skipping based on some
    additional logic."""


    tvPosIndexList = []
    n = len(fvText)
    m = len(fvPattern)

    # For skippinng logic to work, we need to know which all character are their in
    # pattern and also position of the charcaters in the pattern. So this preprocessing
    # of pattern would helps us a lot to implement skip logic.
    tvLastCharPosDic = {}
    for i in range(m):
        tvLastCharPosDic[fvPattern[i]] = i


    tI = 0
    while tI <= (n-m):
        # Uncomment below loggig to see how skip logic is working as compared to navive approach.
        # print("Text: " + str(fvText[tI:tI+len(fvPattern)]) + " Pattern: " + str(fvPattern))

        for pI in range(m-1, -1, -1):
            tvP = fvPattern[pI]
            tvT = fvText[pI+ tI]
            if(tvP == tvT):
                continue
            else:
                # Before breaking lets us check in case this particular character is present into
                # the pattern or not. In this case we shift the text index beyond this char as any
                # overlapping text which involves the char would not match. 
                if(tvT not in tvLastCharPosDic):
                    tI = tI + (pI +1)
                # In case, current char does not match but char does appear in the pattern, so in that
                # case, we need to shift the index so that both char can align. 
                elif(tvT in tvLastCharPosDic):
                    tDiff = (pI+ tI) - tvLastCharPosDic[tvT]
                    tI = tDiff
                break

        # check in case we really got complete match by checking out pI index got complete
        # length of pattern. Now append it and then shift index by one to go further.
        if(pI == 0):
            tvPosIndexList.append(tI)
            tI = tI + 1

    return tvPosIndexList
































def rabincarp_stringmatch(fvText, fvPattern):
    """This one implements rabin carp algorithms for string matching. """

    tvPosIndexList = []
    n = len(fvText)
    m = len(fvPattern)


    tvNumt = 0
    tvNump = 0
    for i in range(0, m):
        tvNumt = 10*tvNumt + ord(fvText[i])
        tvNump = 10*tvNump + ord(fvPattern[i])

    if(tvNumt == tvNump):
        tvPosIndexList.append(0)


    for i in range(1, n-m+1):
        tvNumt = tvNumt - ord(fvText[i-1])*(10**(m-1))
        tvNumt = 10*tvNumt + ord(fvText[i+m -1])
    
        if(tvNumt == tvNump):
            tvPosIndexList.append(i)


    return tvPosIndexList















##############################################################################################################
##########################################____main____########################################################
##############################################################################################################

tvTextList    = ["bananamania","abcabaabcabac", "aaa", "which finally halts.  at that point"]
tvPatternList = ["bulk", "abac", "aa", "at that"]

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


for i in range(3, len(tvTextList)):
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



