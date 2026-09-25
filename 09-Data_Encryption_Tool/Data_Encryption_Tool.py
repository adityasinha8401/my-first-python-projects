print("=====WELCOME TO THE DATA ENCRYPTION TOOL=====")
message=input("Enter The Text You Want To Encrypt(Only In Upper Case Letters):")
new_message=""
for character in message:
    if character in message=="":
        new_message+=character
    else:
        letter_code=ord(character)
        new_letter_code=letter_code+4
        new_message+=chr(new_letter_code)
print("=====ENCRYPTED MESSAGE=====")
print("Original Message:",message)
print("Encrypted Message:",new_message)
input("Enter Done To Exit...")
