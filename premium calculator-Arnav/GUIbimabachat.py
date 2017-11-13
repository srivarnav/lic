

#jeevananand

from Tkinter import*
from tkMessageBox import*
import calculations 
import bimabachat


root1=Tk()





Label (root1,text="Minimum Age",font="verdana 12 bold ").grid(row=0,column=2)
Label (root1,text="Term    Max Age   Min S.A.",font="verdana 12 bold ").grid(row=1,column=2)
Label (root1,text="9 yrs   66 yrs      Rs 35000",font="verdana 12 bold ").grid(row=2,column=2)
Label (root1,text="12 yrs  63 yrs      Rs 50000",font="verdana 12 bold ").grid(row=3,column=2)
Label (root1,text="15 yrs  60 yrs      Rs 70000",font="verdana 12 bold ").grid(row=4,column=2)

Label (root1,text="Enter Sum Assured :",font="verdana 10").grid(row=5,column=1)
e1=Entry(root1,bd=5)
e1.grid(row=5,column=3)

Label (root1,text="Enter Term  :",font="verdana 10").grid(row=6,column=1)
v1 = IntVar()
w=OptionMenu(root1,v1,"9","12","15").grid(row=6,column=3)

Label (root1,text="Enter Age [MIn 15] :",font="verdana 10").grid(row=7,column=1)
e2=Entry(root1,bd=5)
e2.grid(row=7,column=3)

Label(root1,text="Mode of Payment :",font="verdana 10").grid(row=8,column=1)
v2=IntVar()
'''Radiobutton(root1,text="Yearly",variable=v2,value=1,sticky=w).grid(row=8,column=3)
Radiobutton(root1,text="Half yearly",variable=v2,value=2).grid(row=9,column=3)
Radiobutton(root1,text="Quaterly",variable=v2,value=3).grid(row=10,column=3)
Radiobutton(root1,text="Monthly",variable=v2,value=4).grid(row=11,column=3)'''
Label(root1,text="Single Premium",font="Arial 10 bold").grid(row=8,column=3)
def calc(sa,mode,tp,term):

    
    if term==9:
        if sa>=75000 and sa <=145000:
            tp=tp-(tp*6/100)
        elif sa>=150000:
            tp=tp-(tp*8/100)
    elif term==12:
        if sa>=10000 and sa <=195000:
            tp=tp-(tp*4/100)
        elif sa>=200000:
            tp=tp-(tp*6/100)
    elif term==15:
        if sa>=150000 and sa <=295000:
            tp=tp-(tp*3/100)
        elif sa>=300000:
            tp=tp-(tp*5/100)



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


def calculate():
    sa=int(e1.get())
    term= v1.get()
    

    age=int(e2.get())
    
    
    mode=v2.get()
    
    if term==9:
        DX=bimabachat.D9
        print 0
    elif term==12:
        DX=bimabachat.D12
    elif term==15:
        DX=bimabachat.D15

    print DX[age]
    tp=DX[age]

   
    
    print sa,type(sa),mode,type(mode),tp,type(tp)
    tabular = calc(sa,mode,tp,term)
    Button(root1,text="",width=28).grid(row=13,column=2)
    Label(root1,text="Rs"+str(tabular),font="verdana 12 bold").grid(row=13,column=2)
    #s=showinfo(title="PREMIUM",message=tabular)
    
    
Button(root1,text="Premium",font="verdana 11 bold",justify=CENTER,bd=6,command=calculate).grid(row=12,column=2)


Label(root1,text="PREMIUM :",font="verdana 12 bold").grid(row=13,column=1)



root1.mainloop()



