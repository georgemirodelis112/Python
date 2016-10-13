myString=raw_input('Give me a sentence : \n') 
myList=list(myString.split())
a=len(myList)
oldString=''
for i in range(a):
    b=len(myList[i])
    b=int(b)
    m=int(b)-2
    newString=myList[i]
    for j in range(b):
        if (newString[j]=='0'or newString[j]=='1'or newString[j]=='2' or
        newString[j]=='3'or newString[j]=='4'or newString[j]=='5' or
        newString[j]=='6'or newString[j]=='7'or newString[j]=='8' or
        newString[j]=='9'or newString[j]=='!'or newString[j]=='@' or
        newString[j]=='#'or newString[j]=='$'or newString[j]=='%' or
        newString[j]=='^'or newString[j]=='&'or newString[j]=='*' or
        newString[j]=='('or newString[j]==')'or newString[j]=='-' or
        newString[j]=='_'or newString[j]=='='or newString[j]=='+' or
        newString[j]=='`'or newString[j]=='~'or newString[j]==';' or
        newString[j]==':'or newString[j]=='"'or newString[j]=='|' or
        newString[j]==','or newString[j]=='<'or newString[j]=='.' or
        newString[j]=='>'or newString[j]=='/'or newString[j]=='?'):
            m=m-1
            oldString=oldString+newString[j]
        else:
            oldString=oldString
    m=str(m)
    newString=newString[0]+oldString+m+newString[-1]
    myList[i]=newString
print ' '.join(myList).strip('[]')

