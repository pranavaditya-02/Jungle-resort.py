import tkinter
import mysql.connector
from tkinter import messagebox
from tkinter import Spinbox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
win=tkinter.Tk()
h=win.winfo_screenheight()
w=win.winfo_screenwidth()
win.configure(height=h,width=w,bg='#4F92BD')
win.title('RESORT BOOKING')
mailformat = ('@gmail.com' , '@yahoo.com' , "@outlook.com")

def show():
    a=txt1.get()
    b=cal1.get()
    c=variable3.get()
    d=txt4.get()
    e=txt5.get()
    f=txt6.get()
    g=txt7.get()
    h=days.get()
    i=cal2.get()
    j=txt8.get()
    k=variable11.get()
    l=persons.get()
    m=adults.get()
    n=kids.get()
    if a!='' and b!='' and c!='' and d!='' and e!='' and f!='' and g!='' and h!='' and i!='' and k!='' and l!='' and m!='' and n!='':
        if a.isalpha():
            if d.isnumeric:
                if e.endswith(mailformat):
                    if f.isalpha():
                        if g.isalpha():
                            if h.isnumeric:
                                if l.isnumeric:
                                    if m.isnumeric:
                                        if n.isnumeric:
                                            if len(d)==10:
                                                con=mysql.connector.connect(user='root',password='',host='localhost',database='jungle_resort')
                                                cur=con.cursor()
                                                cur.execute("insert into jungle_resort values('%s','%s','%s',%s,'%s','%s',%s,'%s','%s','%s',%s,%s)"
                                                %(a,b,c,d,e,g,h,i,j,k,m,n))
                                                con.commit()
                                                messagebox.showinfo('Submit Message','Booking Successful')
                                                txt1.delete(0,'end')
                                                cal1.delete(0,'end')
                                                txt4.delete(0,'end')
                                                txt5.delete(0,'end')
                                                txt6.delete(0,'end')
                                                txt7.delete(0,'end')
                                                txt8.delete(0,'end')
                                                cal2.delete(0,'end')
                                                days.delete(0,'end')
                                                persons.delete(0,'end')
                                                adults.delete(0,'end')
                                                kids.delete(0,'end')
                                                variable3.set('Choose any option....')
                                                variable11.set('Choose any option....')
                                            else:
                                                messagebox.showerror('Alert Message','Phone number must have 10 digits')
                                        else:
                                            messagebox.showerror('Alert Message','No.of kids must be in numbers')
                                    else:
                                        messagebox.showerror('Alert Message','No.of adults must be in numbers')
                                else:
                                    messagebox.showerror('Alert Message','Total no. of persons must be in numbers')
                            else:
                                messagebox.showerror('Alert Message','No of days must be in numbers')
                        else:
                            messagebox.showerror('Alert Message','country\state must be in alphabets')
                    else:
                        messagebox.showerror('Alert Message','Family name must be in alphabets')
                else:
                    messagebox.showerror('Alert Message','Enter a valid mail id')
            else:
                messagebox.showwarning('Alert Message','Ph.no must be in numbers')
        else:
            messagebox.showerror('Alert Message','Customer name must be in alphabets')
    else:
        messagebox.showwarning('Warning', 'Fields are empty')         
                    
                                    
