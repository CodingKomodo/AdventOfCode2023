with open('Day4/input.txt') as file:
    in_text = file.readlines()
    in_text = [x.split(':')[1].strip() for x in in_text]
    win_num = [x.split('|')[0].split(' ') for x in in_text]
    my_num = [x.split('|')[-1].split(' ') for x in in_text]
    win_num = [(lambda y: [int(x) for x in y if x.isdigit()])(y) for y in win_num]
    my_num = [(lambda y: [int(x) for x in y if x.isdigit()])(y) for y in my_num]

total = 0
for i,win_list in enumerate(my_num):
    sub_total = 0
    for one_num in win_list:
        if one_num in win_num[i]:
            if sub_total == 0:
                sub_total += 1
            else:
                sub_total *= 2
    total += sub_total
print(total)