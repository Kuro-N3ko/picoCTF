![image](https://github.com/user-attachments/assets/34dfbff7-c7ce-4f06-9ff8-20b24471fe5e)

at this challenge we have a python script 
import sys

def exit():
  sys.exit(0)

def scramble(L):
  A = L
  i = 2
  while (i < len(A)):
    A[i-2] += A.pop(i-1)
    A[i-1].append(A[:i-2])
    i += 1
    
  return L

def get_flag():
  flag = open('flag.txt', 'r').read()
  flag = flag.strip()
  hex_flag = []
  for c in flag:
    hex_flag.append([str(hex(ord(c)))])

  return hex_flag

def main():
  flag = get_flag()
  cypher = scramble(flag)
  print(cypher)

if __name__ == '__main__':
  main()

when i connect to server using netcat it display a "nested list" in string form.  (cuz this challenge provides a dynamic flag through netcat port so we can't use nested lists in code python)

The hint of this chall suggests using "eval()" to convert the flag into a list of strings.When the list is coverted, the second hint directs you to focus only on outer list which can be achieved by funct "extract_outer_list()" 
and this is python decode script :

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


