# def foo(array):  # ham foo co tham so la mang
#     sum = 0  # khoi tao bien sum = 0
#     product = 1  # khoi tao bien product = 1
#     for i in array:  # duyet mang array
#         sum += i  # sum = sum + i
#     for i in array:  # duyet mang array
#         product *= i  # product = product * i
#     print(
#         "Sum = " + str(sum) + ", Product = " + str(product)
#     )  # In ra kết quả tổng và sản phẩm của mảng array


# foo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # goi ham foo -> trả kết quả ra màn hình Sum = 55, Product = 3628800

"------------------------------------------------------------------------"

# def printPairs(array): # ham printPairs co tham so la mang
#     for i in array: # duyet mang array
#         for j in array: # duyet mang array
#             print(str(i) + "," + str(j)) # in ra cac cap phan tu cua mang array


# printPairs([1, 2, 3, 4, 5]) # goi ham printPairs -> trả kết quả ra màn hình 1,1 1,2 1,3 1,4 1,5 2,1 2,2 2,3 2,4 2,5 3,1 3,2 3,3 3,4 3,5 4,1 4,2 4,3 4,4 4,5 5,1 5,2 5,3 5,4 5,5

"------------------------------------------------------------------------"

# def printUnorderedPairs(array): # ham printUnorderedPairs co tham so la mang
#     for i in range(0, len(array)): # duyet mang array
#         for j in range(i + 1, len(array)): # duyet mang array
#             print(str(array[i]) + "," + str(array[j])) # in ra cac cap phan tu cua mang array


# printUnorderedPairs([1, 2, 3, 4, 5]) # goi ham printUnorderedPairs -> trả kết quả ra màn hình 1,2 1,3 1,4 1,5 2,3 2,4 2,5 3,4 3,5 4,5

"------------------------------------------------------------------------"

# def printUnorderedPairs(arrayA, arrayB): # ham printUnorderedPairs co tham so la 2 mang
#     for i in range(0, len(arrayA)): # duyet mang arrayA
#         for j in range(0, len(arrayB)): # duyet mang arrayB
#             if arrayA[i] < arrayB[j]: # neu phan tu arrayA[i] nho hon phan tu arrayB[j]
#                 print(str(arrayA[i]) + "," + str(arrayB[j])) # in ra cap phan tu arrayA[i] va arrayB[j]


# printUnorderedPairs([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]) # goi ham printUnorderedPairs -> trả kết quả ra màn hình 1,6 1,7 1,8 1,9 1,10 2,6 2,7 2,8 2,9 2,10 3,6 3,7 3,8 3,9 3,10 4,6 4,7 4,8 4,9 4,10 5,6 5,7 5,8 5,9 5,10


# def printUnorderedPairs(arrayA, arrayB): # ham printUnorderedPairs co tham so la 2 mang
#     for i in range(len(arrayA)): # duyet mang arrayA
#         for j in range(len(arrayB)): # duyet mang arrayB
#             for k in range(0, 100000): # duyet mang arrayB
#                 print(str(arrayA[i]) + "," + str(arrayB[j])) # in ra cap phan tu arrayA[i] va arrayB[j]

# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# printUnorderedPairs(a, b) # goi ham printUnorderedPairs -> trả kết quả ra màn hình 1,6 1,7 1,8 1,9 1,10 2,6 2,7 2,8 2,9 2,10 3,6 3,7 3,8 3,9 3,10 4,6 4,7 4,8 4,9 4,10 5,6 5,7 5,8 5,9 5,10

"------------------------------------------------------------------------"


# def reverse(array): # ham reverse co tham so la mang
#     for i in range(0, int(len(array) / 2)): # duyet mang array
#         other = len(array) - i - 1 # khoi tao bien other = do dai mang - i - 1

#         temp = array[i] # khoi tao bien temp = array[i]

#         array[i] = array[other] # array[i] = array[other]

#         array[other] = temp # array[other] = temp

#     print(array) # in ra mang array


# reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # goi ham reverse -> trả kết quả ra màn hình [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

"------------------------------------------------------------------------"

# def factorial(n): # ham factorial co tham so la n
#     if n < 0: # neu n < 0
#         return -1 # tra ve -1
#     elif n == 0: # neu n = 0
#         return 1 # tra ve 1
#     else: # neu khong
#         return n * factorial(n - 1) # tra ve n * ham factorial(n - 1)

# print(factorial(5)) # goi ham factorial -> trả kết quả ra màn hình 120

"------------------------------------------------------------------------"

# def allFib(n): # ham allFib co tham so la n
#     for i in range(n): # duyet mang n
#         print(str(i) + ":" + str(fib(i))) # in ra i va fib(i)


