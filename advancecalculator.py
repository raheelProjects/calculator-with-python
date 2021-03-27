from tkinter import *
from PIL import ImageTk,Image
window = Tk()
window.configure(bg="yellow")
window.title('calculator')
#input pictures
no1=ImageTk.PhotoImage(Image.open('1.png'))
no2=ImageTk.PhotoImage(Image.open('2.png'))
no3=ImageTk.PhotoImage(Image.open('3.png'))
no4=ImageTk.PhotoImage(Image.open('4.png'))
no5=ImageTk.PhotoImage(Image.open('5.png'))
no6=ImageTk.PhotoImage(Image.open('6.png'))
no7=ImageTk.PhotoImage(Image.open('7.png'))
no8=ImageTk.PhotoImage(Image.open('8.png'))
no9=ImageTk.PhotoImage(Image.open('9.png'))
no0=ImageTk.PhotoImage(Image.open('0.png'))
clear=ImageTk.PhotoImage(Image.open('clear.png'))
#box
box=Entry(window,width=30,borderwidth=5)
box.grid(row=0,column=0,padx=5,pady=5,columnspan=4)
#functions
def enter_number(number):
    curent_number=box.get()
    box.delete(0,END)
    box.insert(0,str(curent_number)+str(number))
def cleared():
    box.delete(0,END)
def jamas():
    first_number=box.get()
    global num
    global working
    working = 'addition'
    num=int(first_number)
    box.delete(0,END)
def multiply():
    first_number=box.get()
    global num
    global working
    working = 'multiply'
    num=int(first_number)
    box.delete(0,END)
def divide():
    first_number=box.get()
    global num
    global working
    working = 'divide'
    num=int(first_number)
    box.delete(0,END)

def subtract():
    first_number=box.get()
    global num
    global working
    working = 'subtraction'
    num=int(first_number)
    box.delete(0,END)
def equal():
    boom=box.get()
    box.delete(0,END)
    Sum = int(boom)
    if working =='addition':
        bro =Sum+num
    elif working == 'subtraction':
        bro =num-Sum
    elif working == 'multiply':
        bro =Sum*num
    elif working == 'divide':
        bro =Sum/num
    box.insert(0,bro)
# buttons
b9=Button(image=no9,command=lambda:enter_number('9'))
b9.grid(row=1,column=0,columnspan=1)
b8=Button(image=no8,command=lambda:enter_number('8'))
b8.grid(row=1,column=1,columnspan=1)
b7=Button(image=no7,command=lambda:enter_number('7'))
b7.grid(row=1,column=2,columnspan=1)
b6=Button(image=no6,command=lambda:enter_number('6'))
b6.grid(row=2,column=0,columnspan=1)
b5=Button(image=no5,command=lambda:enter_number('5'))
b5.grid(row=2,column=1,columnspan=1)
b4=Button(image=no4,command=lambda:enter_number('4'))
b4.grid(row=2,column=2,columnspan=1)
b3=Button(image=no3,command=lambda:enter_number('3'))
b3.grid(row=3,column=0,columnspan=1)
b2=Button(image=no2,command=lambda:enter_number('2'))
b2.grid(row=3,column=1,columnspan=1)
b1=Button(image=no1,command=lambda:enter_number('1'))
b1.grid(row=3,column=2,columnspan=1)
b0=Button(image=no0,command=lambda:enter_number('0'))
b0.grid(row=4,column=0,columnspan=1)
#clear button
clear_button=Button(image=clear,padx=70,command=cleared)
clear_button.grid(row=6,column=1,columnspan=1)
#equal and add button
buttonadd=Button(window,text='+',padx=30,bd=2,pady=20,command=jamas)
buttonequal=Button(window,text='=',padx=30,pady=20,bd=2,command=equal)
#subtract and multiply and divide button
buttonmultiply=Button(window,text='x',padx=30,pady=20,bd=2,command=multiply)
buttondivide=Button(window,text='/',padx=30,pady=20,bd=2,command=divide)
buttonsubtract=Button(window,text='-',padx=30,pady=20,bd=2,command=subtract)
#griding them
buttonmultiply.grid(row=5,column=0)
buttondivide.grid(row=5,column=1)
buttonsubtract.grid(row=5,column=2)
buttonequal.grid(row=4,column=1)
buttonadd.grid(row=4,column=2)
window.mainloop()