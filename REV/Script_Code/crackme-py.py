```
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
