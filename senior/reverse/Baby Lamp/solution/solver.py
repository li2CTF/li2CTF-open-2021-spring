data = "pfkquf>gz?Y>|=Y?:Ym::fw"

for i in range(len(data)):
	print(chr((ord(data[i]) - 2) ^ 8), end="")
