import string

print('''

    ,abPPYba,    ,adppYYa,    ,adPPYba,  ,abdPPYba,  ,adppYYa,    8b,dPPYba,
  a8"        ""  ""     'Y8  a8P_____88  I8[    ""   ""     'Y8   88p'   "Y8
  8b             ,adPPPPP88  8PP"""""""    '"Y8bda,  ,adPPPPP88   88
  "8a,     ,aa  88,     ,88  "8B,    ,aa  aa    ]8I  88,     ,88  88
    '"Ybbd8 "'   '"8bbdP"Y8   '"Ybbd8"'   '"Ybbdp""  '"8bbdP"Y8   88

                                  88
                (@)               88
    ,abPPYba,        8b,dPPYba,   88,dPPYba,    ,adPPYba,   8b,dPPYba,  
  a8"       ""  88   88p'    "8a  88P'    "8a  a8P_____88   88p'   "Y8
  8b            88   88        d8 88       88  8PP"""""""   88
  "8a,     ,aa  88   88b,    ,a8" 88       88  "8B,    ,aa  88
    '"Ybbd8 "'  88   88'YbbdP"'   88       88   '"Ybbd8"'   88
                     88
                     88
''')
alphabet = string.ascii_lowercase
def ceaser_cipher(original_text, shift_amount,encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter

        else:

            if encode_or_decode == "encode":
                 shift_amount *= 1

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here's the '{encode_or_decode}d' result:'{output_text}'")

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    if  direction not in ["decode" ,  "encode"]:
         print("invalid input")
         continue
    msg = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceaser_cipher(original_text=msg,shift_amount=shift,encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again.otherwise,type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("goodbye")



