#!/usr/bin/python
#Date: 08/28/2012
#Finding prime number up to the limit

import math

def sieveOfEratosthenes(limit):
    sieve = [True] * (limit+1)
    multiple = 0
    counter = 2

    for i in range(2, limit):
        if sieve[i] == True:
            counter = 2
            multiple = i * counter
            while multiple < limit:
                sieve[multiple] = False
                counter += 1
                multiple = i * counter
    
    prime = []
    for i in range(2, limit):
        if sieve[i] == True:
            prime.append(i)
    print prime


def sieveOfAtkin(limit):
    sieve = [False] * (limit+1)
    sieve[2] = True
    sieve[3] = True
    limitSqrt = int(math.sqrt(limit))

    for x in range(1, limitSqrt+1):
        for y in range(1, limitSqrt+1):

            n = int((4 * math.pow(x,2)) + math.pow(y,2))
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = int((3 * math.pow(x,2)) + math.pow(y,2))
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = int((3 * math.pow(x,2)) - math.pow(y,2))
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    for n in range(5, limitSqrt):
        if sieve[n] == True:
            x = int(math.pow(n,2))
            i = x
            while i < limit:
                sieve[i] = False
                i += x
    
    prime = []
    for i in range(2, limit):
        if sieve[i] == True:
            prime.append(i)

    print prime

def main():
    limit = raw_input()    
    while limit != "exit":
        print "Sieve Of Eratosthenes method: "
        sieveOfEratosthenes(int(limit))
        print "Sieve of Atkin method: "
        sieveOfAtkin(int(limit))
        limit = raw_input()
    

if __name__ == "__main__":
    main()



