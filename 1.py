from playsound import *
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
from time import sleep
import time
from cryptography.fernet import Fernet
import os
import ctypes #Error Tkinter
import getpass
import easygui
import telebot
from telebot import types
from telebot import util
import socket
from aiogram import types
from requests import get

htoken = '5063802842:AAGR7cAEm26ggCKMbYjkiOCyNmruR4-NcxU'
hadm = '666015577'
token = htoken
adm = hadm
bot = telebot.TeleBot(token, parse_mode=types.ParseMode.HTML)

USER_NAME = getpass.getuser()

window = Tk()
window.title("FeS")
window.geometry('880x500')
window.resizable(width=False, height=False)
#window['bg'] = 'black'
photo = PhotoImage(file = "6553668.png")
w = Label(window, image=photo)
w.pack()


normal_width = 1920
normal_height = 1080


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()


percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)

scale_factor = ((percentage_width + percentage_height) / 2) / 100

fontsize = int(20 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
       fontsize = minimum_size

fontsizeHding = int(72 * scale_factor)
minimum_size = 40
if fontsizeHding < minimum_size:
       fontsizeHding = minimum_size

# Create a style and configure for ttk.Button widget
default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))

def exit():
    sys.exit()

def fullscreen():
    window.attributes('-fullscreen', False, '-topmost', False)

def filemanager():
    txt.config(state="normal")#разблокируем
    txt.delete(0, 'end')
    input_file = easygui.fileopenbox(filetypes=["*.docx"])
    format(txt.insert(END, input_file))
    txt.config(state="readonly")

def clean():
    txt.config(state="normal")
    txt.delete(0, 'end')
    txt.config(state="readonly")


def reference():
    os.system('start FAQ.py')

