
# encoding: translating characters (letters, punctuation, symbols, whitespace and control characters) to integers and than to bits
'''                                                             ASCII table

Symbol/Character                 Dec       Byte        S/C   Dec      Byte       S/C   Dec      Byte        S/C          Dec      Byte
##############################################################################################################################################
NUL (Null) 	                      0 	 00000000       !    33 	00100001       A   65 	  01000001       a            97 	 01100001
SOH (Start of Heading) 	          1 	 00000001       "    34 	00100010       B   66 	  01000010       b            98     01100010
STX (Start of Text) 	          2 	 00000010       #    35 	00100011       C   67 	  01000011       c            99     01100011
ETX (End of Text) 	              3 	 00000011       $    36 	00100100       D   68 	  01000100       d            100    01100100
EOT (End of Transmission) 	      4 	 00000100       %    37 	00100101       E   69 	  01000101       e            101    01100101
ENQ (Enquiry) 	                  5 	 00000101       & 	 38 	00100110       F   70 	  01000110       f            102    01100110
ACK (Acknowledgment) 	          6 	 00000110       '    39 	00100111       G   71     01000111       g            103    01100111
BEL (Bell) 	                      7 	 00000111       (    40 	00101000       H   72     01001000       h            104    01101000
BS (Backspace) 	                  8 	 00001000       )    41 	00101001       I   73 	  01001001       i            105    01101001
HT (Horizontal Tab) 	          9 	 00001001       *    42 	00101010       J   74 	  01001010       j            106    01101010
LF (Line Feed) 	                  10 	 00001010       +    43 	00101011       K   75 	  01001011       k            107    01101011
VT (Vertical Tab) 	              11 	 00001011       ,    44 	00101100       L   76 	  01001100       l            108    01101100
FF (Form Feed) 	                  12 	 00001100       -    45 	00101101       M   77 	  01001101       m            109    01101101
CR (Carriage Return) 	          13 	 00001101       .    46 	00101110       N   78 	  01001110       n            110    01101110
SO (Shift Out) 	                  14 	 00001110       /    47 	00101111       O   79     01001111       o            111    01101111
SI (Shift In) 	                  15 	 00001111       0    48 	00110000       P   80 	  01010000       p            112    01110000
DLE (Data Link Escape) 	          16 	 00010000       1    49 	00110001       Q   81 	  01010001       q            113    01110001
DC1 (Device Control 1) 	          17 	 00010001       2    50 	00110010       R   82 	  01010010       r            114    01110010
DC2 (Device Control 2) 	          18 	 00010010       3    51 	00110011       S   83 	  01010011       s            115    01110011
DC3 (Device Control 3) 	          19 	 00010011       4    52 	00110100       T   84 	  01010100       t            116    01110100
DC4 (Device Control 4) 	          20 	 00010100       5    53 	00110101       U   85 	  01010101       u            117    01110101
NAK (Negative Acknowledgment) 	  21 	 00010101       6    54 	00110110       V   86 	  01010110       v            118    01110110
SYN (Synchronous Idle) 	          22 	 00010110       7    55 	00110111       W   87 	  01010111       w            119    01110111
ETB (End of Transmission Block)   23 	 00010111       8    56 	00111000       X   88 	  01011000       x            120    01111000
CAN (Cancel) 	                  24 	 00011000       9    57 	00111001       Y   89 	  01011001       y            121    01111001
EM (End of Medium) 	              25 	 00011001       :    58 	00111010       Z   90 	  01011010       z            122    01111010
SUB (Substitute) 	              26 	 00011010       ;    59 	00111011       [   91 	  01011011       {            123    01111011
ESC (Escape) 	                  27 	 00011011       <    60 	00111100       \   92 	  01011100       |            124    01111100
FS (File Separator) 	          28 	 00011100       =    61 	00111101       ]   93 	  01011101       }            125    01111101
GS (Group Separator) 	          29 	 00011101       >    62 	00111110       ^   94 	  01011110       ~            126    01111110
RS (Record Separator) 	          30 	 00011110       ?    63 	00111111       _   95 	  01011111       DEL (delete) 127    01111111
US (Unit Separator) 	          31 	 00011111       @    64 	01000000       `   96     01100000
SP (Space)                        32 	 00100000

Note:
128 chars (2^7) >>> last byte digit not used (always zero)
8 bits will let you express 2^8 == 256 possible values.
'''

