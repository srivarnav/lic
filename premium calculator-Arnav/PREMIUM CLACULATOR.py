
from Tkinter import*

from tkMessageBox import*
def guijeevananand():
    import GUIjeevananand
def guijeevanrakshak():
    import GUIjeevanrakshak
def guinewendowment():
    import GUInewendowment
def guimoneyback():
    import GUImoneyback
def guibeemabachat():
    import GUIbimabachat

root=Tk()

root.config(bg="grey")

Label(root,text="Endowment Plans",font="Verdana 12 bold ").grid(row=0,column=1)

Button(root,text="Jeevan Anand",width=28,height=1,command=guijeevananand).grid(row=1,column=1)
Button(root,text="Jeevan Rakshak",width=28,height=1,command=guijeevanrakshak).grid(row=3,column=1)
'''Button(root,text="Jeevan Lakshya",width=28,height=1).grid(row=2,column=0)'''
Button(root,text="New Endowment Plan",width=28,height=1,command=guinewendowment).grid(row=2,column=1)
'''
Button(root,text="New Endowment plan Plus",width=28,height=1).grid(row=3,column=0)
Button(root,text="New Limited period Endowment Plan",width=28,height=1 ).grid(row=3,column=3)'''
Label(root,text="").grid(row=4)


Label(root,text="Money Back PLans",font="Verdana 12 bold ").grid(row=5,column=1)

Button(root,text="Beema Bachat",width=28,height=1,command=guibeemabachat).grid(row=6,column=1)
Button(root,text="Money Back",width=28,height=1,command=guimoneyback).grid(row=7,column=1)
'''
Button(root,text="Jeevan Tarun",width=28,height=1).grid(row=7,column=2)
Button(root,text="Child Money Back",width=28,height=1).grid(row=7,column=2)

Label(root,text=" ").grid(row=8)


Label(root,text="Term Plans",font="Verdana 12 bold ").grid(row=9,column=1)

Button(root,text="Anmol Jeevan",width=28,height=1).grid(row=10,column=0)
Button(root,text="Amulya Jeevan",width=28,height=1).grid(row=10,column=2)

Label(root,text=" ").grid(row=11)


Label(root,text="Pension/Annuity Plans",font="Verdana 12 bold ").grid(row=12,column=1)

Button(root,text="Jeevan Nidhi",width=28,height=1).grid(row=13,column=0)
Button(root,text="Jeevan Akshay",width=28,height=1).grid(row=13,column=2)
Button(root,text="Varishtha Pension Beema Yojana",width=28,height=1).grid(row=14,column=0)
Label(root,text=" ").grid(row=15)
'''

'''
Label(root,text="Child Plans",font="Verdana 12 bold ").grid(row=16,column=1)

Button(root,text="Jeevan Tarun",width=28,height=1).grid(row=17,column=0)
Button(root,text="Child Money Back",width=28,height=1).grid(row=17,column=2)
Label(root,text=" ").grid(row=18)


Label(root,text="Health Plans",font="Verdana 12 bold ").grid(row=19,column=1)

Button(root,text="Jeevan Arogya",width=28,height=1).grid(row=20,column=1)
Label(root,text=" ").grid(row=21)
'''

root.mainloop()
