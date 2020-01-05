import string
from binascii import unhexlify, b2a_base64


def hex_to_byteArray(hexString):
    return unhexlify(hexString)


def xor(buffer1: bytes, buffer2: bytes) -> bytes:
    return bytes([(b1 ^ b2) for b1, b2 in zip(buffer1, buffer2)])


def byte_to_string(byte_list: bytes) -> str:
    return "".join(filter(lambda x: x in string.printable, "".join(map(chr, byte_list))))


HEX_STRING = "1c0111001f010100061a024b53535009181c"
XOR_STRING = "686974207468652062756c6c277320657965"
print(byte_to_string(xor(hex_to_byteArray(HEX_STRING), hex_to_byteArray(XOR_STRING))))
