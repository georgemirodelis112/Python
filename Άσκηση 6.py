myString =raw_input('Give me a sentence : \n')
myList=list(myString.split())
a=len(myList)
a=int(a)
for i in range(a):
    newString=myList[i] 
    if (newString[0]!='0'and newString[0]!='1'and newString[0]!='2' and
        newString[0]!='3'and newString[0]!='4'and newString[0]!='5' and
        newString[0]!='6'and newString[0]!='7'and newString[0]!='8' and
        newString[0]!='9'and newString[0]!='!'and newString[0]!='@' and
        newString[0]!='#'and newString[0]!='$'and newString[0]!='%' and
        newString[0]!='^'and newString[0]!='&'and newString[0]!='*' and
        newString[0]!='('and newString[0]!=')'and newString[0]!='-' and
        newString[0]!='_'and newString[0]!='='and newString[0]!='+' and
        newString[0]!='`'and newString[0]!='~'and newString[0]!=';' and
        newString[0]!=':'and newString[0]!='"'and newString[0]!='|' and
        newString[0]!=','and newString[0]!='<'and newString[0]!='.' and
        newString[0]!='>'and newString[0]!='/'and newString[0]!='?'):
            newString=newString[1:len(newString)]+' '+newString[0]
    else:
            newString=newString[0:len(newString)]+' '
    myList[i]=newString         
print ' '.join(myList).strip('[]')+'argh'
