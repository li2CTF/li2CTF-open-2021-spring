# Black&AlmostBlack writeup
After reading conditions and name of the task, run `StegSolve`. Using some filters in this utility, we may see that it's actually a QR code. Scan it, then we see next message:

_XOR original with 0xBB or go home_ 

So, we do what we're asked for. Then we look into the binary we got after XORing image with 0xBB and see the flag in the end of file

Example of solution is in `sovler.py`

Flag: **flag{4c7u4lly_Bl4ck_4nd_Wh173_l0l}**
