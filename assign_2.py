

nterms = 17
def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))  

# check if the number of terms is valid  
if nterms <= 0:  
   print("nterms value should be positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(fibo(i))  