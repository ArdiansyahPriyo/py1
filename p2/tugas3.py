from tkinter import*
import tkinter.messagebox


def main():
    mainform = Tk()
    app = Form1(mainform)
    mainform['background'] = "#ced6d6"
    mainform.mainloop()

# =========================Window 1=============================
# membuat kelas login dengan nama Form1


class Form1():
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry('280x110+0+0')
        # self.master.config(bg='#b8b5ad')
        self.frame = Frame(self.master, bg='#ced6d6')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

# ======================lABEL & ENTRY======================
        self.lblTitle = Label(self.frame, bg='#ced6d6', font=('Candara', 15))
        self.lblTitle['text'] = "Login"
        self.lblTitle.grid(
            row=0, column=1, sticky=tkinter.N + tkinter.E + tkinter.W)

        self.lblUname = Label(self.frame, bg="#ced6d6")
        self.lblUname['text'] = "Username"
        self.lblUname['font'] = "Consolas"
        self.lblUname.grid(row=1, column=0)  # -------

        self.lblPass = Label(self.frame, bg="#ced6d6")
        self.lblPass['text'] = "Password"
        self.lblPass['font'] = "Consolas"
        self.lblPass.grid(row=2, column=0)

        self.txtUname = Entry(self.frame, textvariable=self.Username)
        self.txtUname['width'] = 30
        self.txtUname.grid(row=1, column=1, columnspan=2)

        self.txtPass = Entry(self.frame, show="*", textvariable=self.Password)
        self.txtPass['width'] = 30
        self.txtPass.grid(row=2, column=1, columnspan=2)
# =======================BUTTON=============================
        self.btnLogin = Button(self.frame, font=(
            'Consolas', 10), command=self.proses_login)
        self.btnLogin['text'] = "Login"
        self.btnLogin.grid(
            row=3, column=1, sticky=tkinter.E + tkinter.W)

        self.btnReset = Button(self.frame, font=(
            'Consolas', 10), command=self.reset)
        self.btnReset['text'] = "Reset"
        self.btnReset.grid(
            row=3, column=2, sticky=tkinter.E + tkinter.W)
# ========================Fungsi=================================

    def proses_login(self):
        uname = (self.Username.get())
        passw = (self.Password.get())
        if (uname == str("user1") and passw == str("admin")):
            self.newForm = Toplevel(self.master)
            self.app = Form2(self.newForm)
        else:
            tkinter.messagebox.showinfo("Information", "Login Gagal ^_^")
            self.Username.set("")
            self.Password.set("")
            self.txtUname.focus()

    def reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUname.focus()

    def new_form(self):
        self.newForm = Toplevel(self.master)
        self.app = Form2(self.newForm)
# ==============================================================