# def fib(n): # ham fib co tham so la n
#     if n <= 0: # neu n <= 0
#         return 0 # tra ve 0
#     elif n == 1: # neu n = 1
#         return 1 # tra ve 1
#     return fib(n - 1) + fib(n - 2) # tra ve ham fib(n - 1) + ham fib(n - 2)

"------------------------------------------------------------------------"

# def powerOf2(n): # ham powerOf2 co tham so la n
#     if n < 1: # neu n < 1
#         return 0 # tra ve 0
#     elif n == 1: # neu n = 1
#         return 1 # tra ve 1
#     else: # neu khong
#         prev = powerOf2(int(n / 2)) # khoi tao bien prev = ham powerOf2(n / 2)
#         curr = prev * 2 # khoi tao bien curr = prev * 2
#         print(curr) # in ra curr
#         return curr # tra ve curr

# powerOf2(50)

"------------------------------------------------------------------------"
# Find Number of Days Above Average Temperature

# numDays = int(input("How many days' temperatures? "))  # nhap so ngay
# total = 0  # khoi tao bien total = 0
# temp = []  # khoi tao mang temps
# for i in range(numDays):  # duyet mang numdays
#     nextDays = int(input("Day" + str(i + 1) + "'s high temp: "))
#     temp.append(nextDays)  # them phan tu nextDays vao mang temps
#     total += temp[i]  # total = total + temps[i]
# average = round(total / numDays, 2)  # khoi tao bien average = total / numdays
# print("Average = " + str(average))  # in ra average

# above = 0  # khoi tao bien above = 0
# for i in range(numDays):  # duyet mang numdays
#     if temp[i] > average:  # neu temps[i] > average
#         above += 1  # above = above + 1
# print(str(above) + " days above average")  # in ra above

# -------------------------------------------------------------------------

# Example 1                                   -               #Example 2
# How many days' temperatures? 2              -               How many days' temperatures? 4
# Day1's high temp: 1                         -               Day1's high temp: 20
# Day2's high temp: 2                         -               Day2's high temp: 21
# Average = 1.5                               -               Day3's high temp: 50
# 1 days above average                        -               Day4's high temp: 60
#                                             -               Average = 37.75
#                                             -               2 days above average

"------------------------------------------------------------------------"

# def twoSum(nums, target): # ham twoSum co tham so la nums va target
#     for i in range(len(nums)): # duyet mang nums
#         for j in range(i + 1, len(nums)): # duyet mang nums
#             if nums[j] == target - nums[i]: # neu nums[j] = target - nums[i]
#                 return [i, j] # tra ve [i, j]

# print(twoSum([3, 2, 4], 6)) # goi ham twoSum -> trả kết quả ra màn hình [1, 2]

"------------------------------------------------------------------------"

# rotate Matrix 90 degree by an NxN matrix

# def rotateMatrix(matrix): # ham rotateMatrix co tham so la matrix
#     if len(matrix) == 0 or len(matrix) != len(matrix[0]): # neu do dai mang matrix = 0 hoac do dai mang matrix khong bang do dai mang matrix[0]
#         return False # tra ve False
#     n = len(matrix) # khoi tao bien n = do dai mang matrix
#     for layer in range(int(n / 2)): # duyet mang n / 2
#         first = layer # khoi tao bien first = layer
#         last = n - 1 - layer # khoi tao bien last = n - 1 - layer
#         for i in range(first, last): # duyet mang first den last
#             offset = i - first # khoi tao bien offset = i - first
#             top = matrix[first][i] # khoi tao bien top = matrix[first][i]
#             matrix[first][i] = matrix[last - offset][first] # matrix[first][i] = matrix[last - offset][first]
#             matrix[last - offset][first] = matrix[last][last - offset] # matrix[last - offset][first] = matrix[last][last - offset]
#             matrix[last][last - offset] = matrix[i][last] # matrix[last][last - offset] = matrix[i][last]
#             matrix[i][last] = top # matrix[i][last] = top
#     return matrix # tra ve matrix

# print(rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # goi ham rotateMatrix -> trả kết quả ra màn hình [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

"------------------------------------------------------------------------"

# from array import *

# my_array = array("i") # khoi tao mang my_array
# print(my_array) # in ra mang my_array -> array('i')
# my_array1 = array("i", [1, 2, 3, 4, 5]) # khoi tao mang my_array1
# print(my_array1) -> array('i', [1, 2, 3, 4, 5])

"------------------------------------------------------------------------"

# import numpy as np

# np_array = np.array([], dtype=int) # khoi tao mang np_array
# print(np_array) # in ra mang np_array -> []
# np_array1 = np.array([1, 2, 3, 4]) # khoi tao mang np_array1
# print(np_array1) # in ra mang np_array1 -> [1 2 3 4]

