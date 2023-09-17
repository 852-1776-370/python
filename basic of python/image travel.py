import numbers
from sqlite3 import Row
from tkinter import *
from turtle import back
from PIL import  ImageTk,Image
root=Tk()
root.title("image in tkinter")
root.iconbitmap("C:/Users/rames/Downloads/saloni.jpg")
#root.iconphoto("")
root.iconname("ramesh giri")
#root.iconphoto("c:/Users/rames/Downloads/saloni.jpg")
#my_label=Label(root,text="41" + u'\u00b0',font=('ramesh',32)).pack()

button=Button(root,text="quit",command=root.quit)
button.grid(row=2,column=0)
my_image=ImageTk.PhotoImage(Image.open("C:/Users/rames/Downloads/saloni.jpg"))
my_image1=ImageTk.PhotoImage(Image.open("C:/Users/rames/Downloads/didi.jpg.jpeg"))
mylist=[my_image,my_image1]

label1=Label(image=my_image)
label1.grid(row=0,column=0,columnspan=3)
def next(num):
    global label1
    global next
    global back
    label1.grid_forget()
    label1=Label(image=mylist[len(mylist)-1])
    label1.grid(row=1,column=0,columnspan=3)    
    button2=Button(root,text=">>",command=lambda:next[len(mylist)-1])
    button1=Button(root,text="<<",command=lambda:back[len(mylist)+1])
    button1.grid(row=0,column=0)
    button2.grid(row=0,column=1)
    
def back():
    global label1
    global next
    global back
    label1.grid_forget()
    label1=Label(image=mylist[len(mylist)+1])
    label1.grid(row=1,column=0,columnspan=3)

button1=Button(root,text="next",command=lambda:next(2))
button2=Button(root,text='back',command=back)
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
root.mainloop()
