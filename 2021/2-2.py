f = open('./2021/inputs/2.txt')
content = f.read()
inputs = content.splitlines()

choices = ['forward', 'down', 'up']
x = 0
y = 0
aim = 0

for input in inputs:
    if input.startswith('forward'):
        x += int(input.split('forward ')[1])
        y += aim * int(input.split('forward ')[1])
    elif input.startswith('down'):
        aim += int(input.split('down ')[1])
    elif input.startswith('up'):
        aim -= int(input.split('up ')[1])

print(x, y)
print(x * y)
