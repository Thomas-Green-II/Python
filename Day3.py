# STEGANOGRAPHY/BINARY

-msg = 'a'
-ord(msg)     <------ # ord is how you get the decimal value of a value
97
-bin(ord(msg))   <-------- # bin is how you get the binary value of a value
0b1100001
-format(ord(msg), '0>8b')     <----------- # formats the value to an 8 bit long value
01100001
-int('1100001', 2)    <-------- # Converts the binary into decimal(base2)
97
-chr(int('1100001', 2))   <---------- # Converts the integer to ASCII
a


BIG SCRIPT for STEGO
        |
        |
        |
        V
#!/usr/bin/env python3

def steg_encode_char(char, cover):
    '''LSB encodes a character
    Args:
        char (str): a single character string
        cover (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        None
    '''
    binary1 = format(ord(char), '0>8b')


        for i in range(0,8):
            coverbinl = list(binary1)
            coverbinl[-1] = binary1[i]
            cover[i] = int(''.join(coverbinl), base=2)
            


def steg_decode_char(stego):
    '''LSB decodes a character
    Args:
        stego (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        str: character that was decoded
    '''
    msgbits = []
    
    for item in cover
        msgbits.append(bin(item)[-1])

    chr(int(''.join(msgbits),base=2))
    return msgbits
