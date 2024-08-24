from tkinter import *
top=Tk()
top.geometry("1400x800")
top.title("WOW")
top.config(bg="grey")
welcome=Label(top,text="WELCOME",font=("TimesNewRoman",25,"bold"),bg="white")
welcome.place(x=700,y=20)
def login():
    art=Frame(top,bg="pink",height=700,width=400)
    art.pack(fill=X)
    student=Label(art,text="STUDENTS",font=("TimesNewRoman",25,"bold"),bg="white")
    student.place(x=700,y=20)
    box1=Entry(art,text="",font=("TimesNewRoman",25,"bold"),fg="black")
    box1.place(x=550,y=100)
   
welcome=Label(top,text="NAME",font=("TimesNewRoman",25,"bold"),bg="white")
welcome.place(x=200,y=100)
hi=Label(top,text="DEPARTMENT",font=("TimesNewRoman",25,"bold"),bg="white")
hi.place(x=200,y=200)
hello=Label(top,text="REGISTER NO",font=("TimesNewRoman",25,"bold"),bg="white")
hello.place(x=200,y=300)
box=Entry(top,text="",font=("TimesNewRoman",25,"bold"),fg="black")
box.place(x=700,y=100)
bax=Entry(top,text="",font=("TimesNewRoman",25,"bold"),fg="black")
bax.place(x=700,y=200)
bex=Entry(top,text="",font=("TimesNewRoman",25,"bold"),fg="black")
bex.place(x=700,y=300)
BUTTON=Button(top,text="SUBMIT",font=("TimesNewRoman",25,"bold"),bg="black",fg="white",activebackground="green",activeforeground="red",command=login)
BUTTON.place(x=700,y=500)



