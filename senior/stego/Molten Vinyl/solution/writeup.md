# Molten Vinyl writeup
In conditions we see hint (_every 8th bit_). Using `wave` (we also have this hint in conditions) python library we can get all frames. We just take each 8th bit of all bytes and concat them to make 1 byte (char). Then we concat all chars and get a big output, where we can CTRL+F flag.

Flag: **flag{k1d_1_r34lly_h0p3_y0u_d1dn7_c0ll3c7_7h15_m0l73n_fl4g_by_y0ur53lf}**
