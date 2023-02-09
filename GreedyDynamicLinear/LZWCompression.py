# Lempel–Ziv–Welch (LZW) is a universal lossless data compression algorithm created by Abraham Lempel, Jacob Ziv, 
# and Terry Welch. It was published by Welch in 1984 as an improved implementation of the LZ78 algorithm published 
# by Lempel and Ziv in 1978. The algorithm is simple to implement and has the potential for very high throughput 
# in hardware implementations.[1] It is the algorithm of the Unix file compression utility compress and is used 
# in the GIF image format.

# Encoding
# --------
# A high-level view of the encoding algorithm is shown here:

    # 1. Initialize the dictionary to contain all strings of length one.
    # 2. Find the longest string W in the dictionary that matches the current input.
    # 3. Emit the dictionary index for W to output and remove W from the input.
    # 4. Add W followed by the next symbol in the input to the dictionary.
    # 5. Go to Step 2.


# Decoding
# ---------
# A high-level view of the decoding algorithm is shown here:

    # 1. Initialize the dictionary to contain all strings of length one.
    # 2. Read the next encoded symbol: Is it encoded in the dictionary?
        # 1. Yes:
            # 1. Emit the corresponding string W to output.
            # 2.Concatenate the previous string emitted to output with the first symbol of W. Add this to the dictionary.
        # 2. No:
            # 1. Concatenate the previous string emitted to output with its first symbol. Call this string V.
            # 2. Add V to the dictionary and emit V to output.
    # 3. Repeat Step 2 until end of input string


# https://www.cs.cmu.edu/~pattis/15-1XX/common/handouts/ascii.html
# Dec  Char                           Dec  Char     Dec  Char     Dec  Char
# ---------                           ---------     ---------     ----------
#   0  NUL (null)                      32  SPACE     64  @         96  `
#   1  SOH (start of heading)          33  !         65  A         97  a
#   2  STX (start of text)             34  "         66  B         98  b
#   3  ETX (end of text)               35  #         67  C         99  c
#   4  EOT (end of transmission)       36  $         68  D        100  d
#   5  ENQ (enquiry)                   37  %         69  E        101  e
#   6  ACK (acknowledge)               38  &         70  F        102  f
#   7  BEL (bell)                      39  '         71  G        103  g
#   8  BS  (backspace)                 40  (         72  H        104  h
#   9  TAB (horizontal tab)            41  )         73  I        105  i
#  10  LF  (NL line feed, new line)    42  *         74  J        106  j
#  11  VT  (vertical tab)              43  +         75  K        107  k
#  12  FF  (NP form feed, new page)    44  ,         76  L        108  l
#  13  CR  (carriage return)           45  -         77  M        109  m
#  14  SO  (shift out)                 46  .         78  N        110  n
#  15  SI  (shift in)                  47  /         79  O        111  o
#  16  DLE (data link escape)          48  0         80  P        112  p
#  17  DC1 (device control 1)          49  1         81  Q        113  q
#  18  DC2 (device control 2)          50  2         82  R        114  r
#  19  DC3 (device control 3)          51  3         83  S        115  s
#  20  DC4 (device control 4)          52  4         84  T        116  t
#  21  NAK (negative acknowledge)      53  5         85  U        117  u
#  22  SYN (synchronous idle)          54  6         86  V        118  v
#  23  ETB (end of trans. block)       55  7         87  W        119  w
#  24  CAN (cancel)                    56  8         88  X        120  x
#  25  EM  (end of medium)             57  9         89  Y        121  y
#  26  SUB (substitute)                58  :         90  Z        122  z
#  27  ESC (escape)                    59  ;         91  [        123  {
#  28  FS  (file separator)            60  <         92  \        124  |
#  29  GS  (group separator)           61  =         93  ]        125  }
#  30  RS  (record separator)          62  >         94  ^        126  ~
#  31  US  (unit separator)            63  ?         95  _        127  DEL



import os
from pathlib import Path
from os import path








