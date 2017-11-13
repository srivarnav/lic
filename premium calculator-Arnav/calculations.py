
def premcalc(sa,mode,tp):

    if mode==1:
        tp=tp-(tp*0.02)
    elif mode==2:
        tp=tp-(tp*0.01)

    if sa>=200000 and sa <=495000 :
        tp=tp-2
    elif sa>=500000 :
        tp=tp-3

    #accidental benfits
    tp=tp+1

    x=sa/1000
    tp=tp*x

    if mode==1:
        tp=tp/1
    elif mode==2:
        tp=tp/2
    elif mode==3:
        tp=tp/4
    elif  mode==4:
        tp=tp/12
    
    tp=tp+(tp*3.09/100)
    print tp
    return tp
    
    
x=premcalc (100000,1,92.05)
x=x+(x*3.09/100)
#print x
