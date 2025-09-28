from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry('300x350+800+400')
win.title('login')
win.configure(background="#E7B7F1")


def login():
    user=user_entry.get()
    password=psw_entry.get()

    if user == 'admin'and password=='1234':
        win.withdraw()

        new_win=Toplevel(win)
        new_win.title('info')
        new_win.geometry('150x150')
        new_win.configure(background="#E7B7F1")

        lbl_welcome=Label(new_win,text='Welcome to system',font='calibri 11',foreground='black',background="#EEC4F6")
        lbl_welcome.place(x=15,y=30)

        def back_to_login (nw=new_win):
            nw.destroy()
            win.deiconify()

        btn_ok=Button(new_win,text='OK',font='calibri 8',foreground='black',background="#E7B7F1",command=back_to_login)
        btn_ok.place(x=70,y=100)

    else:
        messagebox.showerror('Erorr','Enter again')
        
Label(win,text='user :',font='calibri 13',foreground='black',background="#EEC4F6").place(x=20,y=20)
Label(win,text='password :',font='calibri 13',foreground='black',background="#EEC4F6").place(x=20,y=65)

user_entry=Entry(win,width=36)
user_entry.place(x=70,y=24)

psw_entry=Entry(win,width=30,show='*')
psw_entry.place(x=106,y=70)

btn_login=Button(win,text='login',font='calibra 10',command=login,foreground='black',background="#EEC4F6")
btn_login.place(x=140,y=260)


win.mainloop()
