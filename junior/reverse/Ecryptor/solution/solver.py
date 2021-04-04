f = open("output.txt", "r")
numbers = f.read().split(" ")
shift = 2
flag = ""

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    numbers[i] = numbers[i] // shift
    shift += 1

for i in range(len(numbers)):
    numbers[i] = numbers[i] ^ 0x73

for i in range(len(numbers)):
    flag += chr(numbers[i])

print(flag)
