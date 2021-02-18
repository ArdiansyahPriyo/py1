# nama file: tugas2.py
# impor modul tkinter

import tkinter


def main():
    # membuat form utama
    mainform = tkinter.Tk()
    # digunakan untuk membuat objek atau instance dari kelas Tk
    # yang akan dijadikan form utama

    # mengubah title bar
    mainform.wm_title("Tugas 2")
    mainform['background'] = "#bbc9c9"

    # fungsi insert pada listbox
    def insertmhs(*args):
        listbox.insert(tkinter.END, entry.get())

    # fungsi menghitung total IP mahasiswa
    def hasil(hsl):
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

    # membuat objek label
    lbl1 = tkinter.Label(mainform, height=2)
    lbl1['text'] = "Masukkan Nama Mahasiswa"
    lbl1.grid(row=0, column=0)

    # membuat objek button
    btn = tkinter.Button(mainform)
    btn['text'] = "Add Data"
    btn.bind("<Button-1>", insertmhs)
    btn.grid(row=1, column=0)

    # membuat objek entry
    entry = tkinter.Entry(mainform)
    entry['width'] = 20
    entry.grid(row=1, column=1)

    # membuat objek listbox
    listbox = tkinter.Listbox(mainform)
    listbox.grid(row=2, column=1)

    # membuat objek label
    lbl2 = tkinter.Label(mainform)
    lbl2['text'] = "1. Keamanan Sistem dan Jaringan"
    lbl2.grid(row=3, column=0)

    # membuat objek entry
    txt1 = tkinter.Entry(mainform)
    txt1['width'] = 20
    txt1.grid(row=3, column=1)

    # membuat objek label
    lbl3 = tkinter.Label(mainform)
    lbl3['text'] = "2. Praktik Keamanan Sistem dan Jaringan"
    lbl3.grid(row=4, column=0)

    # membuat objek entry
    txt2 = tkinter.Entry(mainform)
    txt2['width'] = 20
    txt2.grid(row=4, column=1)

    # membuat objek label
    lbl4 = tkinter.Label(mainform)
    lbl4['text'] = "3. Digital Enterpreneurship"
    lbl4.grid(row=5, column=0)

    # membuat objek entry
    txt3 = tkinter.Entry(mainform)
    txt3['width'] = 20
    txt3.grid(row=5, column=1)

    # membuat objek label
    lbl5 = tkinter.Label(mainform)
    lbl5['text'] = "4. Bahasa Indonesia"
    lbl5.grid(row=6, column=0)

    # membuat objek entry
    txt4 = tkinter.Entry(mainform)
    txt4['width'] = 20
    txt4.grid(row=6, column=1)

    # membuat objek label
    lbl6 = tkinter.Label(mainform)
    lbl6['text'] = "5. Pemrograman Berbasis Dekstop"
    lbl6.grid(row=7, column=0)

    # membuat objek entry
    txt5 = tkinter.Entry(mainform)
    txt5['width'] = 20
    txt5.grid(row=7, column=1)

    # membuat objek label
    lbl7 = tkinter.Label(mainform)
    lbl7['text'] = "6. Praktik Pemrograman Berbasis Dekstop"
    lbl7.grid(row=8, column=0)

    # membuat objek entry
    txt6 = tkinter.Entry(mainform)
    txt6['width'] = 20
    txt6.grid(row=8, column=1)

    # membuat objek label
    lbl8 = tkinter.Label(mainform)
    lbl8['text'] = "7. Tata Kelola Teknologi Informasi"
    lbl8.grid(row=9, column=0)

    # membuat objek entry
    txt7 = tkinter.Entry(mainform)
    txt7['width'] = 20
    txt7.grid(row=9, column=1)

    # membuat objek label
    lbl9 = tkinter.Label(mainform)
    lbl9['text'] = "8. Pancasila"
    lbl9.grid(row=10, column=0)

    # membuat objek entry
    txt8 = tkinter.Entry(mainform)
    txt8['width'] = 20
    txt8.grid(row=10, column=1)

    # membuat objek button
    btn = tkinter.Button(mainform, bg="#2757a1")
    btn['text'] = "Hitung"
    btn.bind("<Button-1>", hasil)
    btn.grid(row=11, column=1)

    # membuat objek label
    lbl10 = tkinter.Label(mainform)
    lbl10['text'] = "IP Mahasiswa"
    lbl10.grid(row=12, column=0)

    # membuat objek entry
    totNilai = tkinter.Entry(mainform)
    totNilai.grid(row=12, column=1)

    # menampilkan form
    mainform.mainloop()


if __name__ == "__main__":
    main()
