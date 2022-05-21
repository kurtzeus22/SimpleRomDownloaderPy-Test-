#INSTALLER MAKER QUICK
import PySimpleGUI as sg
import datetime
import os
import sys

sg.theme('DarkGrey6')

looper=0
while looper < 1:
    layout = [
        [sg.Text('Installer Maker Python')],
        [sg.Text('Game Name: ', size =(20, 1)), sg.InputText()],
        [sg.Text('Console to Use for Game: ', size =(20, 1)), sg.InputText()],
        [sg.Text('Cloud Storage: ', size =(20, 1)), sg.InputText()],
        [sg.Text('Total Size of Game in MB: ', size =(20, 1)), sg.InputText()],
        [sg.Text('URL for File: ', size =(20, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ]

    window = sg.Window('Install Maker Python', layout,size=(500,250))
    event, values = window.read()
    window.close()
   
    diskint = int(values[3])
    timer = str(datetime.timedelta(seconds=diskint))  
    print('')
    print('')
    print('')
    print('RESULT')
    print('')
    print('from cProfile import label')
    print('import webbrowser')
    print('from cgitb import text')
    print('from msilib.schema import ComboBox')
    print('from tkinter import*')
    print('from tkinter.ttk import Combobox')
    print('window = Tk()')
    print('window.title("Install -' + values[0] + ' ") #create gamename')
    print('window.geometry("500x500")')
    print('window.configure(bg=\'black\')')
    print('window.resizable(0,0)')
    print('')
    print('')
    print('def popup():')
    print('    popupwindow = Toplevel(window)')
    print('    popupwindow.title("Alert")')
    print('    popupwindow.geometry("200x100")')
    print('    alert = Label(popupwindow, text="Downloading Will Start on Browser")')
    print('    button1 = Button(popupwindow, text="Okay", command=window.destroy)')
    print('    alert.pack()')
    print('    button1.pack()')
    print('    popupwindow.mainloop()')
    print('')
    print('lbl1 = Label(window, text="_",  fg=\'black\' , bg=\'black\', font=("Arial", 13))')
    print('lbl1.pack()')
    print('lbl_about = Label(window, text="You are about to Install ' + values[0] + ' ", fg=\'white\', bg=\'black\', font=("Arial BOLD", 13)) #insert gamename')
    print('lbl_about.pack()')
    print('lbl1 = Label(window, text="_",  fg=\'black\' , bg=\'black\', font=("Arial", 13))')
    print('lbl1.pack()')
    print('lbl_zip = Label(window, text="*7Zip Download",width=50, anchor="w", fg=\'white\' , bg=\'black\', font=("Arial", 11))')
    print('lbl_zip.pack()')
    print('lbl_drive = Label(window, text="*From ' + values[2] + ' ",width=50, anchor="w", fg=\'white\' , bg=\'black\', font=("Arial", 11)) #insert cloud storage')
    print('lbl_drive.pack()')
    print('lbl_console = Label(window, text="*You need to have a ' + values[1] + '/' + values[1] + ' Emulator",width=50, anchor="w", fg=\'white\', bg=\'black\', font=("Arial", 12))')
    print('lbl_console.pack()')
    print('lbl2 = Label(window, text="_",  fg=\'black\' , bg=\'black\', font=("Arial", 13))')
    print('lbl2.pack()')
    print('lbl_ds = Label(window, text="Disk Space Required:  \t' + values[3] + ' MB" , fg=\'white\' , bg=\'black\', font=("Arial", 11)) #insert disk space required')
    print('lbl_ds.pack()')
    print('lbl_edt = Label(window, text="Estimated Download Time: \t' + timer + ' for 1MB/s ", fg=\'white\', bg=\'black\', font=("Arial", 11)) #insert download time')
    print('lbl_edt.pack()')
    print('lbl3 = Label(window, text="_",  fg=\'black\', bg=\'black\', font=("Arial", 13))')
    print('lbl3.pack()')
    print('lbl4 = Label(window, text="_",  fg=\'black\', bg=\'black\', font=("Arial", 13))')
    print('lbl4.pack()')
    print('lbl_loc = Label(window, text="Location for Installation: ", fg=\'white\', bg=\'black\', font=("Arial", 11)) #Insert Location Storage')
    print('lbl_loc.pack()')
    print('')
    print('data = ("C:/Games", "C:/Emulator Games")')
    print('cb=Combobox(window, values=data, width=50)')
    print('cb.place(x=60, y=150)')
    print('cb.pack()')
    print('lbl1 = Label(window, text="_",  fg=\'black\' , bg=\'black\', font=("Arial", 13))')
    print('lbl1.pack()')
    print('')

    print('new = 1')
    print('url = "' + values[4] + '"')
    print('def openweb():')
    print('    webbrowser.open(url,new=new)')

    print('button1 = Button(window, text="Install", fg=\'white\', bg=\'black\' , width=25, command=openweb)')
    print('button2 = Button(window, text="Cancel", fg=\'white\', bg=\'black\' , width=25, command=window.destroy)')
    print('button1.pack()')
    print('lbl1 = Label(window, text="_",  fg=\'black\' , bg=\'black\', font=("Arial", 13))')
    print('lbl1.pack()')
    print('button2.pack()')
    print('window.mainloop()')

    os.system("pause")
    print('')
    print('Do you want to try again? 1 = YES | 0 = NO: ')
    loopers = int(input())
    if loopers == 1:
        looper == 0
    elif loopers == 0:
        looper =+ 1

    os.system("pause")

