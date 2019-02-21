date_list = []

date = '2019-01-%s%s'
units = 1
tens = 0
for i in range(31):
    date_list.append(date % (tens, units))
    if units == 9:
        units = 0
        tens += 1
    else:
        units += 1

print date_list
