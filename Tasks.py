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

# --- Century Year --- #

# def century(year):
#     if year <= 0:
#         return False
#     if year % 100 == 0:
#         century = year // 100
#     else:
#         century = year // 100 + 1
#
#     return century
#
#
# print(century(2023))

# --- Century Year --- #

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

# --- Steps variants --- #

# def climbStairs(n):
#     dp = [0] * (n + 1)
#     dp[0] = 1
#     dp[1] = 1
#
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[n]
#
#
# print(climbStairs(5))

# --- Steps variants --- #

# --- Pair index ---#

# def containsNearbyDuplicate(nums, k):
#     for i in range(0, len(nums) - 1):
#         for j in range(i + 1, min(i + k + 1, len(nums))):
#             if nums[i] == nums[j]:
#                 return True
#     return False
#
#
# print(containsNearbyDuplicate([1, 2, 3, 1], 3))

# --- Pair index ---#


# --- Sum digits --- #

# def addDigits(num):
#     num_str = str(num)
#     sum_digits = 0
#     for digit in num_str:
#         sum_digits += int(digit)
#     return sum_digits
#
#
# print(addDigits(555))

# --- Sum digits --- #

# --- Convert number to reversed array of digits --- #

# def digitize(n):
#     return [int(char) for char in str(n)[::-1]]
#
#
# print(digitize(23582357))

# --- Convert number to reversed array of digits --- #

# --- Clock --- #

# def past(h, m, s):
#     return (h * 3600000) + (m * 60000) + (s * 1000)
#
#
# print(past(0, 1, 1))

# --- Clock --- #

# --- Sum without highest and lowest number --- #

# def sum_array(arr):
#     if len(arr) <= 1:
#         return 0
#     arr.sort()
#     return sum(arr[1:-1])
#
#
# print(sum_array([-6, -20, -1, -10, -12]))

# --- Sum without highest and lowest number --- #

# --- Total amount of points --- #

# def points(games):
#     total_points = 0
#     for game in games:
#         goals = game.split(':')
#         if goals[0] > goals[1]:
#             total_points += 3
#         elif goals[0] < goals[1]:
#             total_points += 0
#         elif goals[0] == goals[1]:
#             total_points += 1
#     return total_points
#
#
# print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']))

# --- Total amount of points --- #

# --- Count of positives / sum of negatives --- #

# def count_positives_sum_negatives(arr):
#     if not arr:
#         return []
#     positive = []
#     negative = []
#     count = 0
#     for i in arr:
#         if i < 0:
#             negative.append(i)
#         elif i > 0:
#             positive.append(i)
#             count +=1
#     return [count, sum(negative)]
#
#
# print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))

# --- Count of positives / sum of negatives --- #

# --- Swap case --- #

# def swap_case(s):
#     result = ""
#     for i in s:
#         if i.islower():
#             result += i.upper()
#         elif i.isupper():
#             result += i.lower()
#         else:
#             result += i
#     return result
#
#
# print(swap_case('Www.HackerRank.com'))

# --- Swap case --- #

# --- String Split and Join --- #

# def split_and_join(line):
#     words = line.split(' ')
#     return '-'.join(words)
#
# print(split_and_join('this is a string'))

# --- String Split and Join --- #

# --- What's Your Name? --- #

# def print_full_name(first, last):
#     full_name = f"{first} {last}"
#     message = f"Hello {full_name}! You just delved into python."
#     print(message)
#
#
# print_full_name('Ross', 'Taylor')

# --- What's Your Name? --- #

# --- Mutations --- #

# def mutate_string(string, position, character):
#     new_string = list(string)
#     new_string[position] = character
#     mut_string = ''.join(new_string)
#     return mut_string
#
#
# print(mutate_string('abracadabra', 5, 'k'))

# --- Mutations --- #
