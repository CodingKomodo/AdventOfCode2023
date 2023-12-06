with open('Day4/input.txt') as file:
    in_text = file.readlines()
    in_text = [x.split(':')[1].strip() for x in in_text]
    win_num = [x.split('|')[0].split(' ') for x in in_text]
    my_num = [x.split('|')[-1].split(' ') for x in in_text]
    win_num = [(lambda y: [int(x) for x in y if x.isdigit()])(y) for y in win_num]
    my_num = [(lambda y: [int(x) for x in y if x.isdigit()])(y) for y in my_num]

total_cards = [1 for i in range(len(win_num))]
for i,my_list in enumerate(my_num):
    num_match = 0
    for one_num in my_list:
        if one_num in win_num[i]:
            num_match += 1
    for num in range(i+1, min(i+num_match+1,len(total_cards))):
        total_cards[num] += 1 * total_cards[i]
print(sum(total_cards))