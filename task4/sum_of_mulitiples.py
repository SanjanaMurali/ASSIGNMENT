# python program to find sum of all multiples of 4 and 5 below 1000

#function to find sum of n natural numbers
def sum_of_numbers(k):
  total=(k*(k+1))/2
  return total
k1=999/4
k2=999/5
k3=999/20
sum_of_multiples=(4*sum_of_numbers(k1))+(5*sum_of_numbers(k2))-(20*sum_of_numbers(k3))
print "Sum of all multiples of 4 and 5 below 1000 is \n",sum_of_multiples
