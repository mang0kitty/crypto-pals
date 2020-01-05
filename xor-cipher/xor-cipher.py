from binascii import unhexlify

input = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

data = unhexlify(input)

for key in range(0, 255):
    decoded = str(bytes([(b ^ key) for b in data]))
    if all([c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. '\"!?" for c in decoded]):
        print("Key: ", key, " :: ", decoded)
