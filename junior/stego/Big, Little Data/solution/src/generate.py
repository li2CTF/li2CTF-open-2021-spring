from random import randint, choice

flag = "flag{hmmm_c7rl+F_0r_gr3p?}"

alph = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [str(i) for i in range(10)] + ["_", "{", "}", "?", "+", "-"]

with open("data.dat", "w") as f:
	offset1 = randint(600000, 1500000)
	offset2 = randint(600000, 1500000)
	data = []
	for _ in range(offset1):
		data.append(alph[randint(0, len(alph) - 1)])
	data.append(flag)
	for _ in range(offset2):
		data.append(alph[randint(0, len(alph) - 1)])
	f.write("".join(data))