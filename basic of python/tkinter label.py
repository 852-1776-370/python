from tkinter import *
import tkinter as tk
root=Tk()
root.title("hello  ramesh")
santosh=Label(text="hello  avinav")
santosh.pack(padx=20,pady=20)
ramesh=Label(text="hello ramesh")
ramesh.pack(padx=20,pady=20)
rohit=Button(root,text="say hello rohit",command= root.destroy)
rohit.pack(padx=21,pady=22)
root.mainloop()
