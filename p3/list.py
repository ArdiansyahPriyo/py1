import tkinter


def main():
    mainform = tkinter.Tk()
    mainform.wm_title("Listbox")
    mainform.geometry('300x300+0+0')

    def insertmhs(*args):
        listbox.insert(tkinter.END, entry.get())

    def deletemhs(*args):
        listbox.delete(tkinter.ANCHOR)

    lbl = tkinter.Label(mainform, height=2, font=('Candara', 15))
    lbl['text'] = "Listbox"
    lbl.grid(row=0, column=2, columnspan=2, sticky=tkinter.E+tkinter.W)

    btn = tkinter.Button(mainform, activebackground='#2887c7')
    btn['text'] = "Add Data"
    btn.bind("<Button-1>", insertmhs)
    btn.grid(row=1, column=1, columnspan=2, sticky=tkinter.E+tkinter.W)

    btn = tkinter.Button(mainform, activebackground='#c42124')
    btn['text'] = "Delete"
    btn.bind("<Button-1>", deletemhs)
    btn.grid(row=2, column=1, columnspan=2,
             sticky=tkinter.N+tkinter.E+tkinter.W)

    entry = tkinter.Entry(mainform)
    entry['width'] = 20
    entry.grid(row=1, column=3)

    listbox = tkinter.Listbox(mainform)
    listbox.grid(row=2, column=3)

    mainform.mainloop()


if __name__ == "__main__":
    main()