"------------------------------------------------------------------------"

# import array as arr

# my_array1 = arr.array("i", [1, 2, 3, 4]) # khoi tao mang my_array1
# print(my_array1) # in ra mang my_array1 -> array('i', [1, 2, 3, 4])
# my_array1.insert(0, 6) # them phan tu 6 vao vi tri 0 cua mang my_array1
# print(my_array1) # in ra mang my_array1 -> array('i', [6, 1, 2, 3, 4])

"------------------------------------------------------------------------"
# from array import *
# arr1 = array("i", [1, 2, 3, 4, 5, 6])
# arr2 = array("d", [1.3, 1.5, 1.6])

# print(arr2) # in ra mang arr2 -> array('d', [1.3, 1.5, 1.6])
# arr1.insert(2,9) # them phan tu 9 vao vi tri 2 cua mang arr1
# print(arr1) # in ra mang arr1 -> array('i', [1, 2, 9, 3, 4, 5, 6])


# def traverseArray(array): # ham traverseArray co tham so la array
#     for i in array: # duyet mang array
#         print(i) # in ra i
# traverseArray(arr1) # goi ham traverseArray -> trả kết quả ra màn hình 1 2 9 3 4 5 6


"------------------------------------------------------------------------"
# from array import *
# arr1 = array("i", [1, 2, 3, 4, 5, 6])


# def accessElement(array, index): # ham accessElement co tham so la array va index
#     if index > len(array): # neu index > do dai mang array
#         print("There is no element at this index") # in ra There is no element at this index
#     else: # neu khong
#         print(array[index]) # in ra phan tu tai vi tri index cua mang array
# accessElement(arr1, 4) # goi ham accessElement -> trả kết quả ra màn hình 5

"------------------------------------------------------------------------"

# from array import *
# my_array1 = array("i", [1, 2, 3, 4, 5])


# def linear_search(arr, target): # ham linear_search co tham so la arr va target
#     for i in range(len(arr)): # duyet mang arr
#         if arr[i] == target: # neu phan tu arr[i] = target
#             return i # tra ve i
#     return -1 # tra ve -1
# print(linear_search(my_array1, 8)) # goi ham linear_search -> trả kết quả ra màn hình -1

"------------------------------------------------------------------------"

# from array import *
# arr1 = array("i", [1, 2, 3, 4, 5, 6]) # khoi tao mang arr1
# arr1.remove(4) # xoa phan tu 4 khoi mang arr1
# print(arr1) # in ra mang arr1 -> array('i', [1, 2, 3, 5, 6])

"----------------------------------------------------------------------------"

# Anser 10 questions
# Xoá dấu """ """ # để chạy code
""" 
# 1. Create an array and traverse.
from array import *

arr = array("i", [1, 2, 3, 4, 5])
print(arr) # in ra mang arr -> array('i', [1, 2, 3, 4, 5])

# 2. Access individual elements through indexes.
# print("Question 2") # in ra Question 2
# print(arr[3]) # in ra phan tu tai vi tri 3 cua mang arr -> 4

# 3. Append a value to the array.
print("Question 3") # in ra Question 3
arr.append(6) # them phan tu 6 vao cuoi mang arr
print(arr) # in ra mang arr -> array('i', [1, 2, 3, 4, 5, 6])

# 4. Insert value in an array.
print("Question 4") # in ra Question 4
arr.insert(3, 11) # them phan tu 11 vao vi tri 3 cua mang arr
print(arr) # in ra mang arr -> array('i', [1, 2, 3, 11, 4, 5, 6])

# 5. Extend array by another array.
print("Question 5") # in ra Question 5
arr1 = array("i", [10, 11, 12]) # khoi tao mang arr1
arr.extend(arr1) # them mang arr1 vao mang arr
print(arr) # in ra mang arr -> array('i', [1, 2, 3, 11, 4, 5, 6, 10, 11, 12])

# 6. Add items from list into array.
print("Question 6") # in ra Question 6
arr1 = [20, 21, 22] # khoi tao mang arr1
arr.fromlist(arr1) # them mang arr1 vao mang arr
print(arr) # in ra mang arr -> array('i', [1, 2, 3, 11, 4, 5, 6, 10, 11, 12, 20, 21, 22])

# 7. Remove any array element.
print("Question 7") # in ra Question 7
arr.remove(11) # xoa phan tu 11 khoi mang arr
print(arr) # in ra mang arr -> array('i', [1, 2, 3, 4, 5, 6, 10, 11, 12, 20, 21, 22])

# 8. Remove last array element.
print("Question 8") # in ra Question 8
arr.pop() # xoa phan tu cuoi cung khoi mang arr
print(arr) # in ra mang arr -> array('i', [1, 2, 3, 4, 5, 6, 10, 11, 12, 20, 21])

# 9. Fetch any element through its index.
print("Question 9") # in ra Question 9
print(arr.index(21)) # in ra vi tri cua phan tu 21 trong mang arr -> 10

# 10. Reverse a given array.
print("Question 10") # in ra Question 10
arr.reverse() # dao nguoc mang arr
print(arr) # in ra mang arr -> array('i', [21, 20, 12, 11, 10, 6, 5, 4, 3, 2, 1])

# 11. Get array buffer information.
print("Question 11") # in ra Question 11
print(arr.buffer_info()) # in ra thong tin buffer cua mang arr -> (140722016, 11)

# 12. Check for number of occurrences of an element.
print("Question 12") # in ra Question 12
print(arr.count(21)) # in ra so lan xuat hien cua phan tu 21 trong mang arr -> 1

# 13. Convert array to string.
print("Question 13") # in ra Question 13
strTemp = str(arr) # chuyen mang arr thanh chuoi strTemp
print(strTemp) # in ra strTemp -> array('i', [21, 20, 12, 11, 10, 6, 5, 4, 3, 2, 1])

# 14. Convert array to a python list with same elements using tolist() method.
print("Question 14") # in ra Question 14
print(arr.tolist()) # in ra mang arr -> [21, 20, 12, 11, 10, 6, 5, 4, 3, 2, 1]


# # 15. Append a string to char array using fromstring() method.
# print("Question 15") # in ra Question 15
# strTemp = "Python" # khoi tao chuoi strTemp
# arr.fromstring(strTemp) # them chuoi strTemp vao mang arr

# 16. Slice Elements from an array.
print("Question 16") # in ra Question 16
print(arr[2:5]) # in ra phan tu tu vi tri 2 den vi tri 5 cua mang arr -> array('i', [12, 11, 10])
"""

