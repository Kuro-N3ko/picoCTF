![image](https://github.com/user-attachments/assets/62f388ea-0389-4030-aea4-508ac04bf9a2)

Analyze this file on IDA, and I get the first part of the flag `picoCTF{wELF_d0N3_mate_`

```
  v39 = __readfsqword(0x28u);
  std::allocator<char>::allocator(&v21, argv, envp);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(
    v22,
    "picoCTF{wELF_d0N3_mate_",
    &v21);
```

I will give the pseudocode of the main fuction at IDA in another file

Now I will analyze the flow of pseudocode

```
std::string v22 = "picoCTF{wELF_d0N3_mate_";
std::string v23 = "0";
std::string v24 = "5";
std::string v25 = "d";
std::string v26 = "3";
std::string v27 = "2";
std::string v28 = "a";
std::string v29 = "a";
std::string v30 = "e";
std::string v31 = "e";
std::string v32 = "d";
std::string v33 = "b";
std::string v34 = "e";
std::string v35 = "6";
std::string v36 = "c";
std::string v37 = "9";
std::string v38 = "8";
```

There are 37 strings, start with `v22` which is the first part of the flag and others will participate in solving problem.

```
  if ( *(char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v24, 0LL) <= 65 )
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v34);
```
It looks complicated but it's actually just basic comparision statement to concatenate strings. I will convert it to python to easy to understand: if ord(v24[0]) <= 65: ==> v22 += v34 

I will do the same thing with other.

```
  if ( *(_BYTE *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v35, 0LL) != 65 )
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v37);
```

```
  if ( v19 - *(char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v30, 0LL) == 3 )
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v26);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v25);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v28);
  if ( *(_BYTE *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v29, 0LL) == 71 )
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v29);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v27);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v36);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v23);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, v31);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v22, 125LL);
```
125LL = '}'

I wrote a py script to solve this

```python
def combine_flag():
    flag = "picoCTF{wELF_d0N3_mate_"  #v22
    
    v23 = "0"
    v24 = "5"
    v25 = "d"
    v26 = "3"
    v27 = "2"
    v28 = "a"
    v29 = "a"
    v30 = "e"
    v31 = "e"
    v32 = "d"
    v33 = "b"
    v34 = "e"
    v35 = "6"
    v36 = "c"
    v37 = "9"
    v38 = "8"
    
    if ord(v24[0]) <= 65:
        flag += v34
        
    if ord(v35[0]) != 65:
        flag += v37
    
    if ord(v30[0]) == 3:
        flag += v29
    
    flag += v26
    flag += v25
    flag += v28
    
    if ord(v29[0]) == 71:
        flag += v29
        
    flag += v27
    flag += v36
    flag += v23
    flag += v31
    flag += "}"
    
    return flag

print(combine_flag())

```
