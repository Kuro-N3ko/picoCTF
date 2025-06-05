```python
def extract_outer_list(array):
    return [item for inner in array for item in inner if isinstance(item, str)]

def get_flag():
    flag = []
    with open('flag.txt', 'r') as file:
        flag = file.read()

    list_string = eval(flag)
    flag = extract_outer_list(list_string)

    hex_flag = []
    for c in flag:
        hex_flag.append(chr(int(c, 16)))

    return hex_flag

def main():
    flag = get_flag()
    print(''.join(flag))

if __name__ == "__main__":
    main()
```
