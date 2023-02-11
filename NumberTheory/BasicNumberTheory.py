# Every positive integer a is divisible by the trivial divisors 1 and a. The nontrivial
# divisors of a are the factors of a. For example, the factors of 20 are 2, 4, 5, and 10.
# Prime and composite numbers

# An integer a > 1 whose only divisors are the trivial divisors 1 and a is a prime
# number or, more simply, a prime. Primes have many special properties and play a
# critical role in number theory. The first 20 primes, in order, are
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71

# An integer a > 1 that is not prime is a composite number or, more simply, a 
# composite. For example, 39 is composite because 3|39.



# XOR:The XOR operator outputs a 1 whenever the inputs do not match, which occurs when 
# one of the two inputs is exclusively true.

# 0 XOR 0 = 0
# 0 XOR 1 = 1
# 1 XOR 0 = 1
# 1 XOR 1 = 0

# OR: The OR operator is also known as logical disjunction. It outputs a 1 whenever one or more of 
# its inputs are 1. Here is the truth table:
# 0 OR 0 = 0
# 0 OR 1 = 1
# 1 OR 0 = 1
# 1 OR 1 = 1


# Division
#---------
# Let Z be the set of integers.
# Z = {.... -3, -2, -1, 0, 1, 2, 3 .....}
# Let x and y are any two integers, that is x, y $ Z.
# We say that x divides y, and write x|y, if there is q $ Z such that
#       y = qx

# Quotient and reminder
#----------------------
# Let x and y are any two integers, that is x, y $ Z.
# It is possible to find integers q and r such that
#   y = qx + r
# where 0<= r <= x -1
# The integer q is called quotient and r is called reminder.
# we can write r = y mod x

# If we replace y by y mod x, we say that y is reduced modulo x.
# r' = (y mod x) mod x
# What it signifiy?. I do not know.

# Greatest common divisor
#------------------------
# The gcd of x, y $ X is positive integers denoted by gcd(x,y) such that
#   gcd(x,y)|x and gcd(x,y)|y;
#   if q|x and q|y, then q|gcd(x,y).

# It is known that given any x,y $ Z there exist r,s $  such that
#   rx + sy = gcd(x,y)


import math



def isPrime(fvNumber):
    """A prime number (or a prime) is a natural number greater than 1 that is not a 
    product of two smaller natural numbers. The property of being prime is called 
    primality. A simple but slow method of checking the primality of a given number
    n, called trial division, tests whether n is a multiple of any integer between 
    2 and sqrt(n)."""

    tvSqrtVal = math.sqrt(fvNumber)
    tvEndRange = int(math.ceil(tvSqrtVal))
    isPrime = True
    tI = 2
    while tI <= tvEndRange:
        tMod = (fvNumber % tI)
        if(tMod == 0):
            isPrime = False
            break
        tI = tI + 1

    return isPrime



def euclid_gcd(fvFirst, fvSecond):
    """ euclid_gcd 
    gcd(int a, int b)
        if (a == b) return a;
        if (a < b) return gcd(a, b - a);
    """
    
    if(fvFirst == 0):
        return fvSecond
    
    return euclid_gcd(fvSecond % fvFirst, fvFirst)









# ####################################################################################
# ##############################________main_________#################################
# ####################################################################################


tvNumberList = [3,4,5,6,7]
for aNumber in tvNumberList:
    tvOut = isPrime(aNumber)
    print(str(aNumber) + " isPrime: " + str(tvOut))



tvFirst  = 24
tvSecond = 10
tvGcdValue = euclid_gcd(tvFirst, tvSecond)
print(tvGcdValue)


# we need to solve gcd(b, 192) = 1
tvOuputList = []
for i in range(2, 192):
    tvGcdValue = euclid_gcd(i, 192)
    if(tvGcdValue == 1):
        tvOuputList.append(i)

print(tvOuputList)






print("Completed Sucessfully")