ord('a') # ASCII domain
ord('€') # Unicode domain

chr(97)
chr(8364)

bin(97) # binary representation of an integer with the prefix "0b"
chr(0b01100001)

bytes([97])
bytes([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100, 33])

str(b'clich\xc3\xa9', 'utf-8')

'{0:b}'.format(ord('a'))
'{0:b}'.format(ord('€')) # more than one byte for non-ASCII


def make_bit_seq(s):
    if not str(s).isascii():
        raise ValueError("ASCII only allowed")
    return " ".join(f"{ord(i):08b}" for i in str(s))

make_bit_seq('a')
make_bit_seq('€')
make_bit_seq('Roberto')

int('11')
int('11', base=10)  # default
int('11', base=2)  # Binary
int('11', base=8)  # Octal
int('11', base=16)  # Hex

print(0x11)

### hex - bytes to string and string to bytes

# \x20 ' '    \x21 '!'    \x22 '"'    \x23 '#'
# \x24 '$'    \x25 '%'    \x26 '&'    \x27 '''
# \x28 '('    \x29 ')'    \x2a '*'    \x2b '+'
# \x2c ','    \x2d '-'    \x2e '.'    \x2f '/'
# \x30 '0'    \x31 '1'    \x32 '2'    \x33 '3'
# \x34 '4'    \x35 '5'    \x36 '6'    \x37 '7'
# \x38 '8'    \x39 '9'    \x3a ':'    \x3b ';'
# \x3c '<'    \x3d '='    \x3e '>'    \x3f '?'
# \x40 '@'    \x41 'A'    \x42 'B'    \x43 'C'
# \x44 'D'    \x45 'E'    \x46 'F'    \x47 'G'
# \x48 'H'    \x49 'I'    \x4a 'J'    \x4b 'K'
# \x4c 'L'    \x4d 'M'    \x4e 'N'    \x4f 'O'
# \x50 'P'    \x51 'Q'    \x52 'R'    \x53 'S'
# \x54 'T'    \x55 'U'    \x56 'V'    \x57 'W'
# \x58 'X'    \x59 'Y'    \x5a 'Z'    \x5b '['
# \x5c '\'    \x5d ']'    \x5e '^'    \x5f '_'
# \x60 '`'    \x61 'a'    \x62 'b'    \x63 'c'
# \x64 'd'    \x65 'e'    \x66 'f'    \x67 'g'
# \x68 'h'    \x69 'i'    \x6a 'j'    \x6b 'k'
# \x6c 'l'    \x6d 'm'    \x6e 'n'    \x6f 'o'
# \x70 'p'    \x71 'q'    \x72 'r'    \x73 's'
# \x74 't'    \x75 'u'    \x76 'v'    \x77 'w'
# \x78 'x'    \x79 'y'    \x7a 'z'    \x7b '{'
# \x7c '|'    \x7d '}'    \x7e '~'

# hexadecimal escape \xNN
# unicode escape \uNNNN
"a" == "\x61" == "\u0061"

##################################################################
################## string >> ENCODE >> bytes #####################
################## bytes >> DECODE >> string #####################
##################################################################

'Hello world!'.encode('utf-8')
b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21'.decode('utf-8')
b'Hello world!'.decode('utf-8')

'Niño'.encode('utf-8') # byte object: representations of bytes permit only ASCII characters
b'Niño'.decode('utf-8') # error
b'Ni\xc3\xb1o'.decode('utf-8')

list(b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21') # decimal value of each byte

# same string, different encoding
b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-16')
b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'.decode('utf-8')


characters = b'\x63\x6c\x69\x63\x68\xe9' # b defines a bytes string
str(characters)
print(characters)
print(characters.decode("latin-1"))

characters = "cliché"
print(characters.encode("UTF-8"))
print(characters.encode("latin-1"))
print(characters.encode("CP437"))
print(characters.encode("ascii"))

# Unicode string
b'\u48\u65\u6c\u6c\u6f\u20\u57\u6f\u72\u6c\u64\u21'.decode('unicode_escape') # error!
b'\u0048\u0065\u006c\u006c\u006f\u0020\u0057\u006f\u0072\u006c\u0064\u0021'.decode('unicode_escape')
