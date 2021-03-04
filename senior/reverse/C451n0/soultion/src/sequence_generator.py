with open("message.txt", "r") as f:
	data = [i for i in f.read()]
	let = "X"
	for i in range(len(data)):
		data[i] = ord(data[i]) - ord(let)
	print(data)
	print(len(data))