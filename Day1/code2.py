with open('Day1/input.txt', mode= 'r+') as file:
    inputs = file.readlines()
possible_num = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
numbers = []

for i in range(len(inputs)):
    build_num = ''
    line = inputs[i]
    for j in range(len(line)):
        leave = False
        if line[j] in '1234567890':
            build_num += line[j]
            break
        for val in range(3,6):
            try:
                build_num += possible_num[line[j:j+val]]
                leave = True
            except:
                pass
        if leave:
            break
    for j in range(len(line) - 1,-1,-1):
        leave = False
        if line[j] in '1234567890':
            build_num += line[j]
            break
        for val in range(-3,-6,-1):
            try:
                build_num += possible_num[line[j + val+1:j+ 1]]
                leave = True
            except:
                pass
        if leave:
            break
    if len(build_num) == 0:
        numbers.append(0)
    numbers.append(int(build_num))
print(sum(numbers))

        