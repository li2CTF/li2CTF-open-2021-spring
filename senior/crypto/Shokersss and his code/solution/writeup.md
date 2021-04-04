# Shokersss and his code
Firstly, let's view all files. One of them is a python code, and the other one contains binary data. Secondly, let's read the conditions more carefully and try to get key words: private-key cryptography algorithms. After some time spent surfing the internet, we'll find *Diffie-Hellman key exchange* and this is what we need. So now we can get a, b variables and, eventually, the file-key - _yusuf_.
Now when we are about to uncipher trash file, we have to figure out the cipher used there. After another time spent on googling, we'll conclude that this is a XOR-cipher. Here is a code that converts trash file to a normal one:

```python 
from math import ceil
key = 'yusuf'
f1 = open('li2_crypto_4enc.txt', 'r').read()
f2 = open('output.txt', 'w')
f2.write(''.join(chr(ord(a) ^ ord(b)) for a, b in zip(key * ceil(len(f1) / len(key)), f1))) 
```

We will get a file with another public key encryption method - RSA. By writing code that defines the prime divisors of N, we can get p and q => we can get the number (the m variable) that was encrypted. Now all we have to do is execute the last line and get the flag.

Flag: **CTF{5h0k3r555_h4735_x0r_bu7_l0v35_dh_4nd_r54}**
