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
