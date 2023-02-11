# Cryptography prior to the modern age was effectively synonymous with encryption, converting readable information 
# (plaintext) to unintelligible nonsense text (ciphertext), which can only be read by reversing the process (decryption).

# Until modern times, cryptography referred almost exclusively to "encryption", which is the process of converting ordinary 
# information (called plaintext) into an unintelligible form (called ciphertext).[13] Decryption is the reverse, in other 
# words, moving from the unintelligible ciphertext back to plaintext. A cipher (or cypher) is a pair of algorithms that 
# carry out the encryption and the reversing decryption. The detailed operation of a cipher is controlled both by the 
# algorithm and, in each instance, by a "key"



import string



# Julius Ciphers Based Algorithm
#-------------------------------
# Alphabet shift ciphers are believed to have been used by Julius Caesar over 2,000 years 
# ago.[6] This is an example  with k = 3. In other words, the letters in the alphabet 
# are shifted three in one direction to encrypt and three in the other direction to 
# decrypt.

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










# Affline Cipher Based Algorithm
# ------------------------------

# Now, what people started thinking is that probably is there any way of extending the key
# space so because that is one of the problems in case of shift cipher the key space is small.
# Well, it is possible to do that and for that we come to affine ciphers.
# For k = (a, b)
# e(a,b)(x) = (ax + b) mod 26
# d(a,b)(y) = a^-1(y - b) mod 26
# The first component A over here has to be co-prime to 26 that is the greatest common divisor
# of a and 26 has to be 1.


class AfflineCipherEncryptDecrypt:
    """ AfflineCipherEncryptDecrypt Basic class."""

    def __init__(self):
        self.mvCharList = list(string.ascii_lowercase)


    def encryptMethod(self, fvCharPosition):
        # e(15,18)(x) = (15*fvChar[index] + 18) mod 26

        tvCryptChar   = (15*fvCharPosition + 18) % 26
        return self.mvCharList[tvCryptChar]
    

    def decryptMethod(self, fvCharPosition):
        # e(15,18)(y) = (7*fvChar[index] + 4) mod 26

        tvPlainChar   = (7*fvCharPosition + 4) % 26
        return self.mvCharList[tvPlainChar]
    
    
    def encrypt(self, fvChar):
        tvCryptChar    = fvChar
        tvCharIndexPos = None
        
        try:
            tvCharIndexPos = self.mvCharList.index(fvChar)
        except ValueError as e:
            pass
        
        if(tvCharIndexPos != None):
            tvCryptChar = self.encryptMethod(tvCharIndexPos)

        return tvCryptChar
    

    def decrypt(self, fvCryptChar):
        tvPlainChar = fvCryptChar
        tvCharIndexPos = None

        try:
            tvCharIndexPos = self.mvCharList.index(fvCryptChar)
        except ValueError as e:
            pass

        if(tvCharIndexPos != None):
            tvPlainChar = self.decryptMethod(tvCharIndexPos)
        
        return tvPlainChar





def affline_shiftciphers_enrcypt(fvPlainText):
    """ affline_shiftciphers_enrcypt """

    tvCryptText = ""
    tvEncrypt = AfflineCipherEncryptDecrypt()

    for tI in range(len(fvPlainText)):
        tvCryptChar = tvEncrypt.encrypt(fvPlainText[tI])
        tvCryptText = tvCryptText + tvCryptChar
    return tvCryptText




def affline_shiftciphers_decrcypt(fvCryptText):
    """ affline_shiftciphers_decrcypt """

    tvPlainText = ""
    tvDecrypt = AfflineCipherEncryptDecrypt()

    for tI in range(len(fvCryptText)):
        tvPlainChar = tvDecrypt.decrypt(fvCryptText[tI])
        tvPlainText = tvPlainText + tvPlainChar

    return tvPlainText







# Vigenère Cipher Based Algorithm
# -------------------------------

# The Vigenère cipher is a method of encrypting alphabetic text by using a 
# series of interwoven Caesar ciphers, based on the letters of a keyword. 
# It employs a form of polyalphabetic substitution.

# First described by Giovan Battista Bellaso in 1553, the cipher is easy to 
# understand and implement, but it resisted all attempts to break it until 1863, 
# three centuries later. This earned it the description le chiffrage indéchiffrable 
# (French for 'the indecipherable cipher'). Many people have tried to implement 
# encryption schemes that are essentially Vigenère ciphers.[3] In 1863, Friedrich 
# Kasiski was the first to publish a general method of deciphering Vigenère ciphers.

# Input : Plaintext :   GEEKSFORGEEKS
#              Keyword :  AYUSH
# Output : Ciphertext :  GCYCZFMLYLEIM

