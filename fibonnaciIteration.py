seq_len=int(input("Enter the sequence length : "))
a=0;b=1;c=a+b;
print(a,end=",")
print(b,end=",")
for i in range(seq_len-2):
    if i!=seq_len-3:
        print(c,end=",")
    else :
        print(c,end="")
    a=b
    b=c
    c=a+b
