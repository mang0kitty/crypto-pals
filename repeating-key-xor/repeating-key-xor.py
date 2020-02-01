def repeating_key_xor(message_bytes, key):
        output_bytes = b''
        for i, byte in enumerate(message_bytes):
            output_bytes += bytes([key[i % len(key)] ^ byte])
        return output_bytes


# def decrypt_repeating_key_xor(encrypted_message, key):


def main():
    key = b"ICE"
    message = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    ciphertext = repeating_key_xor(message, key)
    print(ciphertext.hex())

    decrypted = repeating_key_xor(ciphertext, key)
    print(decrypted.decode("utf-8"))


if __name__ == '__main__':
    main()
