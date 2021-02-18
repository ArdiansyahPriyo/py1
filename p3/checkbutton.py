from tkinter import*


def main():
    mainform = Tk()
    mainform.wm_title("widget button")
    mainform.geometry('230x300+0+0')

    def dslct():
        chk1.deselect()

    lbl = Label(mainform, height=2, font=('Candara', 15))
    lbl['text'] = "Opsi pada CkheckButton"
    lbl.grid(row=0, column=1, columnspan=2, sticky=E+W)

    lbl1 = Label(mainform, height=2)
    lbl1['text'] = "Deselect"
    lbl1.grid(row=2, column=1)

    chk1 = Checkbutton(mainform)
    chk1.grid(row=2, column=2)

    btn2 = Button(
        mainform, activebackground='#c7080e', command=dslct)
    btn2['text'] = "Uncheck"
    btn2.grid(row=3, column=2, sticky=E)

    lbl2 = Label(mainform, height=2)
    lbl2['text'] = "Select Color"
    lbl2.grid(row=4, column=1)

    chk2 = Checkbutton(mainform, selectcolor='#adede9')
    chk2.grid(row=4, column=2)

    mainform.mainloop()


if __name__ == "__main__":
    main()
