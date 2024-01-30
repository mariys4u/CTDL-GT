# 1/ Reversing an array in-place exercise
def reverse_list(lst):
    lst.reverse()
    return lst


# Kiểm tra hàm
print(reverse_list([1, 2, 3, 4, 5]))

"---------------------------------------------------------------"


# 2/ Palindrome exercise
def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


# Kiểm tra hàm
print(is_palindrome("racecar"))

"---------------------------------------------------------------"


# 3/ Integer reversion exercise
def reverse_integer(n):
    return int(str(n)[::-1])


# Kiểm tra hàm
print(reverse_integer(12345))

"---------------------------------------------------------------"


# 4/ Anagram problem exercise
def anagram(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False


# Kiểm tra hàm
print(anagram("abcd3", "3acdb"))
