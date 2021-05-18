from tkinter import *

window = Tk()

def save_fun():
    messagebox.showinfo('Result','Your info has been successfully stored.')

csvReadName_lbl = Label(window,text = 'Enter the csv name you want to read from ===>').grid(row = 0,column = 0,padx = 10,pady = 10)
csvReadName_ent = Entry(window)
csvWriteName_lbl = Label(window,text = 'Enter the csv name you want to write in ===>').grid(row = 1,column = 0,padx = 10,pady = 10)
csvWriteName_ent = Entry(window)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = save_fun).grid(row = 2,column = 0,padx = 10,pady = 10)

csvReadName_ent.grid(row = 0,column = 1,padx = 10,pady = 10)
csvWriteName_ent.grid(row = 1,column = 1,padx = 10,pady = 10)

window.mainloop()