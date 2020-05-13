word = input("Enter any string : ")
frequency={}
for i in range(len(word)):
    if word[i] in frequency.keys():
        frequency[word[i]]+=1
    elif word[i] not in frequency.keys():
        frequency[word[i]]=1
print("The Frequency of letters is :")
for i,j in frequency.items():
    print(f"{i} : {j}")
