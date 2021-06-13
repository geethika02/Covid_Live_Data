from covid import Covid
from tkinter import *
import tkinter.messagebox

win = Tk()
win.title("Covid Data")
win.attributes('-fullscreen',True)
win.config(background="#c8bfe7")

obj = Covid(source="worldometers")


def error():
    tkinter.messagebox.showerror("Invalid Country Name","There is no country called '"+country.get()+"'\nPlease enter a valid Country name")
def empty():
    tkinter.messagebox.showwarning("Warning","Entry field cannot be empty\nPlease enter a Country name")

def worldwide():
    active1.config(text=obj.get_total_active_cases())
    confirmed1.config(text=obj.get_total_confirmed_cases())
    recover1.config(text=obj.get_total_recovered())
    death1.config(text=obj.get_total_deaths())


def showdata():
    aaa = obj.list_countries()
    if country.get().lower() not in aaa:
        error()
        clear()
    elif country.get()=='':
        empty()
        clear()
    else:
        co = obj.get_status_by_country_name(country.get())
        coun1.config(text=country.get())
        tc1.config(text=co['total_cases'])
        c1.config(text=co['confirmed'])
        nc1.config(text=co['new_cases'])
        d1.config(text=co['deaths'])
        nd1.config(text=co['new_deaths'])
        rec1.config(text=co['recovered'])
        ac1.config(text=co['active'])
        cri1.config(text=co['critical'])
        Totest1.config(text=co['total_tests'])
        totcas1.config(text=co['total_cases_per_million'])
        totdea1.config(text=co['total_deaths_per_million'])
        popu1.config(text=co['population'])

def exitwindow():
    win.destroy()


def clear():
    country.set("")
    coun1.config(text="")
    tc1.config(text="")
    c1.config(text="")
    nc1.config(text="")
    d1.config(text="")
    nd1.config(text="")
    rec1.config(text="")
    ac1.config(text="")
    cri1.config(text="")
    Totest1.config(text="")
    totcas1.config(text="")
    totdea1.config(text="")
    popu1.config(text="")


head = Label(win,text="Covid-19 Live Data",font=('Comic Sans MS',25,"bold"),background="#c8bfe7")
head.pack(anchor="center")

country = StringVar()
entercoun = Label(win,text="Enter Country Name :",font=('Comic Sans MS',15,"bold"),background="#c8bfe7")
entercoun.place(x=120,y=65)
entry = Entry(win,textvariable=country,font=('Comic Sans MS',15),bd='3')
entry.place(x=350,y=68)
submit = Button(text="Submit",command=showdata,width=10,font=('Comic Sans MS',11),bg='#567', fg='White',relief="raised")
submit.place(x=620,y=68)

coun = Label(win, text="Country Name ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
coun.place(x=165, y=120)
tc = Label(win,text="Total Cases ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
tc.place(x=165,y=160)
c = Label(win,text="Confirmed Cases ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
c.place(x=165,y=200)
nc = Label(win,text="New Cases ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
nc.place(x=165,y=240)
d = Label(win,text="Deaths ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
d.place(x=165,y=280)
nd = Label(win,text="New Deaths ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
nd.place(x=165,y=320)
rec = Label(win, text="Recovered ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
rec.place(x=165,y=360)
ac = Label(win, text="Active Cases ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
ac.place(x=165,y=400)
cri = Label(win, text="Critical Cases ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
cri.place(x=165,y=440)
Totest = Label(win,text="Total tests " , font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
Totest.place(x=165,y=480)
totcas = Label(win,text="Total Cases per Million ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
totcas.place(x=165,y=520)
totdea = Label(win, text="Total Deaths per Million ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
totdea.place(x=165,y=560)
popu = Label(win,text="Population ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
popu.place(x=165,y=600)

coun2 = Label(win, text=": ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
coun2.place(x=380, y=120)
tc2 = Label(win,text=": ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
tc2.place(x=380,y=160)
c2 = Label(win,text=": ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
c2.place(x=380,y=200)
nc2 = Label(win,text=": ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
nc2.place(x=380,y=240)
d2 = Label(win,text=": ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
d2.place(x=380,y=280)
nd2 = Label(win,text=": ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
nd2.place(x=380,y=320)
rec2 = Label(win, text=": ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
rec2.place(x=380,y=360)
ac2 = Label(win, text=": ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
ac2.place(x=380,y=400)
cri2 = Label(win, text=": ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
cri2.place(x=380,y=440)
Totest2 = Label(win,text=": " , font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
Totest2.place(x=380,y=480)
totcas2 = Label(win,text=":", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
totcas2.place(x=380,y=520)
totdea2 = Label(win, text=": ",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
totdea2.place(x=380,y=560)
popu2 = Label(win,text=": ", font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
popu2.place(x=380,y=600)

exit = Button(text="Exit Page",command=exitwindow,width=11,font=('Comic Sans MS',11),bg='#567', fg='White')
exit.place(x=927,y=660)
clr = Button(text="Clear Data",command=clear,width=11,font=('Comic Sans MS',11),bg='#567', fg='White')
clr.place(x=340,y=660)


coun1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
coun1.place(x=450, y=120)

tc1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
tc1.place(x=450,y=160)

c1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
c1.place(x=450,y=200)

nc1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
nc1.place(x=450,y=240)

d1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
d1.place(x=450,y=280)

nd1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
nd1.place(x=450,y=320)

rec1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
rec1.place(x=450,y=360)

ac1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
ac1.place(x=450,y=400)

cri1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
cri1.place(x=450,y=440)

Totest1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
Totest1.place(x=450,y=480)

totcas1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
totcas1.place(x=450,y=520)

totdea1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
totdea1.place(x=450,y=560)

popu1 = Label(win, font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
popu1.place(x=450,y=600)

world = Label(win,text="World Wide Data",font=('Comic Sans MS', 15, "bold","underline"), background="#c8bfe7")
world.place(x=875,y=400)

active = Label(win,text="Active Cases",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
active.place(x=800,y=460)
confirmed = Label(win,text="Confirmed Cases",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
confirmed.place(x=800,y=500)
recover = Label(win,text="Recovered Cases",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
recover.place(x=800,y=540)
death = Label(win,text="Deaths",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
death.place(x=800,y=580)

active2 = Label(win,text=":",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
active2.place(x=970,y=460)
confirmed2 = Label(win,text=":",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
confirmed2.place(x=970,y=500)
recover2 = Label(win,text=":",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
recover2.place(x=970,y=540)
death2 = Label(win,text=":",font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
death2.place(x=970,y=580)

active1 = Label(win,font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
active1.place(x=1030,y=460)
confirmed1 = Label(win,font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
confirmed1.place(x=1030,y=500)
recover1 = Label(win,font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
recover1.place(x=1030,y=540)
death1 = Label(win,font=('Comic Sans MS', 13, "bold"), background="#c8bfe7")
death1.place(x=1030,y=580)
worldwide()


f1 = Frame(win,background="#c8bfe7",highlightbackground = "#c8bfe7")
f1.place(x=730,y=125,width=500,height=247)
canva = Canvas(f1,width=500,height=247,background="#c8bfe7")
canva.pack()
img = PhotoImage(file="img.png")
canva.create_image(0,0,anchor=NW,image=img)

win.mainloop()