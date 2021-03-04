# Shifter writeup
Program expects flag and then it checks if it's correct or not. Let's read deeper.
`main()` waits for line, then it calls `check_flag()`. This function compares input and `check` array char by char, adding 6 to the check:

![](/junior/reverse/Shifter/solution/static/code.png)

So, to get the flag we just need to add 6 to each char in `check` array. Example of solution is in `solve.py`

Flag: **flag{5h1f71ng_15_4l50_kn0wn_45_c4354r_c1ph3r}**
