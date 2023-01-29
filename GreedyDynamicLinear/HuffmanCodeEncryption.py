# Lossless compression is a class of data compression that allows the original data to be perfectly reconstructed 
# from the compressed data with no loss of information. Lossless compression is possible because most real-world 
# data exhibits statistical redundancy.[1] By contrast, lossy compression permits reconstruction only of an 
# approximation of the original data, though usually with greatly improved compression rates (and therefore 
# reduced media sizes).


# In computer science and information theory, a Huffman code is a particular type of optimal prefix code 
# that is commonly used for lossless data compression. The process of finding or using such a code proceeds
# by means of Huffman coding, an algorithm developed by David A. Huffman while he was a Sc.D. student at MIT, 
# and published in the 1952 paper "A Method for the Construction of Minimum-Redundancy Codes".[1]

# The output from Huffman's algorithm can be viewed as a variable-length code table for encoding a source 
# symbol (such as a character in a file). The algorithm derives this table from the estimated probability 
# or frequency of occurrence (weight) for each possible value of the source symbol. As in other entropy 
# encoding methods, more common symbols are generally represented using fewer bits than less common 
# symbols. Huffman's method can be efficiently implemented, finding a code in time linear to the number 
# of input weights if these weights are sorted.[2] However, although optimal among methods encoding 
# symbols separately, Huffman coding is not always optimal among all compression methods - it is 
# replaced with arithmetic coding[3] or asymmetric numeral systems[4] if a better compression ratio 
# is required.



# Morse code is a method used in telecommunication to encode text characters as standardized sequences of 
# two different signal durations, called dots and dashes, or dits and dahs.[3][4] Morse code is named 
# after Samuel Morse, one of the inventors of the telegraph. International Morse code encodes the 26 
# basic Latin letters a through z, one accented Latin letter (é), the Arabic numerals, and a small set 
# of punctuation and procedural signals (prosigns). There is no distinction between upper and lower case 
# letters.[1] Each Morse code symbol is formed by a sequence of dits and dahs. The dit duration is the 
# basic unit of time measurement in Morse code transmission. The duration of a dah is three times the 
# duration of a dit. Each dit or dah within an encoded character is followed by a period of signal 
# absence, called a space, equal to the dit duration. The letters of a word are separated by a space 
# of duration equal to three dits, and words are separated by a space equal to seven dits.[


import os
from pathlib import Path
from os import path
import nltk

from collections import Counter




class Stack:
    """Stack implementation using list data structures as member. """

    def __init__(self):
        self.ivStack = []
    
    def push(self, fvValue):
        self.ivStack.append(fvValue)
    
    def pop(self):
        tvValue = None
        if not self.isEmpty():
            tvValue = self.ivStack[-1]
            self.ivStack = self.ivStack[0:len(self.ivStack)-1]
        return tvValue
    
    def top(self):
        tvValue = None
        if not self.isEmpty():
            tvValue = self.ivStack[-1]
        return tvValue
    
    def isEmpty(self):
        return (len(self.ivStack) == 0)

    def __str__(self):
        return (str(self.ivStack))





