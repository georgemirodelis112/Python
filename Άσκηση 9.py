def function(x):
    myList=list(x)
    a=len(myList)
    b=1#arxikopio
    n=0#metritis
    while(a>1):
        for i in range(a):
            myList[i]=int(myList[i])#metasximatizo se akereo to string
        for i in range(a):
            b *=myList[i]#vasismeno stin methodo tou paragontikou
        if(b>=0 and b<=9):#elenxos 
            n=n+1#afksisi tou metriti kata 1 ga na mporo na ipologiso ta vimata
            break
        else:#se periptosi pou den petixei o parapano elenxos
            n=n+1#tha afksiso to vima kata 1 pali
            myList=list(str(b))#tha metatrepso ton akereo se string
            a=len(myList)#tha vro to mikos tou to neo omos afti tin fora kai tha ksanatreksei tin loop(while)
    b=int(b)#ton kano pali akereo gt thelo na emfaniso arithmo sta parakato print
    #to 'n' den xreiazete metatropi gt einai apo tin fisi tou akereos
    print 'To apotelesma einai:',b
    print 'H xroniki poliplokotita metatropis tou dosmenou akereou se monopsifio einai:','O(',n,')'

myString=raw_input('Give me a number: \n')#eisodos apo to pliktrologio
function(myString)#klhsh tis sinartisi kai emfanisi apotelesmaton stin othoni
        


    
           

    
        
         
        
        
