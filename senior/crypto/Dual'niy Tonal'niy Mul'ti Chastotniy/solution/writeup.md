# Dual'niy Tonal'niy Mul'ti Chastotniy writeup
Firstly, let's open this file in any audio editor as a spectrogram. We can see how the frequencies of the sounds are repeated.
After that, let's look at the name of the task and translate it: Dual-tone multi-frequency, which is an abbreviation of DTMF. Let's google this and find a picture with the same sound frequencies as in our file. Thus, we only need to decrypt the file itself (this can be done by hand or with the help of online decoders). After decryption, we'll get the string: `67 84 70 123 77 67 95 67 104 112 48 110 107 51 114 53 53 53 95 118 53 95 77 67 95 68 114 49 108 108`. Finally, let's decode each number as an ascii character and get: `CTF{MC_Chp0nk3r555_v5_MC_Dr1ll`. It remains only to put the `}` at the end and the flag is ready.

Flag: **CTF{MC_Chp0nk3r555_v5_MC_Dr1ll}**
