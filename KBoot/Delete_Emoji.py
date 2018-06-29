def without_emoji(x):

    a=''

    for i in x:

        if(i.isalpha() or i.isdigit() or i.isspace()):

            a=a+i

    return a

            
