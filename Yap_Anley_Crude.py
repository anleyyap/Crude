from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox
import tkinter as tk

students = []

def update6():
    aa['state'] = DISABLED
    bb['state'] = NORMAL
    cc['state'] = DISABLED
    dd.insert(0,emp.getFirstname())
    ee.insert(0,emp.getLastname())
    ff.insert(0,emp.getCourse())
    gg.insert(0,emp.getSection())
    hh.insert(0,emp.getContact())
def update7():
    aa['state'] = NORMAL
    bb['state'] = DISABLED
    MsgBox = messagebox.askquestion ('Update ','Are you sure you want to Update?',icon = 'warning')
    if MsgBox == 'yes':
        selected_item = tv.selection()[0]
        tv.item(selected_item, text=dd.get(),values=(ee.get(),self_gender.get(),ff.get(),gg.get(),hh.get()))
        dd.delete(0, END)
        ee.delete(0, END)
        ff.delete(0, END)
        gg.delete(0, END)
        hh.delete(0, END) 
    else:
        print("returning...")       
def add_to_list():
    global emp   
    print("Name: " + " " + dd.get(), ee.get() + "  " + "Gender: " + " " + self_gender.get()+ "  " +"Course: " + " " + ff.get()+ "  " +"Section: " + " " + gg.get()+ "  " + "Contact: " + " " + hh.get())
    emp = Student(dd.get(), ee.get(),self_gender.get(),ff.get(),gg.get(),hh.get())
    a = dd.get()
    b = ee.get()
    c = self_gender.get()
    d = ff.get()
    e = gg.get()
    f = hh.get()
    students.append(Student(a,b,c,d,e,f))
    students.append(emp)
    messagebox.showinfo("Add", "Successful")
    dd.delete(0, END)
    ee.delete(0, END)
    ff.delete(0, END)
    gg.delete(0, END)
    hh.delete(0, END)
    cc['state'] = NORMAL  
def show_list():
    tv.insert('','end', text=emp.getName(),values=(emp.getGender(),emp.getCourse(), emp.getSection(), emp.getContact()))
    root.i = root.i + 1
    cc['state'] = DISABLED
def exit_prog():
    MsgBox = messagebox.askquestion ('Exit','Are you sure you want to Exit?',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()
    else:
        print("Welcome!")    
def delete_to_list():
        MsgBox = messagebox.askquestion ('Delete','Are you sure you want to Delete?',icon = 'warning')
        if MsgBox == 'yes':
            selected_item = tv.selection()
            remove_emp = tv.detach(selected_item)
            dd.delete(0, END)
            ee.delete(0, END)
            ff.delete(0, END)
            gg.delete(0, END)
            hh.delete(0, END)
        else:
            messagebox.showinfo('Return','You will now return to the Main Screen')  
class Student:
    def __init__(self, first_name, last_name, gender, course, section, contact):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.course = course
        self.section = section
        self.contact = contact        
    def getName(self):
        return self.first_name + " " + self.last_name
    def getGender(self):
        self_gender.get()
        return self.gender
    def getCourse(self):
        return self.course
    def getSection(self):
        return self.section
    def getFirstname(self):
        return self.first_name
    def getLastname(self):
        return self.last_name
    def getContact(self):
        return self.contact
    
root = tk.Tk()
root.resizable(0, 0)
root.i = 0
self_gender = StringVar()
root.configure(background='#e2d0bc') 
root.title("Student Registration System")
Label(root, text="First name: ", bg="#e2d0bc").grid(row=2, column=0, padx=10, pady=5)
dd = Entry(root, width=30)
dd.grid(row=2, column=1, padx=10, pady=5)
Label(root, text="Last name: ", bg="#e2d0bc").grid(row=3, column=0, padx=10, pady=5)
ee = Entry(root, width=30)
ee.grid(row=3, column=1, padx=10, pady=5)
Label(root, text="Course: ", bg="#e2d0bc").grid(row=5, column=0, padx=10, pady=5)
ff = Entry(root, width=30)
ff.grid(row=5, column=1, padx=10, pady=5)
Label(root, text="Gender: ", bg="#e2d0bc").grid(row=2, column=2, padx=10, pady=5)
r1 = Radiobutton(root, text="Male", value = "Male", variable=self_gender, bg="#e2d0bc").grid(row = 2, column=2, padx=10, pady=5,columnspan=2)
r2 = Radiobutton(root, text="Female", value = "Female",variable=self_gender, bg="#e2d0bc").grid(row= 2, column=2, padx=10, pady=5,columnspan=3)
Label(root, text="Section: ", bg="#e2d0bc").grid(row=3, column=2, padx=10, pady=5)
gg = Entry(root, width=30)
gg.grid(row=3, column=3, padx=10, pady=5)
Label(root, text="Contact #: ", bg="#e2d0bc").grid(row=5, column=2, padx=10, pady=5)
hh = Entry(root, width=30)
hh.grid(row=5, column=3, padx=10, pady=5)
z1 = Button(root, text="        Add        ", bg="#e2d0bc", command=add_to_list, fg="blue", padx=10, pady=5)
z1.grid(row=8, column=0, padx=10, pady=5)
cc = Button(root, text="       Show       ", bg="#e2d0bc", command=show_list, fg="blue", padx=10, pady=5)
cc.grid(row=8, column=1, padx=10, pady=5)
aa = Button(root, text="     Update     ",state=NORMAL, bg="#e2d0bc", command=update6, fg="blue", padx=10, pady=5)
aa.grid(row=8, column=2, padx=10, pady=5)
z2 = Button(root, text="      Delete      ", bg="#e2d0bc", command=delete_to_list, fg="blue", padx=10, pady=5)
z2.grid(row=8, column=3, padx=10, pady=5)
z3 = Button(root, text="        Exit         ", bg="#e2d0bc", command=exit_prog, fg="red", padx=10, pady=5)
z3.grid(row=0, column=4, padx=10, pady=5, columnspan=5)
bb = Button(root, text="     Update     ",state=DISABLED, bg="#e2d0bc", command=update7, fg="blue", padx=10, pady=5)
bb.grid(row=0, column=3 ,padx=10, pady=5, columnspan=5)
pp = Button(root, text="          Student Registration Form          ", bg="#e2d0bc", fg="blue", padx=10, pady=5)
pp.grid(row=0, column=0 ,padx=10, pady=5)
tv = ttk.Treeview(root, height=15,columns=('gender','Course','Section','contact'))
tv.grid(row=1, column=0 , columnspan=5)
tv.heading('#0', text="Name",anchor=W)
tv.heading('#1', text="Gender",anchor=W)
tv.heading('#2', text="Course",anchor=W)
tv.heading('#3', text="Section",anchor=W)
tv.heading('#4', text="Contact",anchor=W)
root.mainloop()
