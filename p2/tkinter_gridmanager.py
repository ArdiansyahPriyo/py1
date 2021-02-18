# nama file : tkinter_gridmanager

#import modul
import tkinter


def main():
    mainform = tkinter.Tk()

    mainform.wm_title("User Login")

    lbl1 = tkinter.Label(mainform)
    lbl1['text'] = "Username"
    lbl1.grid(row=0, column=0)

    lbl2 = tkinter.Label(mainform)
    lbl2['text'] = "Password"
    lbl2.grid(row=1, column=0)

    txt1 = tkinter.Entry(mainform)
    txt1['width'] = 40
    txt1.grid(row=0, column=1, columnspan=2)

    txt2 = tkinter.Entry(mainform)
    txt2['width'] = 40
    txt2.grid(row=1, column=1, columnspan=2)

    chk = tkinter.Checkbutton(mainform)
    chk['text'] = "Remember Me"
    chk.grid(row=2, column=0)

    btn1 = tkinter.Button(mainform)
    btn1['text'] = "Login"
    btn1.grid(row=2, column=1)

    btn2 = tkinter.Button(mainform)
    btn2['text'] = "Exit"
    btn2.grid(row=2, column=2)

    mainform.mainloop()


if __name__ == "__main__":
    main()