"------------------------------------------------------------------------"

"""
import numpy as np
twoDArray = np.array(
    [[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]]
)
print(twoDArray) # in ra mang twoDArray -> [[11 15 10  6] [10 14 11  5] [12 17 12  8] [15 18 14  9]]


newTwoArray = np.insert(twoDArray, 0, [1, 2, 3, 4], axis=1) # them mang [1, 2, 3, 4] vao vi tri 0 cua mang twoDArray
print(newTwoArray) # in ra mang newTwoArray -> [[ 1 11 15 10  6] [ 2 10 14 11  5] [ 3 12 17 12  8] [ 4 15 18 14  9]]


newTwoArray = np.insert(twoDArray, 0, [1, 2, 3, 4], axis=0) # them mang [1, 2, 3, 4] vao vi tri 0 cua mang twoDArray
print(newTwoArray) # in ra mang newTwoArray -> [[ 1  2  3  4] [11 15 10  6] [10 14 11  5] [12 17 12  8] [15 18 14  9]]


def accessElement(array, rowIndex, colIndex): # ham accessElement co tham so la array, rowIndex va colIndex
    if rowIndex >= len(array) and colIndex >= len(array[0]): # neu rowIndex >= do dai mang array va colIndex >= do dai mang array[0]
        print("Incorrect Index") # in ra Incorrect Index
    else:
        print(array[rowIndex][colIndex]) # in ra phan tu tai vi tri rowIndex va colIndex cua mang array


accessElement(twoDArray, 2, 3) # goi ham accessElement -> trả kết quả ra màn hình 8


def traverseTDArray(array): # ham traverseTDArray co tham so la array
    for i in range(len(array)): # duyet mang array
        for j in range(len(array[0])): # duyet mang array[0]
            print(array[i][j]) # in ra phan tu tai vi tri i va j cua mang array

traverseTDArray(twoDArray) # goi ham traverseTDArray -> trả kết quả ra màn hình 11 15 10 6 10 14 11 5 12 17 12 8 15 18 14 9


def searchTDArray(array, value): # ham searchTDArray co tham so la array va value
    for i in range(len(array)): # duyet mang array
        for j in range(len(array[0])): # duyet mang array[0]
            if array[i][j] == value: # neu phan tu tai vi tri i va j cua mang array = value
                return "The value is located at index " + str(i) + " " + str(j) # tra ve The value is located at index i j
    return "The element is not found" # tra ve The element is not found


print(searchTDArray(twoDArray, 55)) # goi ham searchTDArray -> trả kết quả ra màn hình The element is not found

newTDArray = np.delete(twoDArray, 1, axis=1) # xoa phan tu tai vi tri 1 cua mang twoDArray
print(newTDArray) # in ra mang newTDArray -> [[11 10  6] [10 11  5] [12 12  8] [15 14  9]]
"""
