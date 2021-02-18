import tkinter


def main():
    mainform = tkinter.Tk()

    lbl = tkinter.Label(mainform)
    lbl['text'] = "Masukkan Nama Anda"
    lbl.pack()

    txt = tkinter.Entry(mainform)
    txt['width'] = 40
    txt.pack()

    btn = tkinter.Button(mainform)
    btn['text'] = "Klik Saya"
    btn.pack()

    mainform.mainloop()


if __name__ == "__main__":
    main()
