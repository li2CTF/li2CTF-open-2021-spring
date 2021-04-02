import wave

flag = b"flag{k1d_1_r34lly_h0p3_y0u_d1dn7_c0ll3c7_7h15_m0l73n_fl4g_by_y0ur53lf}"
bin_flag = [b for c in flag for b in bin(c)[2:].rjust(8, "0")]

# offset must be multiple of 8
offset = 0x2DF8

print("[*] Reading...")

w = wave.open('sher.wav', 'rb')

frames_n = w.getnframes()
channels_n = w.getnchannels()
framerate = w.getframerate()
sampwidth = w.getsampwidth()

frames = [c for c in w.readframes(frames_n)]

print(f"[#] Info: frames_n={frames_n} length={len(frames)} channels_n={channels_n} framerate={framerate} sampwidth={sampwidth}")

w.close()
print("[*] Read finished")

print("[*] Hiding flag...")
for i in range(offset, offset + len(bin_flag)):
	new = [b for b in bin(frames[i])[2:].rjust(8, "0")]
	new[-1] = bin_flag[i - offset]
	frames[i] = int("".join(new), 2)
print("[*] Flag hidden")

unbits = ""
for i in range(len(bin_flag) // 8):
	bits = ""
	for j in range(8):
		bits += bin(frames[offset + i * 8 + j])[2:][-1]
	unbits += chr(int(bits, 2))
	
print(f"[!] Flag: {unbits}")

for i in range(len(frames)):
	frames[i] = bytes([frames[i]])

print("[*] Writing...")
w = wave.open('molten-vinyl.wav', 'wb')
w.setnchannels(channels_n)
w.setsampwidth(sampwidth)
w.setframerate(framerate)
w.setnframes(frames_n)
w.writeframes(b''.join(frames))
w.close()
print("[*] Wrote")

print("[*] Testing...")
w = wave.open('molten-vynil.wav', 'rb')
frames = w.readframes(frames_n)

result = ""
bits = ""
for i in range(len(bin_flag) // 8):
	bits = ""
	for j in range(8):
		bits += bin(frames[offset + i * 8 + j])[2:][-1]
	result += chr(int(bits, 2))
print(f"[!] Decoded flag: {result}")
print("Successfully, flag is correct" if flag.decode("ascii") in result else "Flag is corrupted, go and debug me!")
