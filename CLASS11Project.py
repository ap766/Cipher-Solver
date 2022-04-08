import tkinter
from tkinter import*
def raise_frame(frame):
    frame.tkraise()
    command=clicked


root=tkinter.Tk()
root.geometry('655x800')
root.title("encrypt decrypt")

root.configure()

Sample=tkinter.Frame(root,width=300,height=400,relief='raised',borderwidth=10,bg="medium orchid")
PageOne=tkinter.Frame(root,width=300,height=400,relief='raised',borderwidth=10,bg="DodgerBlue2")
PageTwo=tkinter.Frame(root,width=300,height=400,relief='raised',borderwidth=10,bg="DeepSkyBlue2")
Help=tkinter.Frame(root,width=300,height=400,relief='raised',borderwidth=10)
About=tkinter.Frame(root,width=300,height=400,relief='raised',borderwidth=10)
PageThree=tkinter.Frame(root,width=300,height=400,relief='raised',borderwidth=10,bg="chartreuse3")
PageFour=tkinter.Frame(root,width=300,height=400,relief='raised',borderwidth=10,bg="yellow2")
PageFive=tkinter.Frame(root,width=300,height=400,relief='raised',borderwidth=10,bg="dark orange")
Final=tkinter.Frame(root,width=300,height=400,relief='raised',borderwidth=10,bg="red")

Final

def close_window():
    root.destroy()#

Home=Frame(root)
for frame in(Home,PageOne,PageTwo,Sample,Help,About,PageThree,PageFour,PageFive,Final):
    frame.grid(row=1,column=0,sticky='new')

#
Label(Home,text='WELCOME TO',font="Broadway 28 bold", bg="blue").pack()
Label(Home,text="CIPHER SOLVER",bg="blue",fg="white",font="Broadway 58 bold").pack()#label game name using pack()
#
button=tkinter.Button(Home,text='PLAY',width='0',height='0',activebackground='red',bg='red',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(Sample)).pack(side="top",fill='both',expand=True,padx=40,pady=40)#

button=tkinter.Button(Home,text='HELP',width='0',height='0',activebackground='red',bg='red',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(Help)).pack(side="top",fill='both',expand=True,padx=40,pady=40)

button=tkinter.Button(Home,text='ABOUT',width='0',height='0',activebackground='red',bg='red',font="Times 23 bold",activeforeground='black',command=lambda:raise_frame(About)).pack(side="top",fill='both',expand=True,padx=40,pady=40)

button=tkinter.Button(Home,text='QUIT',width='0',height='0',activebackground='red',bg='red',font="Times 23 bold",activeforeground='black',command=close_window).pack(side="top",fill='both',expand=True,padx=40,pady=40)#
#
def clicked():
    
    Remove_Buttons(button)
Label(Sample,text="This is A Sample Page",bg='thistle').pack()#
Label(Sample,text="Quesion:   QZUIPO",font="Times 15 bold",bg='thistle').pack()#




Entry(Sample).pack(padx=20,pady=5)#
Label(Sample,text="",bg='medium orchid').pack(padx=20,pady=5)#
Label(Sample,text="Answer is: Python",font="Times 15 bold",bg='thistle').pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="Letters have been shifted 1 place to the right",font='Times 10',bg='thistle').pack()#

Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#

Label(Sample,text='You can now play the Game!!!',font="Times 23 bold",bg='dark violet').pack()#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#
Label(Sample,text="",bg="medium orchid").pack(padx=20,pady=5)#

Button(Sample,text="Go",font="Times 15 bold",activeforeground="seashell2",bg='thistle',command=lambda:raise_frame(PageOne)).pack()#


def clicked():
    Remove_Buttons(button)
    


Label(Help,text="HELP", font="broadway 30 bold").pack()
Label(Help,text='''Welcome to Cipher Solver
This is a fun filled encryption decryption activity to help recall and learn different terms in the programming language-Python.
the rules of the game are as follows:
At the beginning of each level, one hint will be provided to the player on how to decrypt an encrypted word into a suitable term. Player can also select the "Hint" option to help guess the word.
Once the player enters the word correctly, he/she can move onto the next word. However if the guess in incorrect, computer prompts error type to help player amend and retry.
Cipher Solver involves 5 levels starting from an easy 5 lettered word to more difficult levels with an extra letter in each of them.
Good luck!!''').pack()
button=tkinter.Button(Help,text="PLAY",width="0",height='0',activebackground='red',bg='yellow',font="Times 10 bold",activeforeground='black',command=lambda:raise_frame(PageOne)).pack(side="top",fill='both',expand=True,padx=40,pady=40)


def clicked():
    Remove_Buttons(button)

    
