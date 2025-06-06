![image](https://github.com/user-attachments/assets/12523646-cdb3-4f27-803d-2a5f785dcee4)

---

source code 
```
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)



def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program

    Warning: this function was written quickly and needs proper error handling
    """

    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1 # need a value to return if 1 & 2 are equal

    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2

    print( "The number with largest positive magnitude is "
        + str(greatest_value) )



choose_greatest()

```

# Solution

```python
# Encrypted secret for Mr. Bezos (ROT47 encrypted)
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE0d_a3hgc3N"

# ROT47 reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
           "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

def rot47(text):
    """ROT47 encode/decode function."""
    rotated = ""
    for c in text:
        index = alphabet.find(c)
        if index != -1:
            rotated += alphabet[(index + 47) % len(alphabet)]
        else:
            rotated += c
    return rotated

def generate_flag():
    decoded = rot47(bezos_cc_secret)
    print(f"Flag: {decoded}")

if __name__ == "__main__":
    generate_flag()

```






```
picoCTF{1|\/|_4_p34|\|ut_502b984b}
```
