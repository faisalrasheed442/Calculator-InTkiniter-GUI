from tkinter import *
from tkinter import ttk
from ttkthemes import  themed_tk as tk
# pre paring main window
root=tk.ThemedTk() #to use theme
root.get_themes()
root.set_theme("breeze") #theme name
root.geometry("400x250")
root.resizable(width=False,height=False)
root.title("My calculator")
# root.iconbitmap(r'D:\python\Tkiniter GUI work\img\cal1.ico')#changing icon
# main entery box to get valu
entry_box = Entry(root,font="calibri 14 bold", width=39, bd=4, justify=RIGHT, bg="#dfe6e9")
entry_box.grid(row=0,columnspan=8)
entry_box.insert(0,"0")
# ////////////////////////Function///////////////////////////////////////////////////
# ////////////////////////Function///////////////////////////////////////////////////
# ////////////////////////Function///////////////////////////////////////////////////
def entr_nmbr(x):
    if entry_box.get()=="0":
        entry_box.delete(0,"end")
        entry_box.insert(0,str(x))
    else:
        length=len(entry_box.get())
        entry_box.insert(length,x)
#/////////////////////////////
def entr_op(x):
    if entry_box.get()!="0":
        length=len(entry_box.get())
        entry_box.insert(length,btn_operator[x]["text"])
def clear_in():
    length=len(entry_box.get())
    print(length)
    entry_box.delete(length-1,"end")
    if length==1:
        entry_box.insert(0,"0")  
def clearall():
    entry_box.delete(0,"end") 
    entry_box.insert(0,"0")  
def calcu():
    conntent=entry_box.get()  
    x=eval(conntent)
    entry_box.delete(0,"end")
    entry_box.insert(0,x)
def calcuu(event):
    conntent=entry_box.get()  
    x=eval(conntent)
    entry_box.delete(0,"end")
    entry_box.insert(0,x)
# Buton numbers //////////////////////////////////////////////////////////////////////////////////////////////
# Buton numbers //////////////////////////////////////////////////////////////////////////////////////////////
# Buton numbers //////////////////////////////////////////////////////////////////////////////////////////////
ss = ttk.Style()
ss.configure("Bold.TButton", font=('calibri', 14 ))
btn_nmbr=[]
for x in range(10):
    btn_nmbr.append(ttk.Button(root,width=6, text=str(x), style="Bold.TButton",command=lambda y=x:entr_nmbr(y)))
btn_text=1
for i in range(1,4):
    for j in range(0,3):
        btn_nmbr[btn_text].grid(row=i, column=j)
        btn_text +=1
# ////////////operator btn//////////////////////////////////////////
# ////////////operator btn//////////////////////////////////////////
# ////////////operator btn//////////////////////////////////////////
btn_operator=[]
for x in range(4):
    btn_operator.append(ttk.Button(root,width=6, style="Bold.TButton",command=lambda y=x: entr_op(y)))
btn_operator[0].configure(text="+")
btn_operator[1].configure(text="-")
btn_operator[2].configure(text="*")
btn_operator[3].configure(text="/")
operator_tex=0
btn_operator[3].grid(row=4, column=4, ipady=4)
for x in range(1,4):
    btn_operator[operator_tex].grid(row=x, column=4)
    operator_tex +=1
#//////////////////////////equal btn?////////
#//////////////////////////equal btn?////////
#//////////////////////////equal btn?////////
btn_oth=[]
for x in range(5):
    btn_oth.append(ttk.Button(root,width=6, style="Bold.TButton"))
btn_oth[0].configure(text="0",command=lambda y=0: entr_nmbr(y))
btn_oth[0].grid(row=4, column=1,ipady=4,)
btn_oth[1].configure(text=".",command=lambda y=".": entr_nmbr(y))
btn_oth[1].grid(row=4, column=0,ipady=4)
clr_img=PhotoImage(file="img/clear4.png")
btn_oth[2].configure(image=clr_img,command=clear_in)
btn_oth[2].grid(row=4, column=2,ipadx=14,pady=3)
btn_oth[3].configure(text="C",command=clearall)
btn_oth[3].grid(row=5, column=0)
btn_oth[4].configure(text="=",command=calcu)
btn_oth[4].configure(text="=")
btn_oth[4].grid(row=5, column=2)
root.bind('<Return>', calcuu)
root.mainloop()
