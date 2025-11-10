# Enter your code here. Read input from STDIN. Print output to STDOUT
# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# sample input: 1222311
# sample output: (1, 1) (3, 2) (1, 3) (2, 1)

def compress_string(my_list):
    j = my_list[0]
    freq = 1
    o_list = []
    for i in my_list[1:]: 
        if j == i: 
            freq += 1 
        else:
            o_list.append(str((freq, int(j))))
            freq = 1
        j = i 
    o_list.append(str((freq, int(j))))
    s = " ".join(o_list)
    print(s) 
    
s = input()
compress_string(s)