class Tree:
    """ Basic binary search tree implementations. Borrowed from Tree module/subdirectory."""

    # Constructor
    def __init__(self, initval = None):
        self.value = initval
        if(self.value != None):
            self.left  = Tree()
            self.right = Tree()
        else:
            self.left  = None
            self.right = None

        return
    

    # only empty node has value None
    def isempty(self):
        return (self.value == None)
    
    # Leaf node have both children empty
    def isleaf(self):
        return (self.value != None  and
                self.left.isempty() and
                self.right.isempty() )
    

    # In order traversal
    def inorder(self):
        if(self.isempty()):
            return ([])
        else:
            return (self.left.inorder() +
                    [self.value] +
                    self.right.inorder() )



    # Display Tree as a string
    def __str__(self):
        return (str(self.inorder() ) )
    


    # Pre order traversal
    def preorder(self):
        if(self.isempty()):
            return ([])
        else:
            return ([self.value] + 
                    self.left.preorder() +
                    self.right.preorder() )


    # Post order traversal
    def postorder(self):
        if(self.isempty()):
            return ([])
        else:
            return ( self.left.postorder() +
                    self.right.postorder() +
                    [self.value] )


    # make current node empty.
    def makeempty(self):
        self.value = None
        self.left = None
        self.right = None
        return


    # make current node assign all which is present in right side of node.
    def copyright(self):
        self.value = self.right.value
        self.left  = self.right.left
        self.right = self.right.right

    # make current node assign all which is present in left side of node.
    def copyleft(self):
        self.value = self.left.value
        self.right = self.left.right
        self.left  = self.left.left


    # check if value v occurs in a tree
    def find(self, v):
        if(self.isempty()):
            return False
        if(self.value == v):
            return True
        
        if(v < self.value):
            return (self.left.find(v))
        
        if(v > self.value):
            return (self.right.find(v))
    

    # check if value v occurs in a tree, if it is present get it
    # so that we can process it further and set its left and right child.
    def getNode(self, v):
        if(self.isempty()):
            return None
        if(self.value == v):
            return self
        
        if(v < self.value):
            return (self.left.getNode(v))
        
        if(v > self.value):
            return (self.right.getNode(v))
    

    # go to the left most last value where we find minimum
    def minvalue(self):
        if(self.left.isempty()):
            return self.value
        else:
            return(self.left.minvalue())


    # go to the right most last value where we find maximum
    def maxvalue(self):
        if(self.right.isempty()):
            return self.value
        else:
            return(self.right.maxvalue())


    def insert(self,v):
        """ Find the positon of the v if it would have already be in the tree.
        thats the place it should be kept/insert. """

        # If current tree is empty and we call insert. 
        if self.isempty():
            self.value = v
            self.left = Tree()
            self.right = Tree()
        
        # if value which needs to be inserted is already present. do nothing.
        if self.value == v:
            return
        
        # if value which needs to be inserted is smaller than current node value.
        if(v < self.value):
            self.left.insert(v)
            return
        
        # if value which needs to be inserted is greated than current node value.
        if(v > self.value):
            self.right.insert(v)
            return
    

    


    def delete(self, v):
        """ Find if it exists in the treee and in case found delete it. but after deleting 
        it, we need to rebalance it."""
    
        # If current tree is empty and we call delete, do nothing.
        if self.isempty():
            return

        # If value which needs to be deleted is smaller than current node value.
        if(v < self.value):
            self.left.delete(v)
            return
        
        # If value which needs to be deleted is greated than current node value.
        if(v > self.value):
            self.right.delete(v)
            return

        # If value is found, then we need to handle it more carefully and all cases should
        # be covered.
        if(v == self.value):
            # if current node is leaf node, then just delete is
            if(self.isleaf()):
                self.makeempty()
            
            # if current node is non leaf node with just right child presence.
            elif(self.left.isempty()):
                self.copyright()
            
            # if current node is non leaf node with just left child presence.
            elif(self.right.isempty()):
                self.copyleft()
            
            # if current node is non leaf node with both right and left child presence. Find the maximum value
            # in the left subtree region and keep it here. And now delete that particular node form the left
            # subtree regions.
            else:
                self.value = self.left.maxvalue()
                self.left.delete(self.left.maxvalue())

            return





def build_char_frequencies(fvTextInpt):
    """ build_char_frequencies """

    # Below is useful in case we want to find frquency distribution of each words.
    # tvTokens = nltk.word_tokenize(fvTextInpt)
    # tvFrequencyDistribution = nltk.FreqDist(tvTokens)

    # https://stackoverflow.com/questions/12342207/count-frequency-of-letters-in-a-text-file

    tvCounter = Counter(fvTextInpt)

    tvCharList     = []
    tvCharFreqList = []
    tvTotalCharCount = 0


    # print(tvCounter)
    for charKey, charKeyCount in tvCounter.items():
        # print(charKey, charKeyCount)
        tvCharList.append(charKey)
        tvTotalCharCount = tvTotalCharCount + charKeyCount

    for charKey in tvCharList:
        tvCharCount = tvCounter[charKey]
        tvFreq = tvCharCount/tvTotalCharCount
        tvCharFreqList.append(tvFreq)
    
    return (tvCharList, tvCharFreqList)







