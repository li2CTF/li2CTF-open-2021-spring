# Bacon writeup
We may notice that text in file looks like some `base`, especially `base64`. But, after closer look we may notice that unlike to `base64`, there are no '0', 'O', 'I', 'l', '+' и '/' => it's `base58`. We could also understood it from codnitions - because `base58` is being used in bitcoin.

After decoding we get sequence of 'A' and 'B'. It's Bacon's cipher (name of task is Bacon). After decoding we get "YOURFLAGISFRANCISBACONSBITCOINFARM".

Flags: **flag{YOURFLAGISFRANCISBACONSBITCOINFARM}**, **flag{FRANCISBACONSBITCOINFARM}**
