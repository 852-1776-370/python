from tkinter import *
ramesh_root=Tk()
ramesh_root.geometry("755x700")
ramesh_root.title("ramesh giri wellcome")
e=Entry(ramesh_root,borderwidth=10)
e.grid(row=1,column=1)
button=Button(ramesh_root,text="quit",command=ramesh_root.quit)
button.grid(row=0,column=1)
title_label=Label(text=" Ramesh giri   ",bg="pink",fg="blue",padx=10,pady=5,font="comicsanms,20,bold",borderwidth=10,relief=SUNKEN)
title_label.grid(row=0,column=0)
ramesh_root.mainloop()