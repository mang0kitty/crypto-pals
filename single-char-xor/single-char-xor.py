from binascii import unhexlify
import string


def score(sentence: str):
    score = 0

    for c in sentence:
        if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ":
            score += 1
        if c in "<>[](){}":
            score -= 1
        if ord(c) > 128:
            score -= 100

    return score / len(sentence)


def check_chunk(chunk: bytes):
    # for key in range(0, 256):
    #     decoded = (bytes([(key ^ b)for b in chunk]).decode('ascii'))
    #     print("Key: ", key, " :: ", decoded)
    #print("input: ", chunk.decode("latin-1"))
    try:
        for key in range(0, 256):
            decoded = bytes([(key ^ b)for b in chunk]).decode('latin-1')
            if score(decoded) > 0.9:
                print("Key: ", key, " :: ", decoded)
    except UnicodeDecodeError:
        pass


def read_lines():
    with open('4.txt', 'r') as f:
        while True:
            chunk = f.readline().strip()
            if not chunk:
                print("End of file")
                break
            check_chunk(unhexlify(chunk.strip()))


read_lines()
