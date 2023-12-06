with open('Day3/input.txt') as file:
    my_input = file.read()
    my_input = my_input.split('\n')
    my_input = [[*line] for line in my_input]

gears = {}

for i in range(len(my_input)):
    current_gear = None
    has_char = False
    current_num = ''
    for j in range(len(my_input[0])):
        if my_input[i][j] in '0123456789':
            current_num += my_input[i][j]
            for y in [-1,0,1]:
                for x in [-1,0,1]:
                    if i+y < 0 or i+y >=len(my_input) or j+x < 0 or j+x >= len(my_input[0]):
                        continue
                    if my_input[i+y][j+x] == '*':
                        current_gear = (i+y, j+x)
        else:
            if current_gear:
                if current_gear in gears:
                    gears[current_gear].append(int(current_num))
                else:
                    gears[current_gear] = [int(current_num)]
                
            current_num = ''
            has_char = False
            current_gear = None
    if current_gear:
        if current_gear in gears:
            gears[current_gear].append(int(current_num))
        else:
            gears[current_gear] = [int(current_num)]
total = 0
for item in gears.values():
    if len(item) == 2:
        total += item[0] * item[1]
print(total)