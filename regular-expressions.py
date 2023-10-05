# before the regular expressions are used
# def isPhoneNumber(txt):
#     if len(txt) != 12:
#         return False
#
#     for i in range(0, 3):
#         if not txt[i].isdecimal():
#             return False
#     if txt[3] != '-':
#         return False
#
#     for i in range(4, 7):
#         if not txt[i].isdecimal():
#             return False
#
#     if txt[7] != '-':
#         return False
#
#     for i in range(8, 12):
#         if not txt[i].isdecimal():
#             return False
#
#     return True
#
#
# message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# for i in range(len(message)):
#     chunk = message[i: i+12]
#     if isPhoneNumber(chunk):
#         print('Phone number found: ' + chunk)
#
# print('Done')


# after use of regular expressions
# import re
#
# phoneNumber = re.compile(r'\d{3}-\d{3}-\d{4}')
# searchResult = phoneNumber.search('Call me at 415-555-1011 tomorrow.')
#
# print('Phone number found is: ' + searchResult.group() + '\n')


# using groups
# import re
#
# phoneNumber = re.compile(r'(\d{3})-(\d{3}-\d{4})')
#
# searchResult = phoneNumber.search('Call me at 415-555-1011 tomorrow.')
# print('Phone number found is: ' + searchResult.group())
# print('Phone number found is: ' + str(searchResult.groups()))
# one, two = searchResult.groups()
# print(one)

import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())
