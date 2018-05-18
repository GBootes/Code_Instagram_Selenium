def num(x):

    a=''
    k=True
    for i in x:
        
        if(i.isdigit() and i=='3' and len(a)<11 and k):

            a=a+i
            k=False

        elif(i.isdigit()  and len(a)<11 and k==False):

            a=a+i
            
    return a

            
