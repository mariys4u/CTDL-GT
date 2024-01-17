# def foo(array):
#     sum = 0
#     product = 1
#     for i in array:
#         sum += i
#     for i in array:
#         product *= i
#     print("Sum = " + str(sum) + ", Product = " + str(product))


# foo([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# def printPairs(array):
#     for i in array:
#         for j in array:
#             print(str(i) + "," + str(j))


# printPairs([1, 2, 3, 4, 5])


# def printUnorderedPairs(array):
#     for i in range(0, len(array)):
#         for j in range(i + 1, len(array)):
#             print(str(array[i]) + "," + str(array[j]))


# printUnorderedPairs([1, 2, 3, 4, 5])


# def printUnorderedPairs(arrayA, arrayB):
#     for i in range(0, len(arrayA)):
#         for j in range(0, len(arrayB)):
#             if arrayA[i] < arrayB[j]:
#                 print(str(arrayA[i]) + "," + str(arrayB[j]))


# printUnorderedPairs([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])


# def printUnorderedPairs(arrayA, arrayB):
#     for i in range(len(arrayA)):
#         for j in range(len(arrayB)):
#             for k in range(0, 100000):
#                 print(str(arrayA[i]) + "," + str(arrayB[j]))


# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# printUnorderedPairs(a, b)


# def reverse(array):
#     for i in range(0, int(len(array) / 2)):
#         other = len(array) - i - 1

#         temp = array[i]

#         array[i] = array[other]

#         array[other] = temp

#     print(array)


# reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# def factorial(n):
#     if n < 0:
#         return -1
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(5))


# def allFib(n):
#     for i in range(n):
#         print(str(i) + ":" + str(fib(i)))


# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)


# def powerOf2(n):
#     if n < 1:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         prev = powerOf2(int(n / 2))
#         curr = prev * 2
#         print(curr)
#         return curr


# powerOf2(50)


# Find Number of Days Above Average Temperature


# def averageTemperature(temperatures):
#     sum = 0
#     for temperature in temperatures:
#         sum += temperature
#     return sum / len(temperatures)

# print(averageTemperature([1,2]))


# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[j] == target - nums[i]:
#                 return [i, j]


# print(twoSum([3, 2, 4], 6))


# rotate Matrix 90 degree by an NxN matrix


def rotateMatrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    n = len(matrix)
    for layer in range(int(n / 2)):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            top = matrix[first][i]

            matrix[first][i] = matrix[last - offset][first]

            matrix[last - offset][first] = matrix[last][last - offset]

            matrix[last][last - offset] = matrix[i][last]

            matrix[i][last] = top
    return matrix


print(rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
