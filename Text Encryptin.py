def text_encryptin(text, shift):
    encrypted_text = ""
    for i in text:
        if i.isalpha():
            shifted = ord(i) + shift
            if i.isupper(): 
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            elif i.islower():
                if shifted > ord('z'):  
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += i 
    return encrypted_text

# -------------------------------------------------------------

def text_decryption(encrypted_text, shift):
    decrypted_text = ""
    for x in encrypted_text:
        if x.isalpha():
            shifted = ord(x) - shift
            if x.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            elif x.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += x
    return decrypted_text

# -----------------------------------------------------------------

print("Welcome to Text Encryptor!")
while True:
    print("1.Encryption")
    print("2.Decryption")
    print("3.How do I do?")
    print("4.Exit")
    choise = input("Enter your choice from 1 to 4: ")
    if choise == "1":
        print("-"*30)
        text = input("Enter Your Text: ")
        shift = 5
        encrypted_text = text_encryptin(text, shift)
        print(f"Original texts: '{text}'")
        print(f"Encrypted texts: '{encrypted_text}'")
        print("-"*30)
    elif choise == "2":
        encrypted_text = input("Enter The Encrypted Text: ")
        shift = 5
        decrypted_text = text_decryption(encrypted_text, shift)
        print(f"Encrypted texts: '{encrypted_text}'")
        print(f"Original texts: '{text}'")
    elif choise == "3":
        print("-"*30)
        print(""" *** I'm encrypting texts.
 For example, you made password for the X site
 and you want to encrypt the password in a way so that no one can know the password except you and this is through the -> 'Encryption' menu.
 Or you did this and want to remember the word by deciphering you can do this via the ->'Decryption' menu ***""")
        print("   >> Made by SABER JR <<")
        print("-"*30)
    elif choise == "4":
        print("-"*30)
        print("Thank you for trying our application!")
        break
    else:
        print("-"*30)
        print("Invalid choise!, Please enter a number from 1 to 3")