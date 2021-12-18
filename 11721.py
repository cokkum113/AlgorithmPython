import sys

# s = input()
# for i in range(len(s)):
#     if len(s) >= 10:
#         print(s[i : 10])
#         s = s[10:]
# print(s)


s = input()
while(True):
    i = 0
    if len(s) >= 10:
        print(s[i : 10])
        s = s[10:]
    else:
        print(s)
        break

