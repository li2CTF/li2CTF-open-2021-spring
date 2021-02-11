from random import randint

flag = [c for c in "flag{n0_m0r3_c0un71ng_m4rk5_w1ll_b3_c0un71ng_fl4g5}"]
with open("orig.txt", "r") as f:
	words = f.read().split(" ")
	
	for i in range(len(words)):
		words[i] = [c for c in words[i]]

	cntr = 0
	flag_cntr = 0
	ch = False

	while cntr < len(words) and flag_cntr < len(flag):
		print(cntr)
		ch = False
		
		for j in range(len(words[cntr])):
			if words[cntr][j] != flag[flag_cntr]:
				words[cntr][j] = flag[flag_cntr]	
				ch = True
				flag_cntr += 1
				break

		if not ch:
			cntr += 1
		else:
			cntr += len(words) // len(flag)

	for i in range(len(words)):
		words[i] = "".join(words[i])	

with open("task.txt", "w") as f:
	f.write(" ".join(words))
