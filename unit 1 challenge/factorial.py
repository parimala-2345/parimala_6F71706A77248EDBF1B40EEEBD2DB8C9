def fact_rec(n):
 if n==0 or n==1:
    return 1
 else:
    return n*fact_rec(n-1)

number = 2
res = fact_rec(number)

print("The factorial of {} is {}".format(number,res))
num = int(input("Enter a number: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)