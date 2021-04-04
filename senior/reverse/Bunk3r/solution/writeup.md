# Bunk3r writeup
After decompiling binary we see that app waits for PIN (hexadecimal number) and password (string, length=10). `check_pin()` function simply compares 4 bytes of PIN with some numbers. So, PIN=`11DECADE`.

`check_password()` function contains checks of password letters. We can start from `password[0]` - it's `(pin >> 24) + 0x35` (and we already know PIN). Then, we are able to count other letters (example order: 0 -> 6 -> 3 -> 9 -> 5 -> 2 -> 8 -> 4 -> 1 -> 7). In the end, we have password=`F4SL3NZ0QN`

Enter PIN and password, and get the flag.

Flag: **flag{Y0u_5ucc355fully_d151n73gr473d_Gr3g0r1'5_bunk3r}**
