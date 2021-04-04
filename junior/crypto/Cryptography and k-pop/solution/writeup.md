# Cryptography and k-pop writeup
The first thing we can understand is that the contents of the file were encoded via base64 because of two '='s in the end of the file. After decoding the contents, we get some binary trash. Let's open this in any hxd editor so we can see the bytes. The first bytes of this file are `FF D8 FF E0`. These are the magic bytes of .jpeg files, so now we can save this binary trash as a .jpeg file. Opening it, we'll see a picture and a string which starts with 'CTF...', but there are some korean symbols, so all that remains to be done is to romanize this string. After that we'll have this flag.

Flag: **CTF{shokersss's_most_favourite_korean_song_is_o_solle_mio_by_iz\*one}**
