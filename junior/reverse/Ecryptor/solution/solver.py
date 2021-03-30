f = open("output.txt", "r")
numbers = f.read().split(" ")
cntr = 2
flag = ""

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    numbers[i] = numbers[i] // cntr
    numbers[i] = numbers[i] ^ 0x73
    flag += chr(numbers[i])
    cntr += 1

print(flag)