#label
lbl1=tkinter.Label(win,text='CUSTOMER NAME',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl2=tkinter.Label(win,text='DATE OF BIRTH',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl3=tkinter.Label(win,text='GENDER',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl4=tkinter.Label(win,text='MOBILE NUMBER',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl5=tkinter.Label(win,text='EMAIL ID',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl6=tkinter.Label(win,text='FAMILY NAME',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl7=tkinter.Label(win,text='COUNTRY/STATE',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl8=tkinter.Label(win,text='NO OF DAYS',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl9=tkinter.Label(win,text='DATE OF ARRAIVAL',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl10=tkinter.Label(win,text='TIME OF ARRAIVAL',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl11=tkinter.Label(win,text='FOOD PREFERANCE',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl12=tkinter.Label(win,text='NO OF PERSON',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl13=tkinter.Label(win,text='NO OF ADULTS',font=('arailblack',20,'bold'),bg='gray',fg='white')
lbl14=tkinter.Label(win,text='NO OF KIDS',font=('arailblack',20,'bold'),bg='gray',fg='white')

lbl1.place(x=100,y=150)
lbl2.place(x=100,y=200)
lbl3.place(x=100,y=250)
lbl4.place(x=100,y=300)
lbl5.place(x=100,y=350)
lbl6.place(x=100,y=400)
lbl7.place(x=100,y=450)
lbl8.place(x=800,y=150)
lbl9.place(x=800,y=200)
lbl10.place(x=800,y=250)
lbl11.place(x=800,y=300)
lbl12.place(x=800,y=350)
lbl13.place(x=800,y=400)
lbl14.place(x=800,y=450)

#text

txt1=tkinter.Entry(win,font=('arailblack',15,'bold'),relief='sunken',bd=5)
txt4=tkinter.Entry(win,font=('arailblack',15,'bold'),relief='sunken',bd=5)
txt5=tkinter.Entry(win,font=('arailblack',15,'bold'),relief='sunken',bd=5)
txt6=tkinter.Entry(win,font=('arailblack',15,'bold'),relief='sunken',bd=5)
txt7=tkinter.Entry(win,font=('arailblack',15,'bold'),relief='sunken',bd=5)
txt8=tkinter.Entry(win,font=('arailblack',15,'bold'),relief='sunken',bd=5)

txt1.place(x=400,y=150)
txt4.place(x=400,y=300)
txt5.place(x=400,y=350)
txt6.place(x=400,y=400)
txt7.place(x=400,y=450)
txt8.place(x=1100,y=250)

#combo boxes
variable3 =tkinter.StringVar(win)
variable3.set("Choose any option....")# default value
wi3 = tkinter.OptionMenu(win, variable3,"MALE","FEMALE")
wi3.place(x=400,y=250)

variable11 =tkinter.StringVar(win)
variable11.set("Choose any option....")# default value
wi11 = tkinter.OptionMenu(win, variable11,"VEG","NON-VEG")
wi11.place(x=1100,y=300)

#spin boxes
days=Spinbox(win,from_=0,to=50,increment=1,font=('arailblack',15,'bold'))
days.place(x=1100,y=150)

persons=Spinbox(win,from_=0,to=50,increment=1,font=('arailblack',15,'bold'))
persons.place(x=1100,y=350)

adults=Spinbox(win,from_=0,to=50,increment=1,font=('arailblack',15,'bold'))
adults.place(x=1100,y=400)

kids=Spinbox(win,from_=0,to=50,increment=1,font=('arailblack',15,'bold'))
kids.place(x=1100,y=450)

#calendar
cal1 =DateEntry(win,font=('arail black (Body)',15), bg= "#5cc4ed", fg= "black",)
cal1.place(x=400,y=200)

cal2 =DateEntry(win,font=('arail black (Body)',15), bg= "#5cc4ed", fg= "black",)
cal2.place(x=1100,y=200)

def reset():
    txt1.delete(0,'end')
    cal1.delete(0,'end')
    txt4.delete(0,'end')
    txt5.delete(0,'end')
    txt6.delete(0,'end')
    txt7.delete(0,'end')
    txt8.delete(0,'end')
    cal2.delete(0,'end')
    days.delete(0,'end')
    persons.delete(0,'end')
    adults.delete(0,'end')
    kids.delete(0,'end')
    variable3.set('Choose any option....')
    variable11.set('Choose any option....')
    messagebox.showinfo('Clear' , 'Cleared sucessfully')

#button    
but1=tkinter.Button(win,text='clear',font=('#5cc4ed',18,'bold'),
                    width=20,bg='red',command=reset)
but1.place(x=800,y=600)

but1=tkinter.Button(win,text='Submit',font=('arailblack',18,'bold'),width=20,bg='green',command=show)
but1.place(x=400,y=600)
#label

lbl15=tkinter.Label(win,text='HOTEL JUNGLE RESORT',font=('Lucida Calligraphy',30,'bold'),bg='#4F92BD',fg='gold')
lbl15.place(x=500,y=50)

win.mainloop()