# For generating key, the given keyword is repeated in a circular manner until it matches 
# the length of  the plain text.

# The keyword "AYUSH" generates the key "AYUSHAYUSHAYU"
# The plain text is then encrypted using the processexplained below.


# Encryption
# The plaintext(P) and key(K) are added modulo 26.
#   Ei = (Pi + Ki) mod 26

# Decryption
#   Di = (Ei - Ki + 26) mod 26







class VigenereCipherEncryptDecrypt:
    """ VigenereCipherEncryptDecrypt Basic class."""

    def __init__(self):
        self.mvCharList = list(string.ascii_lowercase)


    def encryptMethod(self, fvCharPositionInText, fvCharPosInKey):
        # e(p,k)(x) = (p + k) mod 26

        tvCryptChar   = (fvCharPositionInText + fvCharPosInKey) % 26
        return self.mvCharList[tvCryptChar]
    

    def decryptMethod(self, fvCharPositionInEncrypt, fvCharPosInKey):
        # d(y) = (e -k + 26) mod 26

        tvPlainChar   = (fvCharPositionInEncrypt - fvCharPosInKey + 26) % 26
        return self.mvCharList[tvPlainChar]
    
    
    def encrypt(self, fvChar, fvKeyChar):
        tvCryptChar    = fvChar
        tvCharIndexPos = None
        tvCharInKeyPos = None

        try:
            tvCharIndexPos = self.mvCharList.index(fvChar)
            tvCharInKeyPos = self.mvCharList.index(fvKeyChar)
        except ValueError as e:
            pass
        
        if( (tvCharIndexPos != None) and (tvCharInKeyPos != None) ):
            tvCryptChar = self.encryptMethod(tvCharIndexPos, tvCharInKeyPos)

        return tvCryptChar
    

    def decrypt(self, fvCryptChar, fvKeyChar):
        tvPlainChar = fvCryptChar
        tvCharIndexPos = None
        tvCharInKeyPos = None

        try:
            tvCharIndexPos = self.mvCharList.index(fvCryptChar)
            tvCharInKeyPos = self.mvCharList.index(fvKeyChar)
        except ValueError as e:
            pass

        if( (tvCharIndexPos != None) and (tvCharInKeyPos != None) ):
            tvPlainChar = self.decryptMethod(tvCharIndexPos, tvCharInKeyPos)
        
        return tvPlainChar



def generate_key_for_vigenere_cipher(fvPlainText, fvKeyWord):
    """ generate_key_for_vigenere_cipher """
    # For generating key, the given keyword is repeated in a 
    # circular manner until it matches the length of  the plain 
    # text.

    tvFinalKeyWord = fvKeyWord
    isEqualLength = False

    while True:
        for tI in range(len(fvKeyWord)):
            tvFinalKeyWord = tvFinalKeyWord + fvKeyWord[tI]
            if(len(tvFinalKeyWord) == len(fvPlainText)):
                isEqualLength = True
                break
        if(isEqualLength == True):
            break

    return tvFinalKeyWord








def vigenere_shiftciphers_enrcypt(fvPlainText, fvKeyText):
    """ vigenere_shiftciphers_enrcypt """

    tvCryptText = ""
    tvEncrypt = VigenereCipherEncryptDecrypt()

    for tI in range(len(fvPlainText)):
        tvCryptChar = tvEncrypt.encrypt(fvPlainText[tI], fvKeyText[tI])
        tvCryptText = tvCryptText + tvCryptChar
    return tvCryptText




def vigenere_shiftciphers_decrcypt(fvCryptText, fvKeyText):
    """ vigenere_shiftciphers_decrcypt """

    tvPlainText = ""
    tvDecrypt = VigenereCipherEncryptDecrypt()

    for tI in range(len(fvCryptText)):
        tvPlainChar = tvDecrypt.decrypt(fvCryptText[tI], fvKeyText[tI])
        tvPlainText = tvPlainText + tvPlainChar

    return tvPlainText









# RSA CryptoSystem Algorithm
# --------------------------

# RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission. 
# It is also one of the oldest. The acronym "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, 
# who publicly described the algorithm in 1977. An equivalent system was developed secretly in 1973 at Government 
# Communications Headquarters (GCHQ) (the British signals intelligence agency) by the English mathematician Clifford 
# Cocks. That system was declassified in 1997.

# In a public-key cryptosystem, the encryption key is public and distinct from the decryption key, which is kept 
# secret (private). An RSA user creates and publishes a public key based on two large prime numbers, along with 
# an auxiliary value. The prime numbers are kept secret. Messages can be encrypted by anyone, via the public key, 
# but can only be decoded by someone who knows the prime numbers.