Label(About,text="ABOUT", font="broadway 30 bold").pack()
Label(About,text='''Cipher Solver encourages player to think, relate and remember; honing their ,mental abilities and concentration levels.
It provides a challenge and a learning experience for the players to train them to visualise multiple dimensions and possibilities.
It enhances the creativity and curiosity of the player and at the same time relaxes them.
A combination of recreation and education, this games focuses on instilling confidence and a computational thinking in the player.''').pack()
button=tkinter.Button(About,text="PLAY",width="0",height='0',activebackground='red',bg='yellow',font="Times 10 bold",activeforeground='black',command=lambda:raise_frame(PageOne)).pack(side="top",fill='both',expand=True,padx=40,pady=40)
        
count=0    

aa1=tkinter.StringVar()
Label(PageOne,text="Level 1 :Easy Peasy Lemon Squeezy",font="Times 18 bold").pack()
Label(PageOne,text="Some times you have to take a step back to move forward",font="Times 13 bold").pack()
Label(PageOne,text='ques:STOKD ',font="Times 13 ").pack(padx=20,pady=30)


a1=Entry(PageOne,textvariable=aa1).pack(padx=25,pady=30)



def hint1():
    print('Hint:An immutable data type.')
def check1():
 global aa1
 N=aa1.get()

 if N=='TUPLE':
    b1=tkinter.Button(PageOne,text='NEXT',width='10',height='0',command=lambda:raise_frame(PageTwo)).pack(side="top",fill='both',expand=True,padx=60,pady=60)

    print('''correct!!
    TUPLE:They are immutable sequences enclosed within round brackets and separated by commas.
    Did you know?
    They can also be used as keys in dictionaries provided they do not contain and mutable data types.''')
    
    
    def clicked():
        Remove_Buttons(b1)

    def Remove_Buttons(MenuButtonsFrame):
        MenuButtonsFrame.destroy()
    
 else:
    print('incorrect')
    if N=='':
        print("error")
    if len(N)!=5:
        print("check string lenght")
    if N.isalpha()==False:
        print("only alphabets ")
    
h=Button(PageOne,text='hint',font="Times 13 ",command=hint1).pack(padx=25,pady=31)
b=Button(PageOne,text='go',font="Times 15",command=check1).pack(padx=25,pady=31)
B1=tkinter.Button(PageOne,text='QUIT',width='10',height='0',command=close_window).pack(side="top",fill='both',expand=True,padx=60,pady=60)

    
Maa1=tkinter.StringVar()
Label(PageTwo,text="Level 2:Buckle up",font="Times 18 bold").pack()
Label(PageTwo,text="The journey of a thousand miles begins by taking one step forward",font="Times 13 bold").pack()
Label(PageTwo,text='ques:TUSJOH',font="Times 13 ").pack(padx=20,pady=30)
a1=Entry(PageTwo,textvariable=Maa1).pack(padx=25,pady=30)

def hint2():
    print('Hint:Immutable python data type.')
def check2():
 global aa1
 V=Maa1.get()
 if V=='STRING':
    
    print('''correct!!
    STRING:Characters enclosed in quotes (single/double/triple) is called a string. They can be concatenated and replicated with the help of arithematic operators "+" and "*"
    Did you know?
    They are also used as keys in dictionaries.''')
    

    b2=tkinter.Button(PageTwo,text='NEXT',width='10',height='0',command=lambda:raise_frame(PageThree)).pack(side="top",fill='both',expand=True,padx=60,pady=60)

    def clicked():
        Remove_Buttons(b2)

    def Remove_Buttons(MenuButtonsFrame):

        MenuButtonsFrame.destroy()
    
 else:
    print('incorrect')
    if V=='':
        print("error")
    if len(V)!=6:
        print("check string lenght")
    if V.isalpha()==False:
        print("only alphabets ")
    
h=Button(PageTwo,text='hint',command=hint2,font="Times 13 ").pack(padx=25,pady=31)
b=Button(PageTwo,text='go',command=check2,font="Times 15 ").pack(padx=25,pady=31)
B2=tkinter.Button(PageTwo,text='QUIT',width='10',height='0',command=close_window).pack(side="top",fill='both',expand=True,padx=60,pady=60)


kaa1=tkinter.StringVar()
Label(PageThree,text="Level 3: Getting harder - Hang in there",font="Times 18 bold ").pack()
Label(PageThree,text="Sometimes more than taking one step ahead towards growth it is important to take one step back towards safety",font="Times 13 bold").pack()
Label(PageThree,text='ques:KHSDQZL',font="Times 13").pack(padx=20,pady=30)
a1=Entry(PageThree,textvariable=kaa1).pack(padx=25,pady=30)

def hint3():
    print('Hint:Data items with fixed values.')
