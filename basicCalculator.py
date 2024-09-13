import customtkinter 




Calculator = customtkinter.CTk()
Calculator.title("Calculator")
Calculator.geometry("370x600")
# Calculator.resizable(height=False,width=False)

Calculator.columnconfigure(0,weight=1)
Calculator.resizable(False,False)


#row 1
f2 = ("Arial Black",15)
f1 = ("Cascadia Code",20)
exp = ""
expLabel = customtkinter.CTkLabel(Calculator,text= exp
                                  ,font=("Arial Black",40),anchor="ne",compound="right",text_color="white")
expLabel.grid(row=0,column=0,padx=30,pady=15,sticky="we")


ansLabel = customtkinter.CTkLabel(Calculator,text=""
                                  ,font=("Cascadia Code",30),anchor="ne",compound="right",text_color="#dab6b1")
ansLabel.grid(row=1,column=0,padx=30,pady=15,sticky="we")

h = 70
p3=(10,0)


app = customtkinter.CTkFrame(Calculator)
app.grid(row=2,column=0,padx=20,pady=20)



def ACFuc():
    global exp
    exp = ""
    ansLabel.configure(text='')     
    expLabel.configure(text='') 

 


operator = ['+','-','/','*']


def setChar(char):
    global exp
    if exp=='' or not (exp[-1] in operator and char in operator) :
        exp = exp + char
        reExp = replacedStr(exp)
        expLabel.configure(text=reExp,font=("Arial Black",40),text_color="white")
        if char.isdigit():
            total = eval(exp)
            ansLabel.configure(text=total,font=("Cascadia Code",30),text_color="#dab6b1")

def replacedStr(str):
    str = str.replace('*','×')
    str = str.replace('/','÷')
    return str


def del_call():
    global exp
    exp = exp[:-1]
    reExp = replacedStr(exp)
    expLabel.configure(text=reExp)
    if exp=='':
        ansLabel.configure(text='')
    elif exp[-1] not in operator:
        total = eval(exp)
        ansLabel.configure(text=total)
    else:
        total = eval(exp[:-1])
        ansLabel.configure(text=total)


def equal_call():
    ansLabel.configure(font=("Arial Black",40),text_color="white")
    expLabel.configure(font=("Cascadia Code",30),text_color="#dab6b1")



Acbtn = customtkinter.CTkButton(app,text="Ac",width=150,height=h,font=f1,fg_color="#E3651D",command=ACFuc)
Acbtn.grid(row=2,column=0,padx=p3,pady=p3,columnspan=2)
delbtn = customtkinter.CTkButton(app,text="Del",width=150,height=h,font=f1,fg_color="#7077A1",command=del_call)
delbtn.grid(row=2,column=2,padx=(10,10),pady=p3,columnspan=2)





p4 = (10,0)
btn1 = customtkinter.CTkButton(app,text="1",width=h,height=h,font=f1,command=lambda:setChar("1"))
btn1.grid(row=3,column=0,padx=p4,pady=p4)
btn2 = customtkinter.CTkButton(app,text="2",width=h,height=h,font=f1,command=lambda:setChar("2"))
btn2.grid(row=3,column=1,padx=p4,pady=p4)
btn3 = customtkinter.CTkButton(app,text="3",width=h,height=h,font=f1,command=lambda:setChar("3"))
btn3.grid(row=3,column=2,padx=p4,pady=p4)
plusbtn = customtkinter.CTkButton(app,text="+",width=h,height=h,font=f1,command=lambda:setChar("+"),fg_color="#B0A4A4",text_color="#000000")
plusbtn.grid(row=3,column=3,padx=(10,10),pady=p4)

p5 = (10,0)
btn4 = customtkinter.CTkButton(app,text="4",width=h,height=h,font=f1,command=lambda:setChar("4"))
btn4.grid(row=4,column=0,padx=p5,pady=p5)
btn5 = customtkinter.CTkButton(app,text="5",width=h,height=h,font=f1,command=lambda:setChar("5"))
btn5.grid(row=4,column=1,padx=p5,pady=p5)
btn6 = customtkinter.CTkButton(app,text="6",width=h,height=h,font=f1,command=lambda:setChar("6"))
btn6.grid(row=4,column=2,padx=p5,pady=p5)
minusbtn = customtkinter.CTkButton(app,text="-",width=h,height=h,font=f1,command=lambda:setChar("-"),fg_color="#B0A4A4",text_color="#000000")
minusbtn.grid(row=4,column=3,padx=(10,10),pady=p5)

p6 = (10,0)
btn7 = customtkinter.CTkButton(app,text="7",width=h,height=h,font=f1,command=lambda:setChar("7"))
btn7.grid(row=5,column=0,padx=p6,pady=p6)
btn8 = customtkinter.CTkButton(app,text="8",width=h,height=h,font=f1,command=lambda:setChar("8"))
btn8.grid(row=5,column=1,padx=p6,pady=p6)
btn9 = customtkinter.CTkButton(app,text="9",width=h,height=h,font=f1,command=lambda:setChar("9"))
btn9.grid(row=5,column=2,padx=p6,pady=p6)
mulbtn = customtkinter.CTkButton(app,text="x",width=h,height=h,command=lambda:setChar("*"),font=f1,fg_color="#B0A4A4",text_color="#000000")
mulbtn.grid(row=5,column=3,padx=(10,10),pady=p6)

p7=(10,0)
eqbtnbtn = customtkinter.CTkButton(app,text="=",width=h,height=h,font=f1,fg_color="#6B728E",command=equal_call)
eqbtnbtn.grid(row=6,column=0,padx=p7,pady=(10,10))
btn0 = customtkinter.CTkButton(app,text="0",width=h,height=h,font=f1,command=lambda:setChar("0"))
btn0.grid(row=6,column=1,padx=p7,pady=(10,10))
btndot = customtkinter.CTkButton(app,text=".",width=h,height=h,command=lambda:setChar("."),font=f1,fg_color="#6B728E")
btndot.grid(row=6,column=2,padx=p7,pady=(10,10))
divbtn = customtkinter.CTkButton(app,text="÷",width=h,command=lambda:setChar("/"),height=h,font=f1,fg_color="#B0A4A4",text_color="#000000")
divbtn.grid(row=6,column=3,padx=(10,10),pady=(10,10))


Calculator.mainloop()