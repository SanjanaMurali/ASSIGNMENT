# python program to print sum of prime numbers less than 2 million
# Sieve of Eratosthenes algorithm is used to find prime numbers

# function to find sum of prime numbers less than 2 million
def sum_of_primes():
  n=2000000
#all 2 miilon entries are entered as True
  prime=[True for i in range(2000000)]
  num=2
  while (num*num<=n):
    if prime[num]==True:
#multiples of num are set as false
       for i in range(num*2,n,num):
         prime[i]=False
    num+=1
  c=[]
#loop to find prime numbers
#prime numbers are those which are True
  for p in range(2,n):
    if prime[p]==True:
       c.append(p)
  print sum(c)

sum_of_primes()
    
