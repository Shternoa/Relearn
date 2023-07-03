# --- Year -- #

# year = int(input('Введите год: '))
#
# if year % 4 == 0:
#     print(f'{year} True')
# elif year % 100 == 0:
#     print(f'{year} False')
# elif year % 400 == 0:
#     print(f'{year} True')
# else:
#     print(f'{year} False')

# --- Year -- #

# --- Список купюр которыми можно заплатить N сумму -- #

# def banknotes(n):
#     bank = [64, 32, 16, 8, 4, 2, 1]
#     res = []
#     for b in bank:
#         count = n // b
#         res += [b] * count
#         n -= count * b
#     return res
#
#
# print(banknotes(12))

# --- Список купюр которыми можно заплатить N сумму -- #


# --- Анаграмма --- #

# def is_anagram(a, b):
#     return True if sorted(a) == sorted(b) else False
#
#
# print(is_anagram('rat', 'cat'))
# print(is_anagram('night', 'thing'))

# --- Анаграмма --- #

# --- Перевернутые согласные ---#

# def reverse_vowels(s):
#     vowels = set('aeiouyAEIOUY')
#     s = list(s)
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] in vowels and s[right] in vowels:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -=1
#         elif s[left] in vowels:
#             right -= 1
#         elif s[right] in vowels:
#             left += 1
#         else:
#             left += 1
#             right -= 1
#     return ''.join(s)
#
# print(reverse_vowels('I am beautiful man'))

# --- Перевернутые согласные ---#

# --- Длинна подстроки --- #

# def longest_substring(s):
#     n = len(s)
#     substring = set()
#     max_substring = None
#     max_count = 0
#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             substr = s[i:j]
#             if substr in substring:
#                 count = s.count(substr)
#                 if count > max_count:
#                     max_substring = substr
#                     max_count = count
#                 elif count == max_count and len(substr) > len(max_substring):
#                     max_substring = substr
#             else:
#                 substring.add(substr)
#     return max_substring, max_count
#
#
# print(longest_substring('abcabcabcabcabc'))

# --- Длинна подстроки --- #

# --- Четная минута --- #

# from datetime import datetime
#
# odd = list(range(1, 61, 2))
# even = list(range(2, 61, 2))
#
#
# this_minute = datetime.today().minute
#
# if this_minute in odd:
#     print(f'{this_minute} is odd')
# else:
#     print(f'{this_minute} is even')

# --- Четная минута --- #

# --- Finding ---#

# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return i, j
#     return None
#
#
# sum = twoSum([2, 7, 11, 15], 26)
# print(sum)

# --- Finding ---#

# --- Candy ---#
# def kidsWithCandies(candies, extracandies):
#     result = []
#     max_candies = max(candies)
#     for i in candies:
#         if i >= extracandies:
#             result.append(True)
#         else:
#             result.append(False)
#     return result
#
#
# kids = kidsWithCandies([2, 3, 5, 1, 3], 3)
# print(kids)

# --- Candy ---#

# --- Sort_Index --- #
# def searchInsert(num, target):
#     if target not in num:
#         num.append(target)
#         return sorted(num).index(target)
#     else:
#         return num.index(target)
#
#
# sort = searchInsert([1, 3, 5, 6], 8)
# print(sort)

# --- Sort_Index --- #

# --- Parentheses --- #

# def is_valid(seek):
#     stack = []
#     mapping = {')': '(', '}': '{', ']': '['}
#     for bracket in seek:
#         if bracket in mapping:
#             if not stack or stack[-1] != mapping[bracket]:
#                 return False
#             stack.pop()
#         else:
#             stack.append(bracket)
#     return not stack
#
#
# print(is_valid("()[]{}"))
# print(is_valid("(]"))

# --- Parentheses --- #

# --- Remove And Count --- #

# def remove_elem(nums, val):
#     result = []
#     count = 0
#     for num in nums:
#         if num != val:
#             result.append(num)
#         else:
#             count += 1
#     return result, count
#
#
# print(remove_elem([3, 2, 2, 3], 3))
# print(remove_elem([3, 2, 5, 5, 2, 3, 5, 1, 6], 5))

# --- Remove And Count --- #
