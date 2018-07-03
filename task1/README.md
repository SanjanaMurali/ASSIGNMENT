MISSING NUMBER IN ARRAY

This is a python 2.7 program to find the missing number in given integer array of 1 to 100

Prerequisties:

 1.This can be run on ubuntu 16.04 using command :
   python file name
   
 2.random : This module implements pseudo-random number generators for various 
   distribution. This is used here to create an array of random numbers between 1-100.
   link: https://docs.python.org/2/library/random.html
   
Logic:

sum of first hundred natural numbers is [n*(n+1)]/2 where n=100.
Then sum of array with missing number is found.
The difference between two is found to get the missing number.
