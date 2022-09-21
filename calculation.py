from tkinter import *
from tkinter import ttk
import math
from PIL import ImageTk, Image
def reres():
    Vlab.destroy()
    collab.destroy()
    reslab.destroy()
    butreres.destroy()
    clik.grid(column=4, row=2, sticky = W)

def v():
    h = float(hent.get()) / 100
    R = float(Rent.get()) / 100
    m = float(ment.get()) / 100
    pi = 3.14

    S = h * pi * ((R + R) ** 2) / 4
    V = S * 1000

    res_A = "Целіндер має " + str(V) + " літрів."

    col = (R * 2) / m

    res_B = "Всього частин - " + str(col)

    i = 1
    a = []
    H = m

    while i != col:
        Ss = (R ** 2) * math.acos(1 - H / R) - (R - H) * (2 * R * H - (H ** 2)) ** 0.5
        Ss = (Ss * h)

        a.append(str(i) + " - " + str(Ss * 1000) + " літрів")
        H = H + m

        i = i + 1
        if i == col:
            a.append( str(int(col)) + " - " + str(V) + " літрів")

    n_A = 0
    n_B = 1

    i = len(a)
    res = ""

    while i != 0:
        res_n = a[n_A:n_B]
        res_n = str(res_n)
        res_n = res_n.replace("[", '')
        res_n = res_n.replace("]", '')
        n_A = n_A + 1
        n_B = n_B + 1
        res = res + str(res_n) + "\n"
        i = i - 1

    res_C = res

    global Vlab
    global collab
    global reslab

    Vlab = ttk.Label(frameres, text=res_A)
    Vlab.grid(column=1, row=1, sticky=W)
    collab = ttk.Label(frameres, text=res_B)
    collab.grid(column=1, row=2, sticky=W)
    reslab = ttk.Label(frameres, text=res_C)
    reslab.grid(column=1, row=3, sticky=W)

    global butreres
    butreres = ttk.Button(frame, text="Перерахувати", command=reres)
    butreres.grid(column=4, row=2, sticky = W)
    clik.grid_remove()

window = Tk()
window.title("Разрахунок літражу целіндра.")
window.geometry('630x300')

main_frame = ttk.Frame(window)
main_frame.pack(fill=BOTH, expand=1)

canvans = Canvas(main_frame)
canvans.pack(side=LEFT, fill=BOTH, expand=1)

sckroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvans.yview)
sckroll.pack(side=RIGHT, fill=Y)

canvans.configure(yscrollcommand=sckroll.set)
canvans.bind('<Configure>', lambda e: canvans.configure(scrollregion=canvans.bbox("all")))

win = ttk.Frame(canvans)

canvans.create_window((0,0), window=win, anchor="nw")

frame = ttk.Frame(win)
frame.grid(column=2, row=1)
frameimg = ttk.Frame(win)
frameimg.grid(column=1, row=1)
frameres = ttk.Frame(win)
frameres.grid(column=1, row=2)

hlab = ttk.Label(frame, text="  Висота целіндра в см -").grid(column=1, row=1, sticky = W)
hent = StringVar()
hhent = ttk.Entry(frame, textvariable=hent).grid(column=2, row=1, sticky = W)

Rlab = ttk.Label(frame, text="  Радіус целіндра в см -").grid(column=1, row=2, sticky = W)
Rent = StringVar()
RRent = ttk.Entry(frame, textvariable=Rent).grid(column=2, row=2, sticky = W)

mlab = ttk.Label(frame, text="  Висота рідини у целіндрі у наклоні в см -").grid(column=1, row=3, sticky = W)
ment = StringVar()
mment = ttk.Entry(frame, textvariable=ment).grid(column=2, row=3, sticky = W)

clik = ttk.Button(frame, command=v,text="Розрахувати")
clik.grid(column=4, row=2, sticky = W)
window.bind(v)

#img = ImageTk.PhotoImage(Image.open("image.png"))
#imgL = ttk.Label(frameimg, image = img).grid(column=1, row=1, sticky=W)

window.update_idletasks()

window.mainloop()
