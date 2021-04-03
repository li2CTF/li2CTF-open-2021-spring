# Encryptor writeup
We see an algo which encrypts text and encypted message (`output.txt`). `flag` variable is redacted, so we must recover it. 

Firstly, let's see how flag is encoded:

1) We get ascii-number of flag's chars (it's reversible operation):
```python
for letter in flag:
	letters.append(ord(letter))
```
2) XOR (Exclusive OR logical operation) with 0x73 (it's also reversible operation):
```python
for i in range(len(letters)):
	letters[i] = letters[i] ^ 0x73
```
3) Multiplication with `shift` number and converting to string (also reversible operation):
```python
for i in range(len(letters)):
	letters[i] = str(letters[i] * shift)
	shift += 1
```

So, our goal is to rewrite this algo back to front using opposite operations:

1) Convert back to integers (`int()` is opposite of `str()`): 
```python
for i in range(len(numbers)):
	numbers[i] = int(numbers[i])
```
2) Divide numbers (`division` is opposite of `multiplication`) them by `shift`:
```python
shift = 2
for i in range(len(numbers)):
	numbers[i] = numbers[i] // shift
	shift += 1
```
3) XOR with 0x73 (`XOR` is opposite of itself):
```python
for i in range(len(numbers)):
	numbers[i] = numbers[i] ^ 0x73
```
4) Concat all chars and print flag:
```python
for i in range(len(numbers)):
	flag += chr(numbers[i])
print(flag)
```

Flag: **flag{w0w_n0w_y0u_kn0w_wh47_15_x0r}**
