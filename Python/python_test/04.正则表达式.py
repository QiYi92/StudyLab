import re

pattern = r'times'
string = "It was the best of times, it was the worst of times."
print(len(re.findall(pattern, string)))

# pattern = r'[a-zA-Z]'
# string = "It was the best of times, it was the worst of times."
# print(len(re.findall(pattern, string))) #查找从a-z,A-Z的所有字母

# pattern = r'[iI]t'
# string = "It was the best of times, it was the worst of times."
# matches = re.findall(pattern, string)
#
# for match in matches:
#     print(match)

# pattern = r'[iI]t'
# string = "It was the best of times, it was the worst of times."
# location = re.search(pattern, string)
# print(location)
# print(location.group())

# string = "It was the best of times, it was the worst of times."
# string = re.sub(r'times', r'life', string)
# print(string)

# match = re.search(r'[A-Z]{5}[0–9]{4}[A-Z]', 'ABcDE1234L')
# # 前5个是char类型,后边4个是digit类型,最后一个是char类型
# if match:
#     print(True)
# else:
#     print(False)
