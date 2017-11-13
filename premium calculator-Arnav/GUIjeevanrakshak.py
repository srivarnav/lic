
#jeevanrakshak

from Tkinter import*
from tkMessageBox import*
import calculations 
import jeevanrakshak


root1=Tk()





Label (root1,text="Enter age from 8-55",font="verdana 12 bold ").grid(row=1,column=2)
Label (root1,text="Min term = 10yrs",font="verdana 12 bold ").grid(row=2,column=2)
Label (root1,text="Max term = 20yrs",font="verdana 12 bold ").grid(row=3,column=2)
Label (root1,text="Min S.A. = Rs 75000 + 5000 upto 200000",font="verdana 12 bold ").grid(row=4,column=2)

Label (root1,text="Enter Sum Assured :",font="verdana 10").grid(row=5,column=1)
e1=Entry(root1,bd=5)
e1.grid(row=5,column=3)

Label (root1,text="Enter Term  :",font="verdana 10").grid(row=6,column=1)
v1 = IntVar()
w=OptionMenu(root1,v1,"10","15","20").grid(row=6,column=3)

Label (root1,text="Enter Age [8-50] :",font="verdana 10").grid(row=7,column=1)
e2=Entry(root1,bd=5)
e2.grid(row=7,column=3)

Label(root1,text="Mode of Payment :",font="verdana 10").grid(row=8,column=1)
v2=IntVar()
Radiobutton(root1,text="Yearly",variable=v2,value=1,sticky=w).grid(row=8,column=3)
Radiobutton(root1,text="Half yearly",variable=v2,value=2).grid(row=9,column=3)
Radiobutton(root1,text="Quaterly",variable=v2,value=3).grid(row=10,column=3)
Radiobutton(root1,text="Monthly",variable=v2,value=4).grid(row=11,column=3)


def calculate():
    sa=int(e1.get())
    term= v1.get()
    
    age=int(e2.get())
    
    
    mode=v2.get()
    
    if term==10:
        DX=jeevanrakshak.D10
        print 0
    elif term==15:
        DX=jeevanrakshak.D15
    elif term==20:
        DX=jeevanrakshak.D20
    
    print DX[age]
    tp=DX[age]

    #print sa,type(sa),mode,type(mode),tp,type(tp)
    tabular = calculations.premcalc(sa,mode,tp)
    Button(root1,text="",width=28).grid(row=13,column=2)
    Label(root1,text="Rs"+str(tabular),font="verdana 12 bold").grid(row=13,column=2)
    #s=showinfo(title="PREMIUM",message=tabular)
    
    
Button(root1,text="Premium",font="verdana 11 bold",justify=CENTER,bd=6,command=calculate).grid(row=12,column=2)


Label(root1,text="PREMIUM :",font="verdana 12 bold").grid(row=13,column=1)



root1.mainloop()



