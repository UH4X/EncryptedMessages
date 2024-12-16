import os

os.system('cls')

print("""
      WELCOME! (THIS WAS MADE BY: C4X)
      Original Github Repository: https://github.com/C0dexH4xer/EncryptedMessages/

      This is a Cipther Encrypter
      You choose the addition
      to the ID's of the ASCII.

      Remember to write on the same ID-Range.
      Otherwise this might not work
      """)

quit_commands = ["exit", "quit", "bye", "farewell", "goodbye", "close", "leave", "cya"]
clear_commands = ["clear", "cls", "blank"]

while True:
    try:
        command = input("Command: ").lower()

        if command == "encrypt":
            
            os.system('cls')

            enc_message = input("Encrypt: ")
            enc_id = int(input("Provide Range-ID: "))
            encrypt_result = ""

            for enc_char in enc_message:

                enc_CharID = (ord(enc_char) + enc_id) % 1114111
                enc_char_msg = chr(enc_CharID)
                encrypt_result += enc_char_msg
            
            print(f"Encrypted code: {encrypt_result} - EncryptionID: {enc_CharID}")
            print()


#------------------------------------------------------------------------------

        elif command == "decrypt":

            dec_message = input("Decrypt: ")
            dec_id = int(input("Provide Range-ID: "))
            decrypt_result = ""

            for dec_char in dec_message:

                dec_CharID = (ord(dec_char) - dec_id) % 1114111
                dec_char_msg = chr(dec_CharID)
                decrypt_result += dec_char_msg
            
            print(f"Decrypted code: {decrypt_result} - EncryptionID: {dec_CharID}")
            print()

        elif command in quit_commands:
            print()
            print("You have chosen to quit the program!")
            break

        elif command == "help":
            print(f"""
                Help section!
                  
                  You have 4 options.

                  1. To exit:
                     write: {quit_commands}.

                  2. Clear:
                     Write: {clear_commands}.
                  
                  3. Encrypt:
                     To encryp, write: "Encrypt".
                  
                  4. Decrypt:
                     To decrypt, write: "Decrypt".
                  
                That's all for this script!
                    """)
            
        elif command in clear_commands:
            os.system('cls')
            print("The screen has been cleared!")
            print()

        

    except ValueError:
        print("An error has occoured...")
        print("Exiting...")
        break




print()
print("You managed to exit the whole program.")
print()








