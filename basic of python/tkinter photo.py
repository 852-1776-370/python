from tkinter import *
root=Tk()
root.title("ramesh giri")
#root.iconphoto("C:/Users/rames/Downloads/saloni.jpg")
e=Entry(root,border=10)
e.grid(row=0,column=3,padx=20,pady=20)
def button(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def delete():
    e.delete(0,1)
def add():
   first_number=e.get()
   global f_num
   f_num=getdouble(first_number)
   e.delete(0,END)
def equal():
    second_number=e.get()
    e.delete(0,END)
    e.insert(0,f_num+getdouble(second_number))
button9=Button(root,text="9",command=lambda:button(9))
button8=Button(root,text="8",command=lambda:button(8))
button7=Button(root,text="7",command=lambda:button(7))
button6=Button(root,text="6",command=lambda:button(6))
button5=Button(root,text="5",command=lambda:button(5))
button4=Button(root,text="4",command=lambda:button(4))
button3=Button(root,text="3",command=lambda:button(3))
button2=Button(root,text="2",command=lambda:button(2))
button1=Button(root,text="1",command=lambda:button(1))
button0=Button(root,text="0",command=lambda:button(0))
buttondelete=Button(root,text="delete",command=delete)
buttonequal=Button(root,text="=",command=equal)
buttonadd=Button(root,text="+",command=add)
button9.grid(row=1,column=0)
button8.grid(row=1,column=1)
button7.grid(row=1,column=2)
button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2)
button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)
button0.grid(row=4,column=0)
buttondelete.grid(row=4,column=1)
buttonequal.grid(row=4,column=2)
buttonadd.grid(row=5,column=0)

root.mainloop()

