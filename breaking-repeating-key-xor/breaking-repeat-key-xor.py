from binascii import a2b_base64
import string


def bytes_to_string(byte_list: bytes) -> str:
    return "".join(filter(lambda x: x in string.printable, "".join(map(chr, byte_list))))


def xor(b_s1, b_s2):
    return bytes([(a ^ b) for a, b in zip(b_s1, b_s2)])


def hamming_distance(string1: bytes, string2: bytes) -> int:
    xor_output = xor(string1, string2)
    return sum(bin(byte).count("1") for byte in xor_output)


def main():
    byte_string = b''.join([a2b_base64(line.strip())
                            for line in open('6.txt', 'r').readlines()])
    i = 0
    keysize_distances = []
    for keysize in range(2, 40):
        # break ciphertext into chunks the length of the keysize
        blocks = [byte_string[i:i+keysize]
                  for i in range(0, len(byte_string), keysize)]
        distances = [hamming_distance(blocks[i], blocks[j])for i in range(
            len(blocks)-1) for j in range(1, len(blocks))]
        distance = sum(distances) / len(distances)
        distance /= keysize
        keysize_distances.append((keysize, distance))

    keysize = sorted(keysize_distances, key=lambda x: x[1])[0]
    print(keysize)
    i = 0
    for i in range(keysize[0]):
        block = b''
        for j in range(i, len(byte_string), keysize[0]):
            block += bytes(byte_string[j])
            print(block)


if __name__ == '__main__':
    main()
