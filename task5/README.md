SUM OF PRIME NUMBERS BELOW 2 MILLION

Python program to print sum of prime numbers below 2 million. Sieve of Eratosthenes algorithm is used to find the prime numbers.


Prerequisties:
 1.This can be run on ubuntu 16.04 using command :
   python file name

Logic:
To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

    1.Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
    2.Initially, let p equal 2, the smallest prime number.
    3.Enumerate the multiples of p by counting to n from 2p in increments of p, and 
      mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not
      be marked).
    4.Find the first number greater than p in the list that is not marked. If 
      there was no such number, stop. Otherwise, let p now equal this new 
      number(which is the next prime), and repeat from step 3.
    5.When the algorithm terminates, the numbers remaining not marked in the list
      are all the primes below n.

    link : https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

