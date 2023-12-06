with open('Day1/input.txt', mode= 'r+') as file:
    inputs = file.readlines()
numbers = []

for i in range(len(inputs)):
    build_num = ''
    line = inputs[i]
    for j in range(len(line)):
        if line[j] in '1234567890':
            build_num += line[j]
            break
    for j in range(len(line) - 1,-1,-1):
        if line[j] in '1234567890':
            build_num += line[j]
            break
    if len(build_num) == 0:
        numbers.append(0)
    numbers.append(int(build_num))
print(sum(numbers))
        
    