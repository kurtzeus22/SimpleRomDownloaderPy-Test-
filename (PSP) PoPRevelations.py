from cProfile import label
import webbrowser
from cgitb import text
from msilib.schema import ComboBox
from tkinter import*
from tkinter.ttk import Combobox
window = Tk()
window.title("Install -Prince of Persia - Revelations ") #create gamename
window.geometry("500x500")
window.configure(bg='black')
window.resizable(0,0)


def popup():
    popupwindow = Toplevel(window)
    popupwindow.title("Alert")
    popupwindow.geometry("200x100")
    alert = Label(popupwindow, text="Downloading Will Start on Browser")
    button1 = Button(popupwindow, text="Okay", command=window.destroy)
    alert.pack()
    button1.pack()
    popupwindow.mainloop()

lbl1 = Label(window, text="_",  fg='black' , bg='black', font=("Arial", 13))
lbl1.pack()
lbl_about = Label(window, text="You are about to Install Prince of Persia - Revelations ", fg='white', bg='black', font=("Arial BOLD", 13)) #insert gamename
lbl_about.pack()
lbl1 = Label(window, text="_",  fg='black' , bg='black', font=("Arial", 13))
lbl1.pack()
lbl_zip = Label(window, text="*7Zip Download",width=50, anchor="w", fg='white' , bg='black', font=("Arial", 11))
lbl_zip.pack()
lbl_drive = Label(window, text="*From EmuParadise ",width=50, anchor="w", fg='white' , bg='black', font=("Arial", 11)) #insert cloud storage
lbl_drive.pack()
lbl_console = Label(window, text="*You need to have a Sony PSP/Sony PSP Emulator",width=50, anchor="w", fg='white', bg='black', font=("Arial", 12))
lbl_console.pack()
lbl2 = Label(window, text="_",  fg='black' , bg='black', font=("Arial", 13))
lbl2.pack()
lbl_ds = Label(window, text="Disk Space Required:       1230 MB" , fg='white' , bg='black', font=("Arial", 11)) #insert disk space required
lbl_ds.pack()
lbl_edt = Label(window, text="Estimated Download Time:  0:20:30 for 1MB/s ", fg='white', bg='black', font=("Arial", 11)) #insert download time
lbl_edt.pack()
lbl3 = Label(window, text="_",  fg='black', bg='black', font=("Arial", 13))
lbl3.pack()
lbl4 = Label(window, text="_",  fg='black', bg='black', font=("Arial", 13))
lbl4.pack()
lbl_loc = Label(window, text="Location for Installation: ", fg='white', bg='black', font=("Arial", 11)) #Insert Location Storage
lbl_loc.pack()

data = ("C:/Games", "C:/Emulator Games")
cb=Combobox(window, values=data, width=50)
cb.place(x=60, y=150)
cb.pack()
lbl1 = Label(window, text="_",  fg='black' , bg='black', font=("Arial", 13))
lbl1.pack()

new = 1
url = "http://162.210.194.49/happyUUKAm8913lJJnckLiePutyNak/pspisos/Prince_Of_Persia_Revelations_REPACK_USA_MULTi3_PSP-ARTiSAN.rar"
def openweb():
    webbrowser.open(url,new=new)
button1 = Button(window, text="Install", fg='white', bg='black' , width=25, command=openweb)
button2 = Button(window, text="Cancel", fg='white', bg='black' , width=25, command=window.destroy)
button1.pack()
lbl1 = Label(window, text="_",  fg='black' , bg='black', font=("Arial", 13))
lbl1.pack()
button2.pack()
window.mainloop()