g = 3793
n = 8501
A = 1661
B = 6099
K = 5508
a = int(input())
b = int(input())
assert a < 1000 and b < 1000
file_key = (bytes.fromhex(str(a) + str(b) + str((a + b) * 5 + 716))).decode("ASCII")
