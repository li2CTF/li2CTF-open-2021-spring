# Tempus machina writeup
We see archive with some text file inside. After some researches, we find `.git`. After checking logs:

```bash
git log --graph
```

We see some commits named as centuries. 
- **Century I:** we see text file with part of flag (`flag{7h4nk_y0u_`). Nothing to see here anymore.
- **Century II:** image. `strings` it and get 2nd part of flag (`f0r_n07_`)
- **Century III:** encrypted part of flag. That's easy to understand it's Caesar cipher. We got 3rd part of flag (`c4u51ng_4ny_`)
- **Century VI:** 7z-archive with password. After researches, we find the password in the end of file - _password=07cc694b9b3fc636710fa08b6922c42b_. After googling this sequence we understand it's md5 hash and we can find that it's `md5("time")`. Enter password, inside archive we see .gif file with the last part of flag (`73mp0r4l_p4r4d0x}`).

Flag: **flag{7h4nk_y0u_f0r_n07_c4u51ng_4ny_73mp0r4l_p4r4d0x}**
