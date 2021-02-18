import tkinter


def main():
    mainform = tkinter.Tk()
    mainform.wm_title("widget button")
    mainform.geometry('300x300+0+0')

    def hapus():
        txt1.delete(0, "end")

    lbl = tkinter.Label(mainform, height=2, font=('Candara', 15))
    lbl['text'] = "Opsi pada Entry"
    lbl.grid(row=0, column=1, columnspan=2, sticky=tkinter.E+tkinter.W)

    lbl1 = tkinter.Label(mainform, height=2)
    lbl1['text'] = "Entry"
    lbl1.grid(row=2, column=1)

    txt1 = tkinter.Entry(mainform, cursor='cross', font=('Courier', 12))
    txt1['width'] = 20
    txt1.grid(row=2, column=2)

    btn1 = tkinter.Button(
        mainform, activebackground='#c7080e', command=hapus)
    btn1['text'] = "Hapus"
    btn1.grid(row=3, column=2, sticky=tkinter.E)
    mainform.mainloop()


if __name__ == "__main__":
    main()
