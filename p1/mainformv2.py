# nama file: mainform.py

# impor modul tkinter

import tkinter


def main():
    # membuat form utama
    mainform = tkinter.Tk()
    # digunakan untuk membuat objek atau instance dari kelas Tk
    # yang akan dijadikan form utama

    # mengubah title bar
    mainform.wm_title("Hello TKinter")
    # merupakan method dalam class Tk yang digunakan untuk mengubah judul form

    # mengubah warna form
    mainform['background'] = "#bbc9c9"
    # adalah atribut yang digunakan untuk menentukan warna latar
    # atau kontrol lain seperti button

# disini anda dapat menambahkan kontrol lain dalam form

    # menampilkan form
    mainform.mainloop()


if __name__ == "__main__":
    main()
