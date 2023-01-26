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
    
    print(tvCharList)
    print(tvCharFreqList)

    print("build_char_frequencies")








####################################################################################
##############################________main_________#################################
####################################################################################


# read some file text into memory which is present in the same directory where 
# current python file resides.
tvPath = Path(__file__)

txtFileName = "inputText.txt"
tvTextFromFile  = ""
txtFilePath = path.join(tvPath.parent, txtFileName)

with open(txtFilePath, "r") as fHandle:
    tvTextFromFile = fHandle.read()

build_char_frequencies(tvTextFromFile)


print("Completed Sucessfully")
