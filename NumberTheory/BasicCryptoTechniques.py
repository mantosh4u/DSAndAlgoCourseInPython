# Cryptography prior to the modern age was effectively synonymous with encryption, converting readable information 
# (plaintext) to unintelligible nonsense text (ciphertext), which can only be read by reversing the process (decryption).

# Until modern times, cryptography referred almost exclusively to "encryption", which is the process of converting ordinary 
# information (called plaintext) into an unintelligible form (called ciphertext).[13] Decryption is the reverse, in other 
# words, moving from the unintelligible ciphertext back to plaintext. A cipher (or cypher) is a pair of algorithms that 
# carry out the encryption and the reversing decryption. The detailed operation of a cipher is controlled both by the 
# algorithm and, in each instance, by a "key"

# Alphabet shift ciphers are believed to have been used by Julius Caesar over 2,000 years ago.[6] This is an example 
# with k = 3. In other words, the letters in the alphabet are shifted three in one direction to encrypt and three in 
# the other direction to decrypt.

import string





# def julius_shiftciphers_enrcypt(fvPlainText, fvEncyptionKey):
#     "julius_shiftciphers_enrcypt"

#     tvCryptText = ""

#     for tI in range(len(fvPlainText)):
#         try:
#             tvCryptChar = fvEncyptionKey[fvPlainText[tI]]
#         except KeyError as e:
#             tvCryptChar = fvPlainText[tI]
#             pass
#         tvCryptText = tvCryptText + tvCryptChar

#     return tvCryptText




# def julius_shiftciphers_decrcypt(fvCryptText, fvEncyptionKey):
#     "julius_shiftciphers_decrcypt"

#     tvPlainText = ""

#     for tI in range(len(fvCryptText)):
#         try:
#             tvPlainChar = fvEncyptionKey[fvCryptText[tI]]
#         except KeyError as e:
#             tvPlainChar = fvCryptText[tI]
#             pass
#         tvPlainText = tvPlainText + tvPlainChar

#     return tvPlainText







# ####################################################################################
# ##############################________main_________#################################
# ####################################################################################


# tvCharList   = list(string.ascii_lowercase)
# tvShiftVal = 3


# tvEncryptDic = {}
# for tI in range(len(tvCharList) - tvShiftVal):
#     tvEncryptDic[tvCharList[tI]] = tvCharList[tI+tvShiftVal]

# for tJ in range(tvShiftVal):
#     tI = tI + 1
#     tvEncryptDic[tvCharList[tI]] = tvCharList[tJ]
    

# tvPlaintText = "send me a hundred more soldiers"
# tvCryptText = julius_shiftciphers_enrcypt(tvPlaintText, tvEncryptDic)
# print(tvCryptText)



# tvDecryptDic = {}
# for tI in range((len(tvCharList) - 1), -1, -1):
#     tvDecryptDic[tvCharList[tI]] = tvCharList[tI-tvShiftVal]

# tvDecrytPlainText = julius_shiftciphers_decrcypt(tvCryptText, tvDecryptDic)
# print(tvDecrytPlainText)

# if(tvPlaintText == tvDecrytPlainText):
#     print("Algorithms seems to be implemented correctly")


# print("Completed Sucessfully")




class ShiftCipherEncryptDecrypt:
    """ ShiftCipherEncryptDecrypt Basic class."""

    shiftValue  = 3

    def __init__(self):
        self.mvCharList = list(string.ascii_lowercase)

    def encrypt(self, fvChar):
        tvCryptChar    = fvChar
        tvCharIndexPos = None
        
        try:
            tvCharIndexPos = self.mvCharList.index(fvChar)
        except ValueError as e:
            pass
        
        if(tvCharIndexPos != None):
            tvShiftVal = ShiftCipherEncryptDecrypt.shiftValue
            tvCharSetLen = len(self.mvCharList)
            tvCryptChar = self.mvCharList[(tvCharIndexPos + tvShiftVal) % tvCharSetLen]
        
        return tvCryptChar
    

    def decrypt(self, fvCryptChar):
        tvPlainChar = fvCryptChar
        tvCharIndexPos = None

        try:
            tvCharIndexPos = self.mvCharList.index(fvCryptChar)
        except ValueError as e:
            pass

        if(tvCharIndexPos != None):
            tvShiftVal = ShiftCipherEncryptDecrypt.shiftValue
            tvCharSetLen = len(self.mvCharList)
            tvPlainChar = self.mvCharList[(tvCharIndexPos- tvShiftVal) % tvCharSetLen]
        
        return tvPlainChar





def julius_shiftciphers_enrcypt(fvPlainText):
    """ julius_shiftciphers_enrcypt """

    tvCryptText = ""
    tvEncrypt = ShiftCipherEncryptDecrypt()

    for tI in range(len(fvPlainText)):
        tvCryptChar = tvEncrypt.encrypt(fvPlainText[tI])
        tvCryptText = tvCryptText + tvCryptChar
    return tvCryptText




def julius_shiftciphers_decrcypt(fvCryptText):
    """ julius_shiftciphers_decrcypt """

    tvPlainText = ""
    tvDecrypt = ShiftCipherEncryptDecrypt()

    for tI in range(len(fvCryptText)):
        tvPlainChar = tvDecrypt.decrypt(fvCryptText[tI])
        tvPlainText = tvPlainText + tvPlainChar

    return tvPlainText








# ####################################################################################
# ##############################________main_________#################################
# ####################################################################################

tvPlaintText = "send me a hundred more soldiers"
tvCryptText = julius_shiftciphers_enrcypt(tvPlaintText)
print(tvCryptText)


tvDecrytPlainText = julius_shiftciphers_decrcypt(tvCryptText)
print(tvDecrytPlainText)

if(tvPlaintText == tvDecrytPlainText):
    print("Algorithms seems to be implemented correctly")

print("Completed Sucessfully")







