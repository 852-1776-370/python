from tkinter import *
from math import *
root=Tk()
root.title("simple calculator")
e=Entry(root,borderwidth=35,border=4)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#e.insert(0,"enter your name")
def button_add(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def sin(string):
    current=e.get()
    global math
    math="sin"
    e.delete(0,END)
    e.insert(0,str(current)+getdouble(string))

def cos(string):
    current=e.get()
    global math
    math="cos"
    e.delete(0,END)
    e.insert(0,str(current)+str(string))
def tan(string):
    current=e.get()
    global math
    math="tan"
    e.delete(0,END)
    e.insert(0,str(current)+getdouble(string))

def clear():
    e.delete(0,END)
def delete():
  e.delete(0,1)

def button_add1():
    first_number=e.get()
    global f_num
    global math
    math = "addtion"
    f_num = getdouble(first_number)
    e.delete(0,END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if(math=="addtion"  ) :
        e.insert(0,f_num + getdouble(second_number))
    if (math == "subtract"):
        e.insert(0, f_num - getdouble(second_number))
    if (math == "multiply"):
        e.insert(0, f_num * getdouble(second_number))
    if(math == "devide"):
          e.insert(0, f_num / getdouble(second_number))
    if(math == "="):
          e.insert(0, f_num )
    if(math=="percent"):
        e.insert(0,(f_num/100)*getdouble(second_number))
    if(math=="power"):
        e.insert(0,f_num**getdouble(second_number))
    if(math=="sin"):
        e.insert(0,(sin(getdouble(second_number))))
def substract():
    first_number = e.get()
    global f_num
    global math
    math = "subtract"
    f_num = getdouble(first_number)
    e.delete(0, END)


def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiply"
    f_num = getdouble(first_number)
    e.delete(0, END)


def devide():
    first_number = e.get()
    global f_num
    global math
    math = "devide"
    f_num = getdouble(first_number)
    e.delete(0, END)
def percent():
    first_number = e.get()
    global f_num
    global math
    math = "percent"
    f_num = getdouble(first_number)
    e.delete(0, END)
def power():
    first_number = e.get()
    global f_num
    global math
    math = "power"
    f_num = getdouble(first_number)
    e.delete(0, END)
button1= Button(root,text="1",command=lambda:button_add(1))
button2=Button(root,text="2",command=lambda:button_add(2))
button3=Button(root,text="3",command=lambda:button_add(3))
button4=Button(root,text="4",command=lambda:button_add(4))
button5=Button(root,text="5",command=lambda:button_add(5))
button6=Button(root,text="6",command=lambda:button_add(6))
button7=Button(root,text="7",command=lambda:button_add(7))
button8=Button(root,text="8",command=lambda:button_add(8))
button9=Button(root,text="9",command=lambda:button_add(9))
button0=Button(root,text="0",command=lambda:button_add(0))
buttonpoint=Button(root,text="0.",command=lambda: button_add(.0))
buttonadd=Button(root,text="+",command=button_add1)
buttonmul=Button(root,text="*",command=multiply)
buttonsub=Button(root,text="-",command=substract)
buttondiv=Button(root,text="/",command=devide)
buttonpercent=Button(root,text="%",command=percent)
buttonroot=Button(root,text="^",command=power)
buttonqual=Button(root,text="=",command=lambda:button_equal())
buttonclear=Button(root,text="clear",command=lambda:clear())
buttondelete=Button(root,text="delete",command=lambda:delete())
buttonsin=Button(root,text="sin(",command=lambda:sin("sin"))
buttoncos=Button(root,text="cos",command=lambda:cos("cos"))
buttontan=Button(root,text="tan",command=lambda:tan("tan"))
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonadd.grid(row=4,column=1)
buttonqual.grid(row=4,column=2)
buttonmul.grid(row=5,column=2)
buttonclear.grid(row=5,column=0)
buttondiv.grid(row=5,column=1)
buttonsub.grid(row=6,column=1)
buttondelete.grid(row=6,column=2)
buttonpercent.grid(row=6,column=0)
buttonroot.grid(row=7,column=0)
buttonpoint.grid(row=7,column=1)
buttonsin.grid(row=7,column=2)
buttoncos.grid(row=8,column=0)
buttontan.grid(row=8,column=1)
root.mainloop()