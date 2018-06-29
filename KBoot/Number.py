def num(x):

    for h in range(0,2):
        
        a=''
        k=True
        for i in x:
        
            if(i.isdigit() and i=='3' and len(a)<10 and k):

                a=a+i
                k=False

            elif(i.isdigit() and len(a)<10 and k==False):

                a=a+i

        if (len(a)<7):

            a=''

        if(h==0 and len(a)>6):

            x=x.replace(a,'')
            num1=a
            print(x)

        elif(len(a)>6):

            num2=a

    try:
        
        if(num1==num2):

            num2=''
    except:

        num2=''
            
    return num1,num2

            
