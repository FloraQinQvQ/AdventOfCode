f = open('./2021/inputs/2.txt')
content = f.read()
inputs = content.splitlines()

choices = ['forward', 'down', 'up']
x = 0
y = 0

for input in inputs:
    if input.startswith('forward'):
        x += int(input.split('forward ')[1])
    elif input.startswith('down'):
        y += int(input.split('down ')[1])
    elif input.startswith('up'):
        y -= int(input.split('up ')[1])

print(x, y)
print(x * y)
