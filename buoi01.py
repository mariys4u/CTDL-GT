# Cau 1:

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")  # if doll == 1, then all dolls are opened
    else:
        openRussianDoll(doll - 1) # if doll != 1, then open the next doll

openRussianDoll(10) # print "All dolls are opened"

"---------------------------------------------------------------"

# Cau 2:
def firstMethod():
    secondMethod() # call the second method
    print("I am the first method")
def secondMethod():
    thirdMethod() # call the third method
    print("I am the second method")
def thirdMethod():
    fourthMethod()# call the fourth method
    print("I am the third method")
def fourthMethod(): # the fourth method is the last method
    print("I am the fourth method")
    
firstMethod() # print "I am the fourth method", "I am the third method", "I am the second method", "I am the first method"

"---------------------------------------------------------------"

# Cau 3:
def recursiveMethod(n):
    if n<1: # if n is less than 1
        print("n is less than 1") # print "n is less than 1"
    else:
        recursiveMethod(n-1) # call the recursive method
        print(n) # print n
        
recursiveMethod(4) # print 1, 2, 3, 4

"---------------------------------------------------------------"

# Cau 4:
def powerOfTwo(n):
    if n == 0:
        return 1 # if n is equal to 0, then return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2 # return the power of 2

print(powerOfTwo(4)) # 2 * 2 * 2 * 2 = 16

"---------------------------------------------------------------"

# Cau 5:
def factorial(n):
    if n == 0: # if n is equal to 0
        return 1 # return 1
    else:
        return n * factorial(n-1) # call the factorial method
print(factorial(5)) # 5 * 4 * 3 * 2 * 1 = 120

"---------------------------------------------------------------"

# Cau 6:
def fibonacci(n):
    if n == 1:
        return 1 # if n is equal to 1, return 1
    elif n == 2:
        return 1 # if n is equal to 2, return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) # call the fibonacci method  
print(fibonacci(10)) # 1 1 2 3 5 8 13 21 34 55

"---------------------------------------------------------------"

# Cau 7:
# How to find the sum of digits of a positive integer number using recursion ?

def sum_of_digits(n):
    if n == 0: # if n is equal to 0
        return 0 # return 0
    else:
        return (n % 10) + sum_of_digits(n // 10) # if n=123, return 3 + sum_of_digits(12) = 3 + 2 + sum_of_digits(1) = 3 + 2 + 1 + sum_of_digits(0) = 3 + 2 + 1 + 0 = 6
print (sum_of_digits(123)) # 1 + 2 + 3 = 6

"---------------------------------------------------------------"

# Cau 8:
# How to calculate power of a number using recursion?
def power(a,n): # a: base, n: exponent
    if n == 0:
        return 1
    else:
        return a * power(a,n-1)
print(power(2,3)) # 2 * 2 * 2 = 8

"---------------------------------------------------------------"

# Cau 9:
# How to find GCD ( Greatest Common Divisor) of two numbers using recursion?
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b) 
print(gcd(12,8)) # a = 12, b = 8, return gcd(8,12%8) = gcd(8,4) = gcd(4,8%4) = gcd(4,0) = 4

"---------------------------------------------------------------"
    
# Cau 10:
# How to convert a number from Decimal to Binary using recursion ?
def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2)) 
    
print(decimalToBinary(10)) # if n = 10, (0 + 10 * decimal_to_binary(5)) = (0 + 10 * (1 + 10 * decimal_to_binary(2))) = (0 + 10 * (1 + 10 * (0 + 10 * decimal_to_binary(1)))) = (0 + 10 * (1 + 10 * (0 + 10 * (1 + 10 * decimal_to_binary(0))))) = (0 + 10 * (1 + 10 * (0 + 10 * (1 + 10 * (0))))) = 1010, 1010 is the binary number of 10
