fileEx ={
    "py":"python",
    "cpp":"c++",
    "doc":"Word",
    "docx":"Word",
    "rtf":"Rich Text Format",
    "wpd":"WordPerfect Document",
    "pdf":"Portable Document File"
    "txt":"text"
}
filename = input("Input the Filename: ")
exten = filename.split(".")
#print(fileEx[exten[-1]])
if exten[-1] in fileEx.keys():
    print ("The extension of the file is : " + repr(fileEx[exten[-1]]))
else :
    print ("The extension of the file is : " + repr(exten[-1]))
