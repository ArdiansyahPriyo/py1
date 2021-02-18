import tkinter
import tkinter.messagebox
import tkinter.font as font


def main():
    mainform = tkinter.Tk()
    mainform.wm_title("widget button")
    mainform.geometry('230x300+0+0')

    def pesan(*args):
        tkinter.messagebox.showinfo(
            "Hallo", "Hallo")

    lbl = tkinter.Label(mainform, height=2, font=('Candara', 15))
    lbl['text'] = "Opsi pada Button"
    lbl.grid(row=0, column=1, columnspan=2, sticky=tkinter.E+tkinter.W)

    lbl1 = tkinter.Label(mainform, height=2)
    lbl1['text'] = "Active Background"
    lbl1.grid(row=2, column=1)

    btn1 = tkinter.Button(mainform, activebackground='#2c7ec9')
    btn1['text'] = "Button 1"
    btn1.grid(row=2, column=2)

    lbl2 = tkinter.Label(mainform, height=2)
    lbl2['text'] = "Active Foreground"
    lbl2.grid(row=3, column=1)

    buttonFont = font.Font(family='Candara', size=12, underline=1)
    btn2 = tkinter.Button(
        mainform, activeforeground='#c7080e', font=buttonFont)
    btn2['text'] = "Button 2"
    btn2.grid(row=3, column=2)

    lbl3 = tkinter.Label(mainform, height=2)
    lbl3['text'] = "Border"
    lbl3.grid(row=4, column=1)

    btn3 = tkinter.Button(mainform, border=10)
    btn3['text'] = "Button 3"
    btn3.grid(row=4, column=2)

    lbl4 = tkinter.Label(mainform, height=2)
    lbl4['text'] = "Background"
    lbl4.grid(row=5, column=1)

    btn4 = tkinter.Button(mainform, bg='#faeb20')
    btn4['text'] = "Button 4"
    btn4.grid(row=5, column=2)

    lbl4 = tkinter.Label(mainform, height=2)
    lbl4['text'] = "Command"
    lbl4.grid(row=6, column=1)

    btn5 = tkinter.Button(mainform)
    btn5['text'] = "Button 5"
    btn5.bind("<Button-1>", pesan)
    btn5.grid(row=6, column=2)

    mainform.mainloop()


if __name__ == "__main__":
    main()