def lzw_compression(fvInputString):
    """ lzw_compression """

    # Initialize dictionary with ASCII value to its corresponding 'char'. chr() 
    # method converts decimal ASCII value to char equivalent. ord() method converts
    # back char to decimal ASCII value.

    tvFullAsciiCharLen = 256
    tvCharToAsciiDic   = {}
    tvOutputCodeList   = []

    for tI in range(tvFullAsciiCharLen):
        tvCharToAsciiDic[chr(tI)] = tI 

    # initialize 'tS' with first character from text.
    tS = fvInputString[0]

    for tI in range(1, len(fvInputString)):
        # take next character from text
        tC = fvInputString[tI]
        
        # Check tSC is in disctionary and in that case, set tSC as initial value tS
        tSC = tS + tC
        if(tSC in tvCharToAsciiDic):
            tS = tSC
        else:
            # Output the index of tS in a list and insert tS into disctionary with 
            # next available ASCII value.
            tvOutputCodeList.append(tvCharToAsciiDic[tS])
            tvCharToAsciiDic[tSC] = tvFullAsciiCharLen
            tvFullAsciiCharLen = tvFullAsciiCharLen + 1
            tS = tC

    tvOutputCodeList.append(tvCharToAsciiDic[tS])
    return(tvCharToAsciiDic, tvOutputCodeList)






def lzw_decompression(fvIndicesList):
    """ lzw_decompression """

    tvRetrievedString = ""

    # Initialize dictionary with ASCII value to its corresponding 'char'. chr() 
    # method converts decimal ASCII value to char equivalent. ord() method converts
    # back char to decimal ASCII value.

    tvFullAsciiCharLen = 256
    tvAsciiDicToChar   = {}

    for tI in range(tvFullAsciiCharLen):
        tvAsciiDicToChar[tI] = chr(tI)



    # initialize 'tCurrent' with first character from fvIndicesList.
    tCurrent = fvIndicesList[0]
    tvRetrievedString = tvRetrievedString + tvAsciiDicToChar[tCurrent]

    for tI in range(1, len(fvIndicesList)):
        # Set 'tPrevious' to current & take the next entry fvIndicesList into the 'tCurrent'.
        tPrevious = tCurrent
        tCurrent  = fvIndicesList[tI]
        
        if(tCurrent in tvAsciiDicToChar):
            tS = tvAsciiDicToChar[tCurrent]
            tvRetrievedString = tvRetrievedString + tS

            tNewEntry = tvAsciiDicToChar[tPrevious] + tS[0]
            tvAsciiDicToChar[tvFullAsciiCharLen] = tNewEntry
            tvFullAsciiCharLen = tvFullAsciiCharLen + 1
        
        else:
            tS = tvAsciiDicToChar[tPrevious]
            tvRetrievedString = tvRetrievedString + tS[0]
            tvAsciiDicToChar[tvFullAsciiCharLen] = tvRetrievedString
            tvFullAsciiCharLen = tvFullAsciiCharLen + 1

    return tvRetrievedString






# ####################################################################################
# ##############################________main_________#################################
# ####################################################################################

# read some file text into memory which is present in the same directory where 
# current python file resides.
tvPath = Path(__file__)

txtInputFileName = "LZWInputText.txt"
tvTextFromFile  = ""
txtInFilePath = path.join(tvPath.parent, txtInputFileName)

# Read original text from input file.
with open(txtInFilePath, "r") as fHandle:
    tvTextFromFile = fHandle.read()


tvInputString = "ABD-ABKABD-ABDABDK"
# tvInputString  = tvTextFromFile

tvOutput = lzw_compression(tvInputString)

tvCharToAsciiDic = tvOutput[0]
tvOutputCodeList = tvOutput[1]

tvRerievedString = lzw_decompression(tvOutputCodeList)


if(tvRerievedString == tvInputString):
    print("Algorithms seems to be working fine")

# Write into output text file. This could be useful for file comparsion utility for larger files.
txtOutputFileName = "outputText.txt"
tvTextToFile      = ""
txtOutFilePath    = path.join(tvPath.parent, txtOutputFileName)


with open(txtOutFilePath, "w") as fHandle:
    fHandle.write(tvRerievedString)

print("Completed Sucessfully")
