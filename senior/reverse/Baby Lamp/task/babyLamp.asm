mov @d, R0
movb (R0), R3
add 2, R0
loop:
    movb (R0), R1
    xor 8, R1
    add 2, R1
    movb R1, (R0)
    add 1, R0
    sub 1, R3
    jnz loop
STOP
d:
    data 0A                ; dont forget to change me!!!
    data "<redacted>"
