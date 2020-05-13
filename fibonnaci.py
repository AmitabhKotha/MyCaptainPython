def fibonnaci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else :
        return fibonnaci(n-1)+fibonnaci(n-2)

seq_len = int(input("Enter the length of the fibonnaci sequence : "))
for i in range(seq_len):
    if i != seq_len-1:
        print(fibonnaci(i),end=",")
    else :
        print(fibonnaci(i))
