with open("orig.txt", "r") as f, open("task.txt") as g:
	orig = f.read()
	task = g.read()
	for i in range(min(len(task), len(orig))):
		if task[i] != orig[i]:
			print(task[i], end="")
