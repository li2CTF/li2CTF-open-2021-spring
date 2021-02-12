flag = "flag{5h1f71ng_15_4l50_kn0wn_45_c4354r_c1ph3r}"
data = []
for i in range(len(flag)):
	data.append(str(ord(flag[i]) - 6))
print("{" + ", ".join(data) + "}")