def check3():
 global aa1
 b=kaa1.get()
 if b=='LITERAL':
    
    print('''correct!!
    LITERAL:Literal is an important token in Python and is often reffered to as constant-Values.
    Did you know?
    Python offers several kinds of literals such as: String, Numeric, Boolean, "None", and Literal Collections.''')
    
    b3=tkinter.Button(PageThree,text='NEXT',width='10',height='0',command=lambda:raise_frame(PageFour)).pack(side="top",fill='both',expand=True,padx=60,pady=60)
    def clicked():
        Remove_Buttons(b3)

    def Remove_Buttons(MenuButtonsFrame):
        MenuButtonsFrame.destroy()
    
 else:
    print('incorrect')
    if b=='':
        print("error")
    if len(b)!=7:
        print("check string lenght")
    if b.isalpha()==False:
        print("only alphabets ")
    
h=Button(PageThree,text='hint',command=hint3,font="Times 13 ").pack(padx=25,pady=31)
b=Button(PageThree,text='go',font="Times 15 ",command=check3).pack(padx=25,pady=31)

B3=tkinter.Button(PageThree,text='QUIT',width='10',height='0',command=close_window).pack(side="top",fill='both',expand=True,padx=60,pady=60)

taa1=tkinter.StringVar()
Label(PageFour,text="Level 4 : Put on your thinking hats",font="Times 18 bold").pack()
Label(PageFour,text="Four steps forward and two steps back is still two steps forward in the right direction",font="Times 13 bold").pack()
Label(PageFour,text='ques:QRGTCVQT',font="Times 13 ").pack(padx=20,pady=30)

a1=Entry(PageFour,textvariable=taa1).pack(padx=25,pady=30)
def hint4():
    print('Hint:Tokens that trigger computation.')
def check4():
 global aa1
 r=taa1.get()
 if r=='OPERATOR':
    
    print('''correct!!
    OPERATORS: Trigger computation when applied to variables and other objects in an expression. They maybe unary ('+'.'-','`','not') or binary (arithematic, bitwise, shift, identity,relational,assignment, logical and membership,
    Did you know?
    Variables and object to which compuatation is applied are known as OPERANDS''')
    
    b4=tkinter.Button(PageFour,text='NEXT',width='10',height='0',command=lambda:raise_frame(PageFive)).pack(side="top",fill='both',expand=True,padx=60,pady=60)
    def clicked():
        Remove_Buttons(b4)

    def Remove_Buttons(MenuButtonsFrame):
        MenuButtonsFrame.destroy()
    
 else:
    print('incorrect')
    if R=='':
        print("error")
    if len(R)!=8:
        print("check string lenght")
    if R.isalpha()==False:
        print("only alphabets ")
    
h=Button(PageFour,text='hint',command=hint4,font="Times 13 ").pack(padx=25,pady=31)
b=Button(PageFour,text='go',command=check4,font="Times 15 ").pack(padx=25,pady=31)
B4=tkinter.Button(PageFour,text='QUIT',width='10',height='0',command=close_window).pack(side="top",fill='both',expand=True,padx=60,pady=60)

    
paa1=tkinter.StringVar()
Label(PageFive,text="Level 5 : Almost there",font="Times 18 bold").pack()
Label(PageFive,text="Even the tiger takes two steps back before he pounces forward",font="Times 13 bold ").pack()
Label(PageFive,text='ques:TYPGYZJCQ',font="Times 13 ").pack(padx=20,pady=30)
a1=Entry(PageFive,textvariable=paa1).pack(padx=25,pady=30)

def hint5():
    print('Hint:Named location referring to a value.')
def check5():
 global aa1
 z=paa1.get()
 if z=='VARIABLES':
    
    print('''correct!!
    VARIABLES:Named labels whose values can be used and processed during during program run.
    Did you know?
    Python allows dynamic typing i.e. a variable pointing to a certain data type can be made to point to a value of different data type.''')
    
    b5=tkinter.Button(PageFive,text='NEXT',width='10',height='0',command=lambda:raise_frame(Final)).pack(side="top",fill='both',expand=True,padx=60,pady=60)
    def clicked():
        Remove_Buttons(b5)

    def Remove_Buttons(MenuButtonsFrame):
        MenuButtonsFrame.destroy()
    
 else:
    print('incorrect')
    if z=='':
        print("error")
    if len(z)!=9:
        print("check string lenght")
    if z.isalpha()==False:
        print("only alphabets ")
    
h=Button(PageFive,text='hint',command=hint5,font="Times 13 ").pack(padx=25,pady=31)
b=Button(PageFive,text='go',command=check5,font="Times 15 ").pack(padx=25,pady=31)

B5=tkinter.Button(PageFive,text='QUIT',width='10',height='0',command=close_window).pack(side="top",fill='both',expand=True,padx=60,pady=60)

Label(Final,text='''Thank you for playing!!
Hope you enjoyed it!!
Keep learning! Keep coding!''',bg='orange').pack()
B6=tkinter.Button(Final,text='QUIT',width='10',height='0',command=close_window).pack(side="top",fill='both',expand=True,padx=60,pady=60)


root.mainloop()