def connect():
 
 file = open('C:\\Users\\' + os.getlogin() + '\\Documents\\Дизайн.txt', "w")
 krat = file.write("Empty")
 file.close()
 file = open('C:\\Users\\' + os.getlogin() + '\\Documents\\Практичность.txt', "w")
 krato = file.write("Empty")
 file.close()
 file = open('C:\\Users\\' + os.getlogin() + '\\Documents\\Функционал.txt', "w")
 kratos = file.write("Empty")
 file.close()

 def check():
    radio_button = str(var.get())
    file = open('C:\\Users\\' + os.getlogin() + '\\Documents\\Дизайн.txt', "w")
    file.write("Дизайн: " + radio_button + '\n')
    file.close()
    #download = open('Оценка.txt', 'rb')
    #bot.send_document(adm, download)

 def check1():
    radio_button1 = str(var1.get())
    file = open('C:\\Users\\' + os.getlogin() + '\\Documents\\Практичность.txt', "w")
    file.write("Практичность: " + radio_button1 + '\n')
    file.close()
    #download = open('Оценка.txt', 'rb')
    #bot.send_document(adm, download)

 def check2():
    radio_button2 = str(var2.get())
    file = open('C:\\Users\\' + os.getlogin() + '\\Documents\\Функционал.txt', "w")
    file.write("Функционал: " + radio_button2 + '\n')
    file.close()
    #download = open('Оценка.txt', 'rb')
    #bot.send_document(adm, download)

 def on_entry_click(event):
    #txt.config(state="normal")
    """function that gets called whenever entry is clicked"""
    if entry_w.get() == 'Добавьте отзыв...':
       entry_w.delete(0, "end") # delete all the text in the entry
       entry_w.insert(0, '') #Insert blank for user input
       entry_w.config(fg = 'black')
    #txt.config(state="readonly")

 def on_focusout(event):
    #txt.config(state="normal")
    if entry_w.get() == '':
        entry_w.insert(0, 'Добавьте отзыв...')
        entry_w.config(fg = 'grey')
    txt.config(state="readonly")

 def clicked():
    res = format(entry_w.get())
    #download = open('Оценка.txt', 'rb')
    file = open('C:\\Users\\' + os.getlogin() + '\\Documents\\Дизайн.txt')
    krat = file.read()
    file.close()
    file = open('C:\\Users\\' + os.getlogin() + '\\Documents\\Практичность.txt')
    krato = file.read()
    file.close()
    file = open('C:\\Users\\' + os.getlogin() + '\\Documents\\Функционал.txt')
    kratos = file.read()
    file.close()
    #os.system('del Оценка.txt')
    hostname = socket.gethostname()
    localip = socket.gethostbyname(hostname)
    publicip = get('http://api.ipify.org').text
    bot.send_message(adm, "Идентификатор: " + '<u>'+os.getlogin()+'</u>' + '\n' + 'Внутренний IP: ' + localip + '\n' + 'Внешний IP: ' + publicip + '\n' + '\n' + 'Оценки: ' + '\n' + krat + krato + kratos + '\n' + 'Отзыв: ' + res)
    #bot.send_document(adm, download)
    #download.close()
    ctypes.windll.user32.MessageBoxW(None, u"Спасибо! Ваш отзыв отправлен!", u"Отзыв отправлен!")
    root.destroy()
    os.system(r'del C:\Users\%username%\Documents\Дизайн.txt')
    os.system(r'del C:\Users\%username%\Documents\Практичность.txt')
    os.system(r'del C:\Users\%username%\Documents\Функционал.txt')
    #os.remove('Оценка.txt')
 

 root = Toplevel()
 root.title("Отзыв")
 root.geometry("499x500")
 root.resizable(width=False, height=False)
 #root.iconbitmap('ico.ico')

 #canvas = Canvas(root, width=0, height=0)
 #label_w = Label (root, text="Отзыв:")
 #label_w.place(x=40, y=30)

 entry_w = Entry(root, width=81)
 entry_w.grid(row=0,
               column=0,
               padx=3,
               pady=390,
               ipady=7)
 #txt.config(state="normal")
 entry_w.insert(0, 'Добавьте отзыв...')
 entry_w.bind('<FocusIn>', on_entry_click)
 entry_w.bind('<FocusOut>', on_focusout)
 entry_w.config(fg = 'grey')
 #txt.config(state="readonly")
 #entry_w.pack(side="left")
 entry_w.place(x=3, y=400)
 btn = Button(root, text="Отправить", bg='#FFFFE0', command=clicked) 
 btn.place(relx = .35, rely = .87, relwidth=.3, relheight=.1)

 root.bind('<Return>', lambda event=None: clicked())
 k = format(entry_w.get())


 txt = Label(root, text='1. Дизайн:', font='14')
 txt.place(relx = .01, rely = .01)

 txt_2 = Label(root, text='2. Практичность:', font='14')
 txt_2.place(relx = .01, rely = .19)

 txt_3 = Label(root, text='3. Функционал:', font='14')
 txt_3.place(relx = .01, rely = .37)

 #txt_two = Label(root, text='2. Удобство использования:', font='14')
 #txt_two.place(relx = .01, rely = .2)

 var = IntVar()
 #var.set(3)

 rb1 = Radiobutton(root, text='⭐', variable=var, value=1, command=check)
 rb2 = Radiobutton(root, text='⭐⭐', variable=var, value=2, command=check)
 rb3 = Radiobutton(root, text='⭐⭐⭐', variable=var, value=3, command=check)


 rb1.place(x=10, y= 25)
 rb2.place(x=10, y= 47)
 rb3.place(x=10, y= 69)

 var1 = IntVar()
 #var1.set(3)

 rb1 = Radiobutton(root, text='⭐', variable=var1, value=1, command=check1)
 rb2 = Radiobutton(root, text='⭐⭐', variable=var1, value=2, command=check1)
 rb3 = Radiobutton(root, text='⭐⭐⭐', variable=var1, value=3, command=check1)


 rb1.place(x=200, y= 110)
 rb2.place(x=200, y= 135)
 rb3.place(x=200, y= 160)

 var2 = IntVar()
 #var2.set(3)

 rb1 = Radiobutton(root, text='⭐', variable=var2, value=1, command=check2)
 rb2 = Radiobutton(root, text='⭐⭐', variable=var2, value=2, command=check2)
 rb3 = Radiobutton(root, text='⭐⭐⭐', variable=var2, value=3, command=check2)


 rb1.place(x=200, y= 210)
 rb2.place(x=200, y= 235)
 rb3.place(x=200, y= 260)


 #canvas.pack()
 root.mainloop()
 os.remove(r'C:\Users\%username%\Documents\Дизайн.txt')
 os.remove(r'C:\Users\%username%\Documents\Практичность.txt')
 os.remove(r'C:\Users\%username%\Documents\Функционал.txt')

