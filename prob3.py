import math

def factor(num):
    for x in range(num+1, 1, -1): # x loops from 2 to number backwards
        for y in range(2,int(math.sqrt(num+1))): #y loops from 2 to number forwards
            if x * y  == num: #if x and y multiply to number...
                if isprime(x) == True: #tests if num is prime
                    return x
                    

def isprime(num):
    for x in range(int(math.sqrt(num)), 1, -1): #same process as factor
        for y in range(2,int(math.sqrt(num+1))):
            if x * y == num: #if x and y multiply to number,
                return False #then by definition number is not prime
    else:
        return True

print factor(600851475143)

#Come back to this later :)
#Iterating through the really large number doesn't work
#Think of a different way! Maybe prime factorization?
