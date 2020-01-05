from binascii import unhexlify, b2a_base64


def hex_to_base64(hex_string):
    return b2a_base64(unhexlify(hex_string))


HEX_STRING = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print("hello")
print(hex_to_base64(HEX_STRING))
