with open("black&almostblack.png", "rb") as f:
	data = [chr(int(i) ^ 0xBB) for i in f.read()]
	print("".join(data))
