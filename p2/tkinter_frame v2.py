# file name : tkinter_frame v2

import tkinter as tkinter

# membuat kelas demo frame
# diturunkan dari kelas frame


class DemoFrame(tkinter.Frame):
    # membuat konstruktor DemoFrame
    def __init__(self, master=None):
        # memanggil konstruktor kelas induk (tkinter.frame)
        tkinter.Frame.__init__(self, master)
       # self.grid()
        self.buatKontrol()

        # membuat den menempatkan kontrol ke dalam frame

    def buatKontrol(self):
        self.btnKeluar = tkinter.Button(self, text="Keluar", command=self.quit)
        self.btnKeluar.grid(sticky=tkinter.E, padx=90, pady=90)


def main():
    # membuat kelas demo
    app = DemoFrame()
    app.master.title("Demo Frame")
    app.mainloop()


# memanggil fungsi
if __name__ == "__main__":
    main()
