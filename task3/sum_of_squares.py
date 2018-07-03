# python program to find the difference between the square of the sum of the first one hundred natural numbers and the sum of the squares

n=100

# sum of squares of natural numbers using formula [n(n+1)(2n+1)]/6
sum_of_squares=(n*(n+1)*((2*n)+1))/6
print "sum of square of first hundred natural numbers",sum_of_squares

#sum of first 100 natural numbers using formula (n(n+1))/2
sum=(n*(n+1))/2
square_of_sum=sum*sum
print "square of sum of first hundred natural numbers"square_of_sum

#difference
difference=square_of_sum-sum_of_squares
print "difference between the square of the sum of the first one hundred natural numbers and the sum of the squares",difference
