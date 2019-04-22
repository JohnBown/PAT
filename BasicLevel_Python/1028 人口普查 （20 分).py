num = int(input())

d = {}
count = 0
max, min = "1814/09/06", "2014/09/06"
max_name, min_name = '', ''

for i in range(num):
    name, date = input().split()
    if date >= '1814/09/06' and date <= '2014/09/06':
        d[name] = date
        count += 1

for key, value in d.items():
    if value > max:
        max = value
        max_name = key
    if value < min:
        min = value
        min_name = key

if count == 0:
    print("0")
else:
    print(str(count) + ' ' + min_name + " " + max_name)