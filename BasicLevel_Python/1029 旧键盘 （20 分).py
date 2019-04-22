import re
a = input()
b = input()
rst = []
for i in b:
    a = re.sub(i, '', a)
for i in a:
    if i.upper() not in rst:
        rst.append(i.upper())
print(''.join(rst))