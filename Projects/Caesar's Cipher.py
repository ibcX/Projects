
# Caesar's Cipher

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

task = input("Do you want to (e)ncrypt or (d)ecrypt?\n")
key_input = int(input("Please enter the key (0 to 25) to use.\n"))

message_encrypted = ""
message_decrypted = ""
if task == "e":
    message_encrypt = input("Enter the message to encrypt.\n").upper()
    for character in message_encrypt:
        i = 0
        if character not in alphabet:
            message_encrypted = message_encrypted + character
        else:
            for letter in alphabet:
                if character == letter:
                    if i+key_input <= 25:
                        message_encrypted = message_encrypted + alphabet[i+key_input]
                    else:
                        message_encrypted = message_encrypted + alphabet[i + key_input - 26]
                i += 1

    print(f"The encrypted message is: {message_encrypted}")


elif task == "d":
    message_decrypt = input("Enter to message to decrypt.\n")
    for character in message_decrypt:
        i = 0
        if character not in alphabet:
            message_decrypted = message_decrypted + character
        else:
            for letter in alphabet:
                if character == letter:
                    if i-key_input >= 0:
                        message_decrypted = message_decrypted + alphabet[i-key_input]
                    else:
                        message_decrypted = message_decrypted + alphabet[i - key_input + 26]
                i += 1

    print(f"The decrypted message is: {message_decrypted}")