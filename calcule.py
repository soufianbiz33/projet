from tkinter import *
gui=Tk()
gui.title(" first calculator ")
gui.geometry("280x250")


expression=""

def press(userinput):
   global expression
   expression= expression+str(userinput)
   equation.set(expression)
   
def equal():
 try:
    global expression
    result=str(eval(expression))
    equation.set(result)
    expression=""
 except:
    equation.set("Error :Try again")
    expression=""
def clear():
    global expression
    expression=""
    equation.set("")
    


titlelabel=Label(gui,text="calculator",fg="black",font=("Century 20 bold"))
titlelabel.grid(columnspan=4,pady=8,padx=5,ipadx=70)

equation=StringVar()


expressionField=Entry(gui,textvariable=equation,bg="black",fg="white")
expressionField.grid(columnspan=4,ipady=5,ipadx=30,pady=10)


btn1=Button(gui,text="1",width=7,height=1,bg="blue",fg="white",command=lambda:press(1))
btn1.grid(row=2,column=0)

btn2=Button(gui,text="2",width=7,height=1,bg="blue",fg="white",command=lambda:press(2))
btn2.grid(row=2,column=1)

btn3=Button(gui,text="3",width=7,height=1,bg="blue",fg="white",command=lambda:press(3))
btn3.grid(row=2,column=2)

btn4=Button(gui,text="4",width=7,height=1,bg="blue",fg="white",command=lambda:press(4))
btn4.grid(row=3,column=0)

btn5=Button(gui,text="5",width=7,height=1,bg="blue",fg="white",command=lambda:press(5))
btn5.grid(row=3,column=1)

btn6=Button(gui,text="6",width=7,height=1,bg="blue",fg="white",command=lambda:press(6))
btn6.grid(row=3,column=2)

btn7=Button(gui,text="7",width=7,height=1,bg="blue",fg="white",command=lambda:press(7))
btn7.grid(row=4,column=0)

btn8=Button(gui,text="8",width=7,height=1,bg="blue",fg="white",command=lambda:press(8))
btn8.grid(row=4,column=1)

btn9=Button(gui,text="9",width=7,height=1,bg="blue",fg="white",command=lambda:press(9))
btn9.grid(row=4,column=2)

btn0=Button(gui,text="0",width=7,height=1,bg="blue",fg="white",command=lambda:press(0))
btn0.grid(row=5,column=0)

dotbtn=Button(gui,text=".",width=7,height=1,bg="gray",fg="black",command=lambda:press("."))
dotbtn.grid(row=5,column=1)

eqbtn=Button(gui,text="=",width=7,height=1,bg="gray",fg="black",command=equal)
eqbtn.grid(row=5,column=2)

plusbtn=Button(gui,text="+",width=7,height=1,bg="orange",fg="white",command=lambda:press("+"))
plusbtn.grid(row=2,column=3)

minusbtn=Button(gui,text="-",width=7,height=1,bg="orange",fg="white",command=lambda:press("-"))
minusbtn.grid(row=3,column=3)

mulbtn=Button(gui,text="*",width=7,height=1,bg="orange",fg="white",command=lambda:press("*"))
mulbtn.grid(row=4,column=3)

divbtn=Button(gui,text="/",width=7,height=1,bg="orange",fg="white",command=lambda:press("/"))
divbtn.grid(row=5,column=3)

clearbtn=Button(gui,text="C",width=7,height=1,bg="black",fg="white",command=clear)
clearbtn.grid(row=6,column=0)


gui.mainloop()