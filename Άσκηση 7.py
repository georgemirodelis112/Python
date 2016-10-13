#edo vriskete i sinartisi 
def SquareOfMyNumber(x):
    if x == 1:
        return True
    low = 0
    high = x //2
    root = high
    while(root * root != x):
       root = (low + high) // 2
       if(low + 1 >= high):
          return False
       if(root * root > x):
          high = root
       else:
          low = root
    return True

#edo apefthinomaste ston xristi
x=raw_input('Give me a number: \n')
x=int(x)

#edo ginete o aparaititos elenxos gia tin
#emfanisi tou antistixou apotelesmatos
if(SquareOfMyNumber(x)):
    print ('true')
else:
    print('false')
