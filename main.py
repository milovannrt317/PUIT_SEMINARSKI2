from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image
from parabolaUtil import *
import numberValidation as nv


def parabola1(x):
    return float(entA1.get()) * pow(x, 2) + float(entB1.get()) * x + float(entC1.get())


def parabola2(x):
    return float(entA2.get()) * pow(x, 2) + float(entB2.get()) * x + float(entC2.get())


def nacrtaj():
    global imgPar

    if float(entA1.get()) == 0 or float(entA2.get()) == 0:
        messagebox.showerror("Greska!", "a1 i a2 moraju biti različiti od 0")
        return

    v1 = findVertex(float(entA1.get()), float(entB1.get()), parabola1)
    v2 = findVertex(float(entA2.get()), float(entB2.get()), parabola2)

        # if v1[0] < 0 or v1[1] < 0 or v2[0] < 0 or v2[1] < 0:
    #     messagebox.showerror("Greska!", "Moraju vertexi (najvisa/najniza tacka) da se nalaze u prvom kvadrantu!")
    #     return

    x = np.arange(float(entXmin.get()), float(entXmax.get()), 0.001)
    y1 = parabola1(x)
    y2 = parabola2(x)
    lineblue, = plt.plot(x, y1, 'b', label='parabola 1')
    linered, = plt.plot(x, y2, 'r', label='parabola 2')
    plt.grid(True)
    plt.xlabel('X osa')
    plt.ylabel('Y osa')
    plt.ylim(min(v1[1], v2[1]) - 10, max(v1[1], v2[1]) + 10)
    plt.legend(handles=[lineblue, linered], loc=2)
    plt.savefig('plot.png')
    plt.clf()
    im = Image.open("plot.png")
    width, height = im.size
    im2 = im.resize((width // 2, height // 2))
    imgPar = ImageTk.PhotoImage(im2)
    canvas.create_image(0, 0, anchor=NW, image=imgPar)

    rez = findIntersection(float(entA1.get()), float(entB1.get()), float(entC1.get()),
                           float(entA2.get()), float(entB2.get()), float(entC2.get()), parabola1, parabola2, v1, v2)
    if rez == -1:
        rez = "beskonacno"
    strRez.set("Resenje je: " + str(rez))
    messagebox.showinfo("Izracunato!", "Resenje je: " + str(rez))


def normalizeRed(intensity):
    Pi = intensity
    Po = (Pi - miniR.get()) * (((maxoR.get() - minoR.get()) / (maxiR.get() - miniR.get())) + minoR.get())
    return Po


def normalizeGreen(intensity):
    Pi = intensity
    Po = (Pi - miniG.get()) * (((maxoG.get() - minoG.get()) / (maxiG.get() - miniG.get())) + minoG.get())
    return Po


def normalizeBlue(intensity):
    Pi = intensity
    Po = (Pi - miniB.get()) * (((maxoB.get() - minoB.get()) / (maxiB.get() - miniB.get())) + minoB.get())
    return Po


def norm_kontr(image, label):
    multiBands = image.split()
    normalized_R = multiBands[0].point(normalizeRed)
    normalized_G = multiBands[1].point(normalizeGreen)
    normalized_B = multiBands[2].point(normalizeBlue)
    normalizedImage = Image.merge("RGB", (normalized_R, normalized_G, normalized_B))
    normImage = ImageTk.PhotoImage(normalizedImage)
    label.config(image=normImage)
    label.image = normImage


root = Tk()
root.title('Seminarski 2')
# za centriranje prozora na sredinu ekrana
root.geometry('900x500+{}+{}'.format((root.winfo_screenwidth() // 2) - (900 // 2),
                                     (root.winfo_screenheight() // 2) - (500 // 2)))
root.option_add("*Font", ('Courier', 12))
strRez = StringVar()
vcmdF = (root.register(nv.validateFloat))
vcmdI = (root.register(nv.validateInt))

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Zadatak 1')
tabControl.add(tab2, text='Zadatak 2')
tabControl.pack(expand=1, fill="both")

# zadatak 1

canvas = Canvas(tab1, width=320, height=240, bg='lightyellow')
canvas.pack()

frmZad1 = Frame(tab1)

# interval
frmInterval = LabelFrame(frmZad1, text="Interval na pozitivnom delu x ose")
Label(frmInterval, text="xmin").pack()
entXmin = Entry(frmInterval, validate='all', validatecommand=(vcmdI, '%P'))
entXmin.pack()
Label(frmInterval, text="xmax").pack()
entXmax = Entry(frmInterval, validate='all', validatecommand=(vcmdI, '%P'))
entXmax.pack(pady=(0, 10))
frmInterval.grid(row=0, column=0, padx=(0, 10))

# parabola1
frmParabola1 = LabelFrame(frmZad1, text="Parabola 1 a*x^2+b*x+c")
Label(frmParabola1, text="a").pack()
entA1 = Entry(frmParabola1, validate='all', validatecommand=(vcmdF, '%P'))
entA1.pack()
Label(frmParabola1, text="b").pack()
entB1 = Entry(frmParabola1, validate='all', validatecommand=(vcmdF, '%P'))
entB1.pack()
Label(frmParabola1, text="c").pack()
entC1 = Entry(frmParabola1, validate='all', validatecommand=(vcmdF, '%P'))
entC1.pack(pady=(0, 10))
frmParabola1.grid(row=0, column=1, padx=(0, 10))

# parabola2
frmParabola2 = LabelFrame(frmZad1, text="Parabola 2 a*x^2+b*x+c")
Label(frmParabola2, text="a").pack()
entA2 = Entry(frmParabola2, validate='all', validatecommand=(vcmdF, '%P'))
entA2.pack()
Label(frmParabola2, text="b").pack()
entB2 = Entry(frmParabola2, validate='all', validatecommand=(vcmdF, '%P'))
entB2.pack()
Label(frmParabola2, text="c").pack()
entC2 = Entry(frmParabola2, validate='all', validatecommand=(vcmdF, '%P'))
entC2.pack(pady=(0, 10))
frmParabola2.grid(row=0, column=2, padx=(0, 10))

frmZad1.pack(pady=(0, 10))

Label(tab1, textvariable=strRez).pack()
strRez.set("Resenje je: ")
btnCrtaj = Button(tab1, text="Nacrtaj", command=nacrtaj)
btnCrtaj.pack()

# zadatak 2

miniR = IntVar(value=80)
maxiR = IntVar(value=230)
minoR = IntVar(value=0)
maxoR = IntVar(value=255)

miniG = IntVar(value=90)
maxiG = IntVar(value=220)
minoG = IntVar(value=0)
maxoG = IntVar(value=255)

miniB = IntVar(value=100)
maxiB = IntVar(value=200)
minoB = IntVar(value=0)
maxoB = IntVar(value=255)

kontrastFrame = Frame(tab2)

crvena = LabelFrame(kontrastFrame, text="Crvena", fg="red")
# Plc = Label(crvena, text='crvena', fg='red').grid(row=0, column=0)
Plcmin = Label(crvena, text='min').grid(row=0, column=1)
Plcmax = Label(crvena, text='max').grid(row=0, column=2)
Plcin = Label(crvena, text='input').grid(row=1, column=0)
Plcout = Label(crvena, text='output').grid(row=2, column=0)
minIR = Spinbox(crvena, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=miniR, width=4).grid(
    row=1, column=1)
maxIR = Spinbox(crvena, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=maxiR, width=4).grid(
    row=1, column=2)
minOR = Spinbox(crvena, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=minoR, width=4).grid(
    row=2, column=1)
maxOR = Spinbox(crvena, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=maxoR, width=4).grid(
    row=2, column=2)

zelena = LabelFrame(kontrastFrame, text="Zelena", fg="green")
# Plz = Label(zelena, text='zelena', fg='green').grid(row=0, column=0)
Plzmin = Label(zelena, text='min').grid(row=0, column=1)
Plzmax = Label(zelena, text='max').grid(row=0, column=2)
Plzin = Label(zelena, text='input').grid(row=1, column=0)
Plzout = Label(zelena, text='output').grid(row=2, column=0)

minIG = Spinbox(zelena, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=miniG, width=4).grid(
    row=1, column=1)
maxIG = Spinbox(zelena, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=maxiG, width=4).grid(
    row=1, column=2)
minOG = Spinbox(zelena, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=minoG, width=4).grid(
    row=2, column=1)
maxOG = Spinbox(zelena, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=maxoG, width=4).grid(
    row=2, column=2)

plava = LabelFrame(kontrastFrame, text="Plava", fg="blue")
# Plb = Label(plava, text='plava', fg='blue').grid(row=0, column=0)
Plbmin = Label(plava, text='min').grid(row=0, column=1)
Plbmax = Label(plava, text='max').grid(row=0, column=2)
Plbin = Label(plava, text='input').grid(row=1, column=0)
Plbout = Label(plava, text='output').grid(row=2, column=0)

minIB = Spinbox(plava, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=miniB, width=4).grid(
    row=1, column=1)
maxIB = Spinbox(plava, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=maxiB, width=4).grid(
    row=1, column=2)
minOB = Spinbox(plava, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=minoB, width=4).grid(
    row=2, column=1)
maxOB = Spinbox(plava, from_=0, to=255, command=lambda: norm_kontr(img, label2), textvariable=maxoB, width=4).grid(
    row=2, column=2)

crvena.pack(side=LEFT, pady=(0, 10), padx=(5, 5))
zelena.pack(side=LEFT, pady=(0, 10), padx=(5, 5))
plava.pack(side=LEFT, pady=(0, 10), padx=(5, 5))

dugmeFrm = Frame(tab2)
dugme = Button(dugmeFrm, command=lambda: norm_kontr(img, label2), text="Prikazi normalizovanu sliku")
dugme.pack()

imgFrame = Frame(tab2)
img = Image.open("Magla.jpg")
width, height = img.size
img = img.resize((round(300 / height * width), round(300)))
slika = ImageTk.PhotoImage(img)
label = Label(imgFrame, image=slika)
label.image = slika  # trik zbog reference
label.pack(side=LEFT)

slika2 = ImageTk.PhotoImage(img)
label2 = Label(imgFrame, image=slika2)
label2.image = slika2  # trik zbog reference
label2.pack(side=RIGHT)

kontrastFrame.pack()
dugmeFrm.pack()
imgFrame.pack()

root.mainloop()
