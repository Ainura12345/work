# Write a Java program and compute the sum of the digits of an integer.


def digit_sum(n):
   sum = 0
   while n>0:
       remainder=n%10
       sum=sum+remainder
       n= n // 10
   return sum
number = int(input())
print (digit_sum(number))
