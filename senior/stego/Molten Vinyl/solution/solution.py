import wave

w = wave.open('molten-vinyl.wav', 'rb')
frames = w.readframes(w.getnframes())

result = ""
for i in range(w.getnframes() * 4 // 8):
	bits = ""
	for j in range(8):
		bits += bin(frames[i * 8 + j])[2:][-1]
	result += chr(int(bits, 2))

print(f'Found something: {result[result.index("flag{"):result.index("flag{") + 200]}')
with open("file.txt", "w") as f:
	f.write(result)