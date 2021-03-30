flag = "<redacted>"
letters = []
shift = 2

for letter in flag:
    letters.append(ord(letter))

for i in range(len(letters)):
    letters[i] = letters[i] ^ 0x73

for i in range(len(letters)):
    letters[i] = str(letters[i] * shift)
    shift += 1

f = open("output.txt", "w")
f.write(" ".join(letters))
f.close()
