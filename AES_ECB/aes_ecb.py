import base64
from Crypto.Cipher import AES


def decode(key, decipher):
    fw = open("decoded.txt", "wb")
    with open("7.txt") as f:
        ciphertext = base64.b64decode(f.read())
        fw.write(decipher.decrypt(ciphertext))
        plaintext = decipher.decrypt(ciphertext)
        try:
            print("The message is authentic:", plaintext)
        except ValueError:
            print("Key incorrect or message corrupted")


def main():
    key = b'YELLOW SUBMARINE'
    decipher = AES.new(key, AES.MODE_ECB)
    decode(key, decipher)


if __name__ == '__main__':
    main()
