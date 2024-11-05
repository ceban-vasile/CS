def create_alphabet():
    upper_alphabet = ['A', 'Ă', 'Â', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Î', 'J', 'K', 'L', 'M',
                      'N', 'O', 'P', 'Q', 'R', 'S', 'Ș', 'T', 'Ț', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return upper_alphabet

def create_key(msg, key):
    key_array = []
    j = 0
    for i in range(len(msg)):
        key_array.append(key[j])
        j = (j + 1) % len(key)

    return key_array


def encrypt(msg, key):
    alphabet = create_alphabet()

    msg = msg.replace(" ", "").upper()

    key_array = create_key(msg, key)

    result = ""

    for i in range(len(msg)):
        k = (alphabet.index(msg[i])+alphabet.index(key_array[i]))%len(alphabet)
        result = result+alphabet[k]

    return result

def decrypt(msg, key):
    alphabet = create_alphabet()

    msg = msg.replace(" ", "").upper()

    key_array = create_key(msg, key)

    result = ""

    for i in range(len(msg)):
        k = (alphabet.index(msg[i])-alphabet.index(key_array[i]))%len(alphabet)
        result = result+alphabet[k]

    return result


def main():
    while True:
        operation = input("Choose operation (encrypt/decrypt): ").strip().lower()
        if operation not in ['encrypt', 'decrypt']:
            print("Please enter 'encrypt' or 'decrypt'.")
            continue

        msg = input("Enter the message or cryptogram: ").strip()

        key = input("Enter the key (at least 7 characters): ").strip().upper()

        if len(key) < 7:
            print("Key must be at least 7 characters long.")
            continue

        if operation == 'encrypt':
            encrypted_msg = encrypt(msg, key)
            print("Encrypted message:", encrypted_msg)
        else:
            decrypted_msg = decrypt(msg, key)
            print("Decrypted message:", decrypted_msg)

        if input("Do you want to continue? (yes/no): ").strip().lower() != 'yes':
            break

if __name__ == "__main__":
    main()
