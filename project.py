import sqlite3
conn = sqlite3.connect('Database2222.db')
c = conn.cursor()


    
#......................................................
from tkinter import*

import time



    
#.................appearance...............................
window = Tk()
window.geometry("800x500")
window.title("ToMaTo")
Tops = Frame(window,bg="white",width = 800,height=50,relief=RAISED)
Tops.pack(side=TOP)

f1 = Frame(window,width = 800,height=450,relief=SUNKEN)
f1.pack(side=LEFT)


localtime=time.asctime(time.localtime(time.time()))

lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Food Option Suggester",fg="dark red",bd=10,anchor='w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="steel blue",anchor=W)
lblinfo.grid(row=1,column=0)


#..................buttons and widgets......................
var1 = IntVar()
def vegnonveg():
    return(var1.get())
    
lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Veg/NonVeg",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=0)

R1 = Radiobutton(f1, font=( 'aria' ,16, ),text="VEG", variable=var1, value=1,command= vegnonveg,
                  anchor= E)
R1.grid(row= 1,column=0,sticky=W)

R2 = Radiobutton(f1, font=( 'aria' ,16, ),text="NON VEG", variable=var1, value=2,command= vegnonveg,
                  anchor = E)
R2.grid(row = 2,column= 0,sticky=W)

#......................................................................
var2 = IntVar()

def type_():
    return(var2.get())

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="TYPE",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=1)

A1 = Radiobutton(f1, font=( 'aria' ,16, ),text="accompaniments", variable=var2, value=1,command= type_,
                  anchor = E)
A1.grid(row = 1,column= 1,sticky=W)

A2 = Radiobutton(f1, font=( 'aria' ,16, ),text="Chinese", variable=var2, value=2,command= type_,
                  anchor = E)
A2.grid(row = 2,column= 1,sticky=W)

A3 = Radiobutton(f1, font=( 'aria' ,16, ),text="North indian", variable=var2, value=3,command= type_,
                  anchor = E)
A3.grid(row = 3,column= 1,sticky=W)

A4 = Radiobutton(f1, font=( 'aria' ,16, ),text="south indian", variable=var2, value=4,command= type_,
                  anchor = E)
A4.grid(row = 4,column= 1,sticky=W)


#.........................................................................
min_cost = [0,50,100,150,200,250,300,350]
max_cost = [50,100,150,200,250,300,350,400]

def min_value1():
    return (S1.get())

def max_value1():
    print(S2.get())
    return (S2.get())

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="MIN COST",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=2)

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="MAX COST",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=2,column=2)

S1 = Spinbox(f1,from_= min_cost[0],to = min_cost[7],increment = 50,font=( 'aria' ,16, ),state="readonly")
S1.grid(row = 1,column = 2,sticky = W)

S2 = Spinbox(f1,from_ = max_cost[0],to = max_cost[7],increment = 50,font=( 'aria' ,16, ),state="readonly")
S2.grid(row = 3,column = 2,sticky = W)



#....................................................................................
var4 =IntVar()
def hmh():
    return(var4.get())


lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="How Much Hungry?",fg="steel blue",bd=10,anchor='w')
lblreference.grid(row=0,column=3)

H1 = Radiobutton(f1, font=( 'aria' ,16, ),text="Not Much", variable=var4, value=1,command= hmh,
                  anchor= E)
H1.grid(row= 1,column=3,sticky=W)

H2 = Radiobutton(f1, font=( 'aria' ,16, ),text="Very Much", variable=var4, value=3,command= hmh,
                  anchor= E)
H2.grid(row= 2,column=3,sticky=W)

H3 = Radiobutton(f1, font=( 'aria' ,16, ),text="Moderate", variable=var4, value=2,command= hmh,
                  anchor= E)
H3.grid(row= 3,column=3,sticky=W)



    

#..................................................................................

def  algorithm(vnv2,type2,hmh2,a2,b2):


    listofresult =[]
    i=0
    c.execute("SELECT * FROM Database2222 WHERE hmh = ? AND vnv = ? AND type = ? AND cost BETWEEN ? AND ?",(hmh2,vnv2,type2,a2,b2))
 
        
    for row  in c.fetchall():
        i=i+1
        listofresult.insert(i,row[0])
        
    
        


    return listofresult

#.....................................................................................
def result():
    vnv1 = vegnonveg()
    type1=type_()
    hmh1 = hmh()
    a=min_value1()
   
    b=max_value1()

    list_ = algorithm(vnv1,type1,hmh1,a,b)
    window(list_)

def window(list_1):
    
    window2 = Tk()
    window2.geometry("400x400")
    window2.title("enjoy your food")
    lblreference = Label(window2, font=( 'aria' ,16, 'bold' ),text="You can order this!",fg="steel blue",bd=10,anchor='w')
    lblreference.pack()
    L2 = Listbox(window2)
    L2.config(font =( 'aria' ,16, 'bold' ))
    for i in list_1:
          L2.insert(END,i)
    L2.pack()
    
    



B1 = Button(f1,font=( 'aria' ,16, 'bold' ),text="SEARCH",fg="steel blue",bd=10,anchor='w',command=result)
B1.grid(row = 6,column = 2,sticky = W)
