with open('Day3/input.txt') as file:
    my_input = file.read()
    my_input = my_input.split('\n')
    my_input = [[*line] for line in my_input]

valid_nums = []
for i in range(len(my_input)):
    has_char = False
    current_num = ''
    for j in range(len(my_input[0])):
        if my_input[i][j] in '0123456789':
            current_num += my_input[i][j]
            for y in [-1,0,1]:
                for x in [-1,0,1]:
                    if i+y < 0 or i+y >=len(my_input) or j+x < 0 or j+x >= len(my_input[0]):
                        continue
                    if my_input[i+y][j+x] not in '1234567890.':
                        has_char = True
        else:
            if has_char:
                valid_nums.append(int(current_num))
            current_num = ''
            has_char = False
    if has_char:
            valid_nums.append(int(current_num))
print(sum(valid_nums))