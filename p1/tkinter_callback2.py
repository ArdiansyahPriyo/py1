import tkinter
import tkinter.messagebox


def main():
    mainform = tkinter.Tk()

    def buttonclick(*args):
        tkinter.messagebox.showinfo(
            "Hallo", "Hallo % s, apa kabar" % (txt.get()))

    lbl = tkinter.Label(mainform)
    lbl['text'] = "Masukkan Nama Anda"
    lbl.pack()

    txt = tkinter.Entry(mainform)
    txt['width'] = 40
    txt.pack()

    btn = tkinter.Button(mainform)
    btn['text'] = "Klik Saya"
    btn.bind("<Button-1>", buttonclick)
    btn.pack()

    mainform.mainloop()


if __name__ == "__main__":
    main()
