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