# =========================Window 2=============================
# membuat kelas dengan nama Form2
class Form2:
    def __init__(self, master):
        self.master = master
        self.master.title("IP MHS")
        self.master.geometry('590x500+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        mk1 = StringVar()
        mk2 = StringVar()
        mk3 = StringVar()
        mk4 = StringVar()
        mk5 = StringVar()
        mk6 = StringVar()
        mk7 = StringVar()
        mk8 = StringVar()
        ip = StringVar()

        # fungsi insert mahasiswa
        def insertmhs(*cok):
            listbox.insert(tkinter.END, entry.get())

        # fungsi menghitung IP
        def hasil():
            a = float(txt1.get())
            b = float(txt2.get())
            c = float(txt3.get())
            d = float(txt4.get())
            e = float(txt5.get())
            f = float(txt6.get())
            g = float(txt7.get())
            h = float(txt8.get())

            total = (a + b + c + d + e + f + g + h)/8
            totNilai.insert(0, total)

        # fungsi reset
        def reset():
            mk1.set("")
            mk2.set("")
            mk3.set("")
            mk4.set("")
            mk5.set("")
            mk6.set("")
            mk7.set("")
            mk8.set("")
            ip.set("")

        # fungsi untuk menghapus data di listbox
        def deletemhs():
            listbox.delete(tkinter.ANCHOR)

# ======================Label,Entry,Button================================
        lbl1 = Label(self.frame, height=2)
        lbl1['text'] = "Masukkan Nama Mahasiswa"
        lbl1['font'] = "Candara"
        lbl1.grid(row=1, column=0, sticky=tkinter.W)

        # membuat objek button
        btnAdd = Button(self.frame, command=insertmhs,
                        bg="#387340", font=('Corbel', 10, 'bold'))
        btnAdd['text'] = "Add"
        btnAdd['fg'] = "white"
        btnAdd.grid(row=1, column=0, sticky=tkinter.E, padx=5)

        btnDel = Button(self.frame, command=deletemhs,
                        bg="#b30c0c", font=('Corbel', 10, 'bold'))
        btnDel['text'] = "Delete"
        btnDel['fg'] = "white"
        btnDel.grid(row=2, column=0, sticky=tkinter.N + tkinter.E, padx=5)

        # membuat objek entry
        entry = Entry(self.frame)
        entry['width'] = 40
        entry.grid(row=1, column=1)

        # membuat objek listbox
        listbox = Listbox(self.frame)
        listbox['width'] = 40
        listbox.grid(row=2, column=1)

        # membuat objek label
        lbl2 = Label(self.frame)
        lbl2['text'] = "1. Keamanan Sistem dan Jaringan"
        lbl2['font'] = "Candara"
        lbl2.grid(row=3, column=0, sticky=tkinter.W)

        # membuat objek entry
        txt1 = Entry(self.frame, textvariable=mk1)
        txt1['width'] = 30
        txt1.grid(row=3, column=1, sticky=tkinter.W)

        # membuat objek label
        lbl3 = Label(self.frame)
        lbl3['text'] = "2. Praktik Keamanan Sistem dan Jaringan"
        lbl3['font'] = "Candara"
        lbl3.grid(row=4, column=0, sticky=tkinter.W)

        # membuat objek entry
        txt2 = Entry(self.frame, textvariable=mk2)
        txt2['width'] = 30
        txt2.grid(row=4, column=1, sticky=tkinter.W)

        # membuat objek label
        lbl4 = Label(self.frame)
        lbl4['text'] = "3. Digital Enterpreneurship"
        lbl4['font'] = "Candara"
        lbl4.grid(row=5, column=0, sticky=tkinter.W)

        # membuat objek entry
        txt3 = Entry(self.frame, textvariable=mk3)
        txt3['width'] = 30
        txt3.grid(row=5, column=1, sticky=tkinter.W)

        # membuat objek label
        lbl5 = Label(self.frame)
        lbl5['text'] = "4. Bahasa Indonesia"
        lbl5['font'] = "Candara"
        lbl5.grid(row=6, column=0, sticky=tkinter.W)

        # membuat objek entry
        txt4 = Entry(self.frame, textvariable=mk4)
        txt4['width'] = 30
        txt4.grid(row=6, column=1, sticky=tkinter.W)

        # membuat objek label
        lbl6 = Label(self.frame)
        lbl6['text'] = "5. Pemrograman Berbasis Dekstop"
        lbl6['font'] = "Candara"
        lbl6.grid(row=7, column=0, sticky=tkinter.W)

        # membuat objek entry
        txt5 = Entry(self.frame, textvariable=mk5)
        txt5['width'] = 30
        txt5.grid(row=7, column=1, sticky=tkinter.W)

        # membuat objek label
        lbl7 = Label(self.frame)
        lbl7['text'] = "6. Praktik Pemrograman Berbasis Dekstop"
        lbl7['font'] = "Candara"
        lbl7.grid(row=8, column=0, sticky=tkinter.W)

        # membuat objek entry
        txt6 = Entry(self.frame, textvariable=mk6)
        txt6['width'] = 30
        txt6.grid(row=8, column=1, sticky=tkinter.W)

        # membuat objek label
        lbl8 = Label(self.frame)
        lbl8['text'] = "7. Tata Kelola Teknologi Informasi"
        lbl8['font'] = "Candara"
        lbl8.grid(row=9, column=0, sticky=tkinter.W)

        # membuat objek entry
        txt7 = Entry(self.frame, textvariable=mk7)
        txt7['width'] = 30
        txt7.grid(row=9, column=1, sticky=tkinter.W)

        # membuat objek label
        lbl9 = Label(self.frame)
        lbl9['text'] = "8. Pancasila"
        lbl9['font'] = "Candara"
        lbl9.grid(row=10, column=0, sticky=tkinter.W)

        # membuat objek entry
        txt8 = Entry(self.frame, textvariable=mk8)
        txt8['width'] = 30
        txt8.grid(row=10, column=1, sticky=tkinter.W)

        # membuat objek button
        btnHitung = tkinter.Button(
            self.frame, command=hasil, bg="#2757a1", font=('Corbel', 10, 'bold'))
        btnHitung['text'] = "Hitung"
        btnHitung['fg'] = "white"
        btnHitung.grid(row=11, column=1, sticky=tkinter.W)

        btnReset = tkinter.Button(
            self.frame, command=reset, bg="#e0e0e0", font=('Corbel', 10, 'bold'))
        btnReset['fg'] = "black"
        btnReset['text'] = "Reset"
        btnReset.grid(row=11, column=1, sticky=tkinter.W, padx=60)

        # membuat objek label
        lbl10 = Label(self.frame)
        lbl10['text'] = "IP Mahasiswa"
        lbl10['font'] = "Candara"
        lbl10.grid(row=12, column=0, sticky=tkinter.E, padx=10)

        # membuat objek entry
        totNilai = Entry(self.frame, textvariable=ip)
        totNilai['width'] = 30
        totNilai.grid(row=12, column=1, sticky=tkinter.W)


if __name__ == "__main__":
    main()
