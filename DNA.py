def comp(seq):
    comp_dict = {"A":"T", "T":"A", "C":"G", "G":"C"}
    seq_comp=""
    for char in seq:
        seq_comp+=comp_dict[char]
    return seq_comp

def rev(seq):
    seq_rev="".join(reversed(seq))
    return seq_rev

def rev_comp(seq):
    tmp=comp(seq)
    return rev(tmp)

src = input("DNA sequence : ")
cnvt = int(input("1(Comp), 2(Rev), 3(Rev_Comp) : "))
if(cnvt>=1 and cnvt<=4):
    if(cnvt==1):
        rst=comp(src)
    elif(cnvt==2):
        rst=rev(src)
    else:
        rst=rev_comp(src)
    print(src, "->", rst)
else:
    print("1(Comp), 2(Rev), 3(Rev_Comp)!!!")