def crypt():

 if  format(txt.get()) == '':
    ctypes.windll.user32.MessageBoxW(None, u"Поле для ввода пути к файлу пусто!", u"Ошибка", 16)
    return

 res = format(txt.get())
 filename = res
 def write_key():
    key = Fernet.generate_key()
    with open('C:\\Users\\' + getpass.getuser() + '\\Documents\\crypto.key', 'wb') as key_file:
        key_file.write(key)

 def load_key():
    return open('C:\\Users\\' + getpass.getuser() + '\\Documents\\crypto.key', 'rb').read()

 def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

 def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

 write_key()
 key = load_key()
 encrypt(filename, key)
 os.system(r'attrib +h C:\Users\%username%\Documents\crypto.key')
 ctypes.windll.user32.MessageBoxW(None, u"Файл " + res + " зашифрован!", u"Cryptor")


def decrypt():
 res = format(txt.get())
 filename = res
 
 def load_key():
    return open('C:\\Users\\' + getpass.getuser()+ '\\Documents\\crypto.key', 'rb').read()

 def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

 key = load_key()

 # расшифровать файл
 decrypt(filename, key)
 os.system(r'attrib -h C:\Users\%username%\Documents\crypto.key')
 os.system(r'del C:\Users\%username%\Documents\crypto.key')
 txt.delete(0, 'end')
 ctypes.windll.user32.MessageBoxW(None, u"Файл " + res + " расшифрован!", u"Cryptor")

#def clicked():
    #res = format(entry_w.get())
    #if res == '1':
        #sys.exit()

#def show_hide_psd():
    #if(check_var.get()):
        #entry_psw.config(show="")
    #else:
        #entry_psw.config(show="*") 

def one():

 if  format(txt.get()) == '':
    ctypes.windll.user32.MessageBoxW(None, u"Поле для ввода пути к файлу пусто!", u"Ошибка", 16)
    return

 def clicked():
    res = format(entry_w.get())
    if res == '1436':
        decrypt()
    else:
        ctypes.windll.user32.MessageBoxW(None, u"Пароль неверный!", u"Ошибка!", 16)

 root = Tk()
 root.title("FeS")
 root.geometry("350x100")
 root.resizable(width=False, height=False)
 root.iconbitmap('ico.ico')

 canvas = Canvas(root, width=300, height=100)
 label_w = Label (root, text="Пароль:")
 label_w.place(x=40, y=30)
 entry_w = Entry(root)
 entry_w.place(x=100, y=30)
 btn = Button(root, text="Ввод", command=clicked) 
 btn.place(relx = .67, rely = .2, relwidth=.3, relheight=.4)
 k = format(entry_w.get())
 #if k == "26":
    #print("rfefgvergver")
 canvas.pack()
 root.mainloop()

fullscreen()

def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if txt.get() == 'Выберите файл...':
       txt.delete(0, "end") # delete all the text in the entry
       txt.insert(0, '') #Insert blank for user input
       txt.config(fg = 'black')

def on_focusout(event):
    if txt.get() == '':
        txt.insert(0, 'Выберите файл...')
        txt.config(fg = 'grey')

#txt_two = Label(window, text='Введите путь к файлу или выберите файл из Проводника:')

txt = Entry(window, bd=3, state="readonly") 
txt.place(relx = .35, rely = .4, relwidth=.3, relheight=.06)
#txt.insert(0, 'Выберите файл...')
#txt.bind('<FocusIn>', on_entry_click)
#txt.bind('<FocusOut>', on_focusout)
#txt.config(fg = 'grey')

btn = Button(window, text="Шифровать!", command=crypt)
btn2 = Button(window, text="Дешифровать!", command=one)
btn3 = Button(window, text="Выйти", command=exit)
btn4 = Button(window, text="Открыть", command=filemanager)
btn5 = Button(window, text="FAQ", command=reference)
btn6 = Button(window, text="Очистить", command=clean)


#txt_two.place(relx = .3, rely = .35)
btn.place(relx = .56, rely = .5, relwidth=.1, relheight=.06)
btn2.place(relx = .34, rely = .5, relwidth=.1, relheight=.06)
btn3.place(relx = .02, rely = .9, relwidth=.1, relheight=.06)
btn4.place(relx = .45, rely = .5, relwidth=.1, relheight=.06)
btn5.place(relx = 0.88, rely = .9, relwidth=.1, relheight=.06)
btn6.place(relx = .67, rely = .4, relwidth=.1, relheight=.06)


cpi = Label(window, text='Оставить отзыв', fg="blue", cursor="hand2", bg='#FFFFE0')
cpi.place(relx = .43, rely = .95)
cpi.bind("<Button-1>", lambda e: connect())

window.mainloop()