# The security of RSA relies on the practical difficulty of factoring the product of two large prime numbers, 
# the "factoring problem". Breaking RSA encryption is known as the RSA problem. Whether it is as difficult as 
# the factoring problem is an open question. There are no published methods to defeat the system if a large 
# enough key is used.

# RSA is a relatively slow algorithm. Because of this, it is not commonly used to directly encrypt user data. 
# More often, RSA is used to transmit shared keys for symmetric-key cryptography, which are then used for 
# bulk encryption–decryption.

# RSA algorithm is an asymmetric cryptography algorithm. Asymmetric actually means that it works on two 
# different keys i.e. Public Key and Private Key. As the name describes that the Public Key is given to 
# everyone and the Private key is kept private.


# Step1: Let n = pq, where p and q are prime numbers.


def rsa_key_generation():
    """rsa_key_generation"""

    # In real world, we need to generate these big primes numbers. 
    p = 13
    q = 17

    n = p*q

    thetaN = (p-1)*(q-1)

    # Now we have to choose b such that gcd(b, thetaN) = 1
    # Below 'tvOuputList' contains the probable solution for this
    # and 'b' is one of solution for above equation.

    # # we need to solve gcd(b, thetaN) = 1
    # tvOuputList = []
    # for i in range(2, thetaN):
    #     tvGcdValue = euclid_gcd(i, thetaN)
    #     if(tvGcdValue == 1):
    #         tvOuputList.append(i)

    # print(tvOuputList)

    b = 55

    # ab =(modulo)1. This means a is inverse of b .i.e. a = b^-1
    a  = 7

    tvKeyComponenDic = {}
    tvKeyComponenDic['n'] = n
    tvKeyComponenDic['p'] = p
    tvKeyComponenDic['q'] = q
    tvKeyComponenDic['a'] = a
    tvKeyComponenDic['b'] = b


    # Public key: (n, b)
    # Private Key: (p,q,a)

    return tvKeyComponenDic







def rsa_encyption(fvInputNumber, fvKeyComponenDic):
    """rsa_encyption. ek(x) = x^b mod n"""
    
    b = fvKeyComponenDic['b']
    n = fvKeyComponenDic['n']

    tvEncryptVal = (fvInputNumber**b) % n

    return tvEncryptVal




def rsa_decryptipon(fvEncrypyNumber, fvKeyComponenDic):
    """rsa_encyption. dk(y) = y^a mod n"""
    
    a = fvKeyComponenDic['a']
    n = fvKeyComponenDic['n']

    tvOriginalVal = (fvEncrypyNumber**a) % n

    return tvOriginalVal

















# ####################################################################################
# ##############################________main_________#################################
# ####################################################################################

# tvPlaintText = "send me a hundred more soldiers"

# # Julius Cipher
# tvCryptText = julius_shiftciphers_enrcypt(tvPlaintText)
# print(tvCryptText)
# tvDecrytPlainText = julius_shiftciphers_decrcypt(tvCryptText)
# print(tvDecrytPlainText)
# if(tvPlaintText == tvDecrytPlainText):
#     print("Algorithms seems to be implemented correctly")


# # Affline Cipher
# tvPlaintText = "hey buddy how are you and whats up"
# tvCryptText = affline_shiftciphers_enrcypt(tvPlaintText)
# print(tvCryptText)
# tvDecrytPlainText = affline_shiftciphers_decrcypt(tvCryptText)
# print(tvDecrytPlainText)
# if(tvPlaintText == tvDecrytPlainText):
#     print("Algorithms seems to be implemented correctly")


# # Vigenere Cipher
# tvKeyword = "samanyumahika"
# tvPlaintText = "i am doing good with basics of cryptography"

# tvGeneratedKeyWord = generate_key_for_vigenere_cipher(tvPlaintText, tvKeyword)

# tvCryptText = vigenere_shiftciphers_enrcypt(tvPlaintText, tvGeneratedKeyWord)
# print(tvCryptText)
# tvDecrytPlainText = vigenere_shiftciphers_decrcypt(tvCryptText, tvGeneratedKeyWord)
# print(tvDecrytPlainText)
# if(tvPlaintText == tvDecrytPlainText):
#     print("Algorithms seems to be implemented correctly")




# RSA Algorihm
tvPlaintText = "rsa is asymetric cryptography system and works with public and private key"
tvNumber  = 128
tvKeyComponenDic = rsa_key_generation()
tvEncryptedText = rsa_encyption(tvNumber, tvKeyComponenDic)
print(tvEncryptedText)

tvDecrytPlainNumber = rsa_decryptipon(tvEncryptedText, tvKeyComponenDic)
if(tvNumber == tvDecrytPlainNumber):
    print("Algorithms seems to be implemented correctly")




print("Completed Sucessfully")
