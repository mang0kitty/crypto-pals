import base64
from Crypto.Cipher import AES

block_size = 16

# def hash(chunk):


def count_repetitions(ciphertext):
    chunks = [ciphertext[i:i+block_size]
              for i in range(0, len(ciphertext), block_size)]

    repetition_count = len(chunks)-len(set(chunks))
    return {"ciphertext": ciphertext, "repetitions": repetition_count}


def main():
    ciphertext = [bytes.fromhex(line.strip()) for line in open('8.txt')]
    repetitions = [count_repetitions(cipher) for cipher in ciphertext]

    most_repetitions = sorted(
        repetitions, key=lambda x: x["repetitions"], reverse=True)[0]
    print("CipherText: {}".format(most_repetitions["ciphertext"]))
    print("Repeating blocks: {}".format(most_repetitions["repetitions"]))


if __name__ == '__main__':
    main()
