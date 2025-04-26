![image](https://github.com/user-attachments/assets/4b13498c-289f-4ead-8df9-224e2feae52c)

chúng ta có 1 file python bytecode disassembly,  https://artifacts.picoctf.net/c_titan/127/snake. Dấu hiệu rõ ràng là 

LOAD_CONST 0 (4)
LOAD_CONST 1 (54)
LOAD_CONST 2 (41)
LOAD_CONST 3 (0)

LOAD_CONST 29 (78)
BUILD_LIST 40  

đoạn chương trình trên LOAD_CONST liên tục 40 lần , mỗi lần 1 con số khác nhau,
rồi BUILD_LIST 40 ghép hết lại thành 1 list có 40 phần tử   

===> input_list chứa 40 số nguyên
![image](https://github.com/user-attachments/assets/1abcba83-6470-445a-b21f-66c91e018907)

và ta sẽ tạo  1 đoạn code py dịch ngược lại đoạn này (XOR decoding with a repeated key) và in ra flag

![image](https://github.com/user-attachments/assets/6e83b178-9a5c-4c28-926a-74466151a9d1)
Chức năng: Giải mã 40 số nguyên XOR với key "J_o3t" để ra chuỗi ẩn.

nhưng vấn đề là đoạn chuỗi key_str mà đề cho

           84 LOAD_CONST              30 ('J')
             86 STORE_NAME               1 (key_str)

          88 LOAD_CONST              31 ('_')
             90 LOAD_NAME                1 (key_str)
             92 BINARY_ADD
             94 STORE_NAME               1 (key_str)

         96 LOAD_NAME                1 (key_str)
             98 LOAD_CONST              32 ('o')
            100 BINARY_ADD
            102 STORE_NAME               1 (key_str)

         104 LOAD_NAME                1 (key_str)
            106 LOAD_CONST              33 ('3')
            108 BINARY_ADD
            110 STORE_NAME               1 (key_str)

         112 LOAD_CONST              34 ('t')
            114 LOAD_NAME                1 (key_str)
            116 BINARY_ADD
            118 STORE_NAME               1 (key_str)   ===> "j_o3t"
            
có thể ko được sắp xếp theo thứ tự nhằm đánh lạc hướng vì chỉ cần khóa xor thay đổi 1 chút là flag sẽ đổi theo (key_list = [ord(c) for c in key_str])
ờm thực ra mình cx chauw hiểu lắm: 

Dòng 2: key_str = 'J' → key_str là 'J'

Dòng 3: key_str = '_' + key_str → '_' + 'J' = '_J'

Dòng 4: key_str = key_str + 'o' → '_J' + 'o' = '_Jo'

Dòng 5: key_str = key_str + '3' → '_Jo' + '3' = '_Jo3'

Dòng 6: key_str = 't' + key_str → 't' + '_Jo3' = 't_Jo3'


cách 1 : Viết script tự động brute-force tất cả các thứ tự của key.

cách 2 : có thể từ format flag của đề dò ra xor_key trên cyberchef....
