from tkinter import *


class main_win:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        self.root.bind("<Return>", self.submit_func)

        self.labelHead = Label(self.root, font="monospace 10 bold", text="Stundenlohn")
        self.labelHead.place(x=80, y=20)

        self.entryMoney = Entry(self.root, font="monospace 10 bold")
        self.entryMoney.place(x=52, y=65)

        self.labelQu = Label(self.root, font="monospace 10 bold", text="Wöchentliche Arbeitsstunde")
        self.labelQu.place(x=40, y=110)

        self.entryTime = Entry(self.root, font="monospace 10 bold", )
        self.entryTime.place(x=52, y=155)

        self.buttonSubmit = Button(self.root, border=0.5, bg="grey", font="monospace 8 bold", text="Berechne",command=self.submit_func)
        self.buttonSubmit.place(x=90, y=200)

        self.labelDay = Label(self.root, font="monospace 9 bold", text="Sie verdienen am Tag: ")
        self.labelDay.place(x=270, y=35)

        self.labelWeek = Label(self.root, font="monospace 9 bold", text="Sie verdienen in der Woche: ")
        self.labelWeek.place(x=270, y=95)

        self.labelMonth = Label(self.root, font="monospace 9 bold", text="Sie verdienen im Monat: ")
        self.labelMonth.place(x=270, y=155)

        self.labelYear = Label(self.root, font="monospace 9 bold", text="Sie verdienen im Jahr: ")
        self.labelYear.place(x=270, y=215)

        self.root.mainloop()

    def submit_func(self, event=None):
        pricePreHour = self.entryMoney.get()
        hoursInWeek = self.entryTime.get()

        day = float(pricePreHour) * 8
        week = float(pricePreHour) * float(hoursInWeek)
        month = week * 4.33
        year = week * 52

        self.labelDay.config(text="Sie verdienen am Tag: \n" + str(day) + "€")
        self.labelWeek.config(text="Sie verdienen in der Woche: \n" + str(week) + "€")
        self.labelMonth.config(text="Sie verdienen im Monat: \n" + str(month) + "€")
        self.labelYear.config(text="Sie verdienen im Jahr: \n" + str(year) + "€")

root = main_win("Gehaltsrechner")