def build_huffman_tree(fvCharList, fvFreqList, fvLength):
    """ build_huffman_tree """

    tvReturnCharCodeDic = {}

    tvCharToFreqDic = {}
    for i in range(0, fvLength):
        tvCharToFreqDic[fvCharList[i]] = fvFreqList[i]

    # This would contain stack of operations order. This would be required while actually building
    # the huffman tree later on.
    tvStack = Stack()
    tvDicLength = len(tvCharToFreqDic)
    while tvDicLength > 2:
        # Get two smallest element and merge them.
        tvSorteValuesTuples = sorted(tvCharToFreqDic.items(), key= lambda x:x[1])
        tvFirstKey   = tvSorteValuesTuples[0][0]
        tvFirstValue = tvSorteValuesTuples[0][1]

        tvSecondKey   = tvSorteValuesTuples[1][0]
        tvSecondValue = tvSorteValuesTuples[1][1]

        # now combine these two
        tvCombinedKey = tvFirstKey + tvSecondKey
        tvCombinedVal = tvFirstValue + tvSecondValue

        # now delete two previous key
        del tvCharToFreqDic[tvFirstKey]
        del tvCharToFreqDic[tvSecondKey]

        # now update dictionary with new key value
        tvCharToFreqDic[tvCombinedKey] = tvCombinedVal

        tvDicLength = len(tvCharToFreqDic)

        tvStack.push(tvFirstKey)
        tvStack.push(tvSecondKey)
        tvStack.push(tvCombinedKey)


    # Now we need to actually form the huffman binary tree using exisiting data.
    
    # Now above dictionary should have just two elements.
    tvKeyList = list(tvCharToFreqDic.keys())
    # tvInitialLeftValue  = tvCharToFreqDic[tvKeyList[0]]
    # tvInitialRightValue = tvCharToFreqDic[tvKeyList[1]]
    # tvInitialRootValue  = tvInitialLeftValue + tvInitialRightValue
    tvInitialLeftKey       = tvKeyList[0]
    tvInitialRightKey      = tvKeyList[1]
    tvInitialRootKey       = tvInitialLeftKey + tvInitialRightKey

    # First, let us create a binary tree with initialvalue and initialKey
    tvHuffmanBTreeRoot       = Tree(tvInitialRootKey) 
    tvHuffmanBTreeRoot.left  = Tree(tvInitialLeftKey)
    tvHuffmanBTreeRoot.right = Tree(tvInitialRightKey)
    
    # maintains the leaf nodes and their pathss as this needs to be used for further processing.
    tvLeafNodeAndCodeList = []
    tvLeafNodeAndCodeList.append( (tvHuffmanBTreeRoot.left,[0]) )
    tvLeafNodeAndCodeList.append( (tvHuffmanBTreeRoot.right,[1]) )



    # Now we need to loop through the stack and start processing data in order to build tree.
    while(not tvStack.isEmpty()):
        tvParentNode     = tvStack.pop()
        tvLeftChildNode  = tvStack.pop()
        tvRightChildNode = tvStack.pop()

        # check if exists in the tree and in case it does, get the object and update their childs.
        for aLeafNode in tvLeafNodeAndCodeList:
            if(aLeafNode[0].value == tvParentNode):
                tvCurrNode       = aLeafNode[0]
                if(tvCurrNode != None):
                    tvLeftNodeCodeList = []
                    tvRightNodeCodeList = []
                    for item in aLeafNode[1]:
                        tvLeftNodeCodeList.append(item)
                        tvRightNodeCodeList.append(item)
                    
                    tvCurrNode.left  = Tree(tvLeftChildNode)
                    tvLeftNodeCodeList.append(0)
                    tvCurrNode.right = Tree(tvRightChildNode)
                    tvRightNodeCodeList.append(1)


                    tvLeafNodeAndCodeList.remove(aLeafNode)
                    tvLeafNodeAndCodeList.append( (tvCurrNode.left, tvLeftNodeCodeList) )
                    tvLeafNodeAndCodeList.append( (tvCurrNode.right, tvRightNodeCodeList) )
                    break



    
    for tvLeafNode in tvLeafNodeAndCodeList:
        if(tvLeafNode[0].value in fvCharList):
            tvAsciiLikeCode = ""
            for aCode in tvLeafNode[1]:
                tvAsciiLikeCode = tvAsciiLikeCode + str(aCode)
            tvReturnCharCodeDic[tvLeafNode[0].value] = tvAsciiLikeCode 

    return tvReturnCharCodeDic






def encyrpt_original_text_using_huffmancode(fvOriginalText, fvHuffmanCharToCodeDic):
    """ encyrpt_original_text_using_huffmancode """    
    
    tvEncryptText = ""
    
    # For exmample A = 65 => 01000001
    tvASCIICodePerChar = 8
    
    tvOriginalTextLength = tvASCIICodePerChar*len(fvOriginalText)
    print("Original Text length In Bits: " + str(tvOriginalTextLength) )

    # Do encyrpt/compress orginal text
    for aChar in fvOriginalText:
        tvEncryptText = tvEncryptText + fvHuffmanCharToCodeDic[aChar]


    tvEncryptedTextLength = len(tvEncryptText)
    print("Encyrpted Text length In Bits: " + str(tvEncryptedTextLength) )

    # Total saving from original data.
    tvrReduction = (tvOriginalTextLength - tvEncryptedTextLength)/tvOriginalTextLength
    tvrReduction = int(tvrReduction*100)
    print("Total Reduction(in %) from original text: " +  str(tvrReduction) )

    return tvEncryptText






def decyrpt_to_retrive_original_text_using_huffmancode(fvEncyrptedText, fvHuffmanCharToCodeDic):
    """ decyrpt_to_retrive_original_text_using_huffmancode """

    tvOriginalText = ""

    tvKeyList   = list(fvHuffmanCharToCodeDic.keys())
    tvValueList = list(fvHuffmanCharToCodeDic.values())

    tvHuffmanCodeToCharDic = {}

    for i in range(len(tvValueList)):
        tvHuffmanCodeToCharDic[tvValueList[i]] = tvKeyList[i]


    tvSingleChar = ""
    # Do retrive orginal text from fvEncyrptedText
    for i in range(0, len(fvEncyrptedText) ):
        tvSingleChar = tvSingleChar + fvEncyrptedText[i]
        if(tvSingleChar in tvHuffmanCodeToCharDic):
            tvOriginalText = tvOriginalText + tvHuffmanCodeToCharDic[tvSingleChar]
            tvSingleChar = ""


    return tvOriginalText







####################################################################################
##############################________main_________#################################
####################################################################################

# tvDic = {"0":1, "1":0, "2":3,"4":2, "3":4}
# tvListOfTuples = sorted(tvDic.items(), key= lambda x:x[1])
# for tvElem in tvListOfTuples:
#     print(tvElem[0] , " ::" , tvElem[1] )


# read some file text into memory which is present in the same directory where 
# current python file resides.
tvPath = Path(__file__)

txtInputFileName = "inputText.txt"
tvTextFromFile  = ""
txtInFilePath = path.join(tvPath.parent, txtInputFileName)




# Read original text from input file.
with open(txtInFilePath, "r") as fHandle:
    tvTextFromFile = fHandle.read()

tvOutput = build_char_frequencies(tvTextFromFile)

tvCharList = tvOutput[0]
tvCharFreqList = tvOutput[1]

for i in range(len(tvCharFreqList)):
    print(str(tvCharList[i]) + ": " + str(tvCharFreqList[i]) )

tvHuffmanCharToCodeDic = build_huffman_tree(tvCharList, tvCharFreqList, len(tvCharFreqList))
# print(tvHuffmanCharToCodeDic)
for aKey, aValue in tvHuffmanCharToCodeDic.items():
    print(str(aKey) + ": " + str(aValue))

# # use course example to build the huffman tree
# tvCharList = ['a', 'b', 'c', 'd', 'e']
# tvCharFreqList = [0.32, 0.25, 0.20, 0.18, 0.05]
# tvHuffmanCharToCodeDic = build_huffman_tree(tvCharList, tvCharFreqList, len(tvCharFreqList))
# print(tvHuffmanCharToCodeDic)
# {'a': '10', 'b': '11', 'c': '01', 'd': '000', 'e': '001'}



tvEncryptText = encyrpt_original_text_using_huffmancode(tvTextFromFile, tvHuffmanCharToCodeDic)
# print(tvEncryptText)

tvOriginalText = decyrpt_to_retrive_original_text_using_huffmancode(tvEncryptText, tvHuffmanCharToCodeDic)
# print(tvOriginalText)


if(tvOriginalText == tvTextFromFile):
    print("Algorithms seems to be working fine")


# Write into output text file. This could be useful for file comparsion utility for larger files.
txtOutputFileName = "outputText.txt"
tvTextToFile      = ""
txtOutFilePath    = path.join(tvPath.parent, txtOutputFileName)


with open(txtOutFilePath, "w") as fHandle:
    # fHandle.write(tvEncryptText)
    fHandle.write(tvOriginalText)


print("Completed Sucessfully")


