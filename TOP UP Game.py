import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from tkinter import filedialog, Text
from tkinter import StringVar
from tkinter import *
import os

root = Tk()  
root.geometry("567x960")
root.title("TOP UP GAME ABCD")
root.iconbitmap('H:\PICTURE\EMOT\icon\DColon.ico')
root.resizable (height= False, width= False)

class gbye:
    def gbye():
        bye="GOOD BYE"
        messagebox.showinfo("THANK YOU!", bye)
        exit(0)


bg = PhotoImage(file="H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/bgawal.png")
ground = Canvas(root, width=567, height=960)
ground.pack(fill="both", expand=True)
ground.create_image(0,0, image=bg, anchor="nw")






def genshinimpact():
    def order():
        step = 1
        if len(loginvia.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI LOGIN VIA TERLEBIH DAHULU")
            step = 0
        if len(server.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI SERVER TERLEBIH DAHULU")
            step = 0
        if len(nickname.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI NICKNAME TERLEBIH DAHULU")
            step = 0
        if len(username.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI USERNAME TERLEBIH DAHULU")
            step = 0
        if len(masukharga.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN LAKUKAN PEMBAYARAN TERLEBIH DAHULU")
            step = 0
        if tombol.get() == 0:
            messagebox.showerror("WHOOOOOPSS!","PILIH PESANAN SEBELUM MENGORDER")
        else:
            while step == 1:
                if tombol.get()==1:
                    harga="65000"
                    order="300 GC"
                elif tombol.get()==2:
                    harga="190000"
                    order="980 GC"
                elif tombol.get()==3:
                    harga="380000"
                    order="1980 GC"
                elif tombol.get()==4:
                    harga="650000"  
                    order="3280 GC"
                elif tombol.get()==5:
                    harga="1250000"  
                    order="6480 GC"
                elif tombol.get()==6:
                    harga="65000"  
                    order="Blessing of the Welkin Moon"
                elif tombol.get()==7:
                    harga="125000"  
                    order="BP. Gnosis Hymn"
                elif tombol.get()==8:
                    harga="245000"  
                    order="BP. Gnosis Chorus"
                
                if int(harga)>int(masukharga.get()):
                    messagebox.showinfo("WARNING!","MAAF UANG ANDA TIDAK CUKUP!")
                else:
                    hitungan = int(masukharga.get()) - int(harga)
                
                hasil =  "USERNAME : " + username.get() + " ORDER : " + order + " SERVER : " + server.get() + " Harga Rp. " + harga + ",00" + " Kembalian : Rp. " + str(hitungan) + ",00"
                messagebox.showinfo("ABCD STRORE", hasil)
                step =0

    global bgimage
    genshin = Toplevel()
    genshin.title('GENSHIN IMPACT')
    genshin.iconbitmap('H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/gnshin.ico')
    genshin.resizable (height = False, width = False)


    
    bgimage = PhotoImage(file="H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/GENSHINPR.png")
    
    ground = Canvas(genshin, width=1024, height=768)
    
    ground.pack(fill="both", expand=True)
    
    ground.create_image(0,0, image=bgimage, anchor="nw")
    
    
    
    
    
    loginvia = StringVar()
    via= Entry(genshin, font=('Phenomena', 17), width = 20, textvariable=loginvia).place(x = 706, y = 137) 
    server = StringVar()
    sv = Entry(genshin, font=('Phenomena', 17),width = 20, textvariable=server).place(x = 706, y = 237)
    nickname = StringVar()
    nm = Entry(genshin,font=('Phenomena', 17), width = 20, textvariable=nickname).place(x = 706, y = 337)
    username = StringVar()
    um = Entry(genshin,font=('Phenomena', 17), width = 20, textvariable=username).place(x = 706, y = 437)
    

    masukharga = Entry(genshin, font = ('Phenomena', 17), width = 20,)
    masukharga.place(x = 706, y = 537)
    
    
    tombol = IntVar()
    button1 = Checkbutton(genshin, bg="black", variable=tombol, onvalue=1, offvalue=0).place(x=110, y=195)  
    button2 = Checkbutton(genshin, bg="black", variable=tombol, onvalue=2, offvalue=0).place(x=110, y=245)  
    button3 = Checkbutton(genshin, bg="black", variable=tombol, onvalue=3, offvalue=0).place(x=110, y=295)  
    button4 = Checkbutton(genshin, bg="black", variable=tombol, onvalue=4, offvalue=0).place(x=110, y=345)
    button5 = Checkbutton(genshin, bg="black", variable=tombol, onvalue=5, offvalue=0).place(x=110, y=395)
    button6 = Checkbutton(genshin, bg="black", variable=tombol, onvalue=6, offvalue=0).place(x=110, y=482)
    button7 = Checkbutton(genshin, bg="black", variable=tombol, onvalue=7, offvalue=0).place(x=110, y=600)
    button4 = Checkbutton(genshin, bg="black", variable=tombol, onvalue=8, offvalue=0).place(x=110, y=655)
    
    def back():
        genshin.destroy()
        
        
    
    
    button1 = Button(genshin, font = ('bonobo'), bg="cyan",height=2, width=7, command = order, text="ORDER").place(x=766,y=600)
    btnback = Button(genshin, font = ('bonobo'),bg="yellow", height=2, width=7, text = "BACK", command = back ).place(x=906,y=700)

########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

def arknights():
    def order():
        step = 1
        if len(loginvia.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI LOGIN VIA TERLEBIH DAHULU")
            step = 0
        if len(server.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI SERVER TERLEBIH DAHULU")
            step = 0
        if len(masukharga.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN LAKUKAN PEMBAYARAN TERLEBIH DAHULU")
            step = 0
        if len(username.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI USERNAME TERLEBIH DAHULU")
            step = 0
        if tombol.get() == 0:
            messagebox.showerror("WHOOOOOPSS!","PILIH PESANAN SEBELUM MENGORDER")
        else:
            while step == 1:
                if tombol.get()==1:
                    harga="65000"
                    order="6 Originium"
                elif tombol.get()==2:
                    harga="190000"
                    order="20 Originium"
                elif tombol.get()==3:
                    harga="380000"
                    order="40 Originium"
                elif tombol.get()==4:
                    harga="650000"  
                    order="66 Originium"
                elif tombol.get()==5:
                    harga="1250000"  
                    order="130 Originium"
                elif tombol.get()==6:
                    harga="65000"  
                    order="Monthly Card"
                elif tombol.get()==7:
                    harga="125000"  
                    order="Weekly Growth"
                elif tombol.get()==8:
                    harga="125000"  
                    order="Starter Upgrade"
                elif tombol.get()==9:
                    harga="245000"  
                    order="Starter Headhunting"
                elif tombol.get()==10:
                    harga="320000"  
                    order="Monthly Headhunting"
                
                if int(harga)>int(masukharga.get()):
                    messagebox.showinfo("WARNING!","MAAF UANG ANDA TIDAK CUKUP!")
                else:
                    hitungan = int(masukharga.get()) - int(harga)
                
                hasil =  "USERNAME : " + username.get() + " ORDER : " + order + " SERVER : " + server.get() + " Harga Rp. " + harga + ",00" + " Kembalian : Rp. " + str(hitungan) + ",00"
                messagebox.showinfo("ABCD STRORE", hasil)
                step =0

    global bgimage
    arknight = Toplevel()
    arknight.title('ARKNIGHT')
    arknight.iconbitmap('H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/logoak.ico')
    arknight.resizable (height = False, width = False)


    
    bgimage = PhotoImage(file="H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/ARKNIGHTPR.png")
    
    ground = Canvas(arknight, width=1024, height=768)
    
    ground.pack(fill="both", expand=True)
    
    ground.create_image(0,0, image=bgimage, anchor="nw")
    
    
    
    
    loginvia = StringVar()
    via= Entry(arknight, font=('Phenomena', 17), width = 20, textvariable=loginvia).place(x = 749, y = 167) 
    server = StringVar()
    sv = Entry(arknight, font=('Phenomena', 17),width = 20, textvariable=server).place(x = 749, y = 267)
    username = StringVar()
    um = Entry(arknight,font=('Phenomena', 17), width = 20, textvariable=username).place(x = 749, y = 387)
    
    masukharga = Entry(arknight, font = ('Phenomena', 17), width = 20,)
    masukharga.place(x = 749, y = 587)
    
    
    tombol = IntVar()
    button1 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=1, offvalue=0).place(x=40, y=145)  
    button2 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=2, offvalue=0).place(x=40, y=185)  
    button3 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=3, offvalue=0).place(x=40, y=225)  
    button4 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=4, offvalue=0).place(x=40, y=265)
    button5 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=5, offvalue=0).place(x=40, y=305)
    button6 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=6, offvalue=0).place(x=40, y=455)
    button7 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=7, offvalue=0).place(x=40, y=495)
    button8 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=8, offvalue=0).place(x=40, y=540)
    button9 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=9, offvalue=0).place(x=40, y=580)
    button10 = Checkbutton(arknight, bg="black", variable=tombol, onvalue=10, offvalue=0).place(x=40, y=625)
    
    def back():
        arknight.destroy()
    
    button1 = Button(arknight,font = ('bonobo'), bg="cyan",height=2, width=7, command = order, text="ORDER").place(x=806,y=640)
    btnback = Button(arknight,font = ('bonobo'), bg="yellow", height=2, width=7, text = "BACK", command = back ).place(x=906,y=700)
    
########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

def ML():
    def order():
        step = 1
        if int(idml.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI ID TERLEBIH DAHULU")
            step = 0
        if len(masukharga.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN LAKUKAN PEMBAYARAN TERLEBIH DAHULU")
            step = 0
        if len(nickname.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI NICKNAME TERLEBIH DAHULU")
            step = 0
        if tombol.get() == 0:
            messagebox.showerror("WHOOOOOPSS!","PILIH PESANAN SEBELUM MENGORDER")
        else:
            while step == 1:
                if tombol.get()==1:
                    harga="59000"
                    order="275 Diamond"
                elif tombol.get()==2:
                    harga="155000"
                    order="706 Diamond"
                elif tombol.get()==3:
                    harga="227000"
                    order="1049 Diamond"
                elif tombol.get()==4:
                    harga="300000"  
                    order="2194 Diamond"
                elif tombol.get()==5:
                    harga="445000"  
                    order="3072 Diamond"
                elif tombol.get()==6:
                    harga="630000"  
                    order="3688 Diamond"
                elif tombol.get()==7:
                    harga="735000"  
                    order="5532 Diamond"
                elif tombol.get()==8:
                    harga="1100000"  
                    order="6238 Diamond"
                elif tombol.get()==9:
                    harga="1250000"  
                    order="6238 Diamond"
                elif tombol.get()==10:
                    harga="1825000"  
                    order="9288 Diamond"
                elif tombol.get()==11:
                    harga="1975000"  
                    order="9994 Diamond"
                elif tombol.get()==12:
                    harga="2460000"  
                    order="12188 Diamond"
                
                if int(harga)>int(masukharga.get()):
                    messagebox.showinfo("WARNING!","MAAF UANG ANDA TIDAK CUKUP!")
                else:
                    hitungan = int(masukharga.get()) - int(harga)
                
                hasil =  "NICKNAME : " + nickname.get() + " ID : " + str(idml.get()) + " ORDER : " + order+ " Harga Rp. " + harga + ",00" + " Kembalian : Rp. " + str(hitungan) + ",00"
                messagebox.showinfo("ABCD STRORE", hasil)
                step =0

    global bgimage
    mlbb = Toplevel()
    mlbb.title('Mobile Legend')
    mlbb.iconbitmap('H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/logoml.ico')
    mlbb.resizable (height = False, width = False)


    
    bgimage = PhotoImage(file="H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/MLPR.png")
    
    ground = Canvas(mlbb, width=1024, height=768)
    
    ground.pack(fill="both", expand=True)
    
    ground.create_image(0,0, image=bgimage, anchor="nw")
    
    
    
    idml= Entry(mlbb, font = ('Phenomena', 17), width = 20,)
    idml.place(x = 740, y = 200) 
    
    
    nickname = StringVar()
    nm = Entry(mlbb,font=('Phenomena', 17), width = 20, textvariable=nickname).place(x = 740, y = 320)
    
    masukharga = Entry(mlbb, font = ('Phenomena', 17), width = 20,)
    masukharga.place(x = 740, y = 460)
    
    tombol = IntVar()
    button1 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=1, offvalue=0).place(x=80, y=130)  
    button2 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=2, offvalue=0).place(x=80, y=175)  
    button3 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=3, offvalue=0).place(x=80, y=225)  
    button4 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=4, offvalue=0).place(x=80, y=270)
    button5 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=5, offvalue=0).place(x=80, y=315)
    button6 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=6, offvalue=0).place(x=80, y=365)
    button7 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=7, offvalue=0).place(x=80, y=412)
    button8 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=8, offvalue=0).place(x=80, y=465)
    button9 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=9, offvalue=0).place(x=80, y=505)
    button10 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=10, offvalue=0).place(x=80, y=555)
    button11 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=11, offvalue=0).place(x=80, y=600)
    button12 = Checkbutton(mlbb, bg="black", variable=tombol, onvalue=12, offvalue=0).place(x=80, y=650)
    
    
    def back():
        mlbb.destroy()
    
    button1 = Button(mlbb,font = ('bonobo'), bg="cyan",height=2, width=7, command = order, text="ORDER").place(x=806,y=550)
    btnback = Button(mlbb,font = ('bonobo'), bg="yellow", height=2, width=7, text = "BACK", command = back ).place(x=906,y=700)
    
########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

def pubg():
    def order():
        step = 1
        if int(idpubg.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI ID TERLEBIH DAHULU")
            step = 0
        if len(masukharga.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN LAKUKAN PEMBAYARAN TERLEBIH DAHULU")
            step = 0
        if len(nickname.get()) == 0:
            messagebox.showerror("WHOOOOOPSS!","SILAHKAN MENGISI NICKNAME TERLEBIH DAHULU")
            step = 0
        if tombol.get() == 0:
            messagebox.showerror("WHOOOOOPSS!","PILIH PESANAN SEBELUM MENGORDER")
        else:
            while step == 1:
                if tombol.get()==1:
                    harga="135000"
                    order="770 UC"
                elif tombol.get()==2:
                    harga="325000"
                    order="2013 UC"
                elif tombol.get()==3:
                    harga="640000"
                    order="4200 UC"
                elif tombol.get()==4:
                    harga="1300000"  
                    order="8750 UC"
                if int(harga)>int(masukharga.get()):
                    messagebox.showinfo("WARNING!","MAAF UANG ANDA TIDAK CUKUP!")
                else:
                    hitungan = int(masukharga.get()) - int(harga)
                
                hasil =  "NICKNAME : " + nickname.get() + " ID : " + str(idpubg.get()) + " ORDER : " + order + " Harga Rp. " + harga + ",00" + " Kembalian : Rp. " + str(hitungan) + ",00"
                messagebox.showinfo("ABCD STRORE", hasil)
                step =0

    global bgimage
    pubg = Toplevel()
    pubg.title('Player Unkown Battle Ground')
    pubg.iconbitmap('H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/logopubg.ico')
    pubg.resizable (height = False, width = False)


    
    bgimage = PhotoImage(file="H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/PUBGPR.png")
    
    ground = Canvas(pubg, width=1024, height=768)
    
    ground.pack(fill="both", expand=True)
    
    ground.create_image(0,0, image=bgimage, anchor="nw")
    
    
    
    
    idpubg= Entry(pubg, font = ('Phenomena', 17), width = 20,)
    idpubg.place(x = 740, y = 200) 
    
    
    nickname = StringVar()
    nm = Entry(pubg,font=('Phenomena', 17), width = 20, textvariable=nickname).place(x = 740, y = 320)
    
    masukharga = Entry(pubg, font = ('Phenomena', 17), width = 20,)
    masukharga.place(x = 740, y = 460)
    
    tombol = IntVar()
    button1 = Checkbutton(pubg, bg="black", variable=tombol, onvalue=1, offvalue=0).place(x=65, y=370)  
    button2 = Checkbutton(pubg, bg="black", variable=tombol, onvalue=2, offvalue=0).place(x=65, y=430)  
    button3 = Checkbutton(pubg, bg="black", variable=tombol, onvalue=3, offvalue=0).place(x=65, y=485)  
    button4 = Checkbutton(pubg, bg="black", variable=tombol, onvalue=4, offvalue=0).place(x=65, y=540)
    
    def back():
        pubg.destroy()
    
    button1 = Button(pubg,font = ('bonobo'), bg="cyan",height=2, width=7, command = order, text="ORDER").place(x=806,y=550)
    btnback = Button(pubg,font = ('bonobo'), bg="yellow", height=2, width=7, text = "BACK", command = back ).place(x=906,y=700)
    
    




btngs = PhotoImage(file='H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/buttongs.png')
btnak = PhotoImage(file='H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/buttonak.png')
btnml = PhotoImage(file='H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/buttonml.png')
btnpubg = PhotoImage(file='H:/UNDIP/SMT2/DKP/TUGAS AKHIR/bismillah final/buttonpubg.png')


button1=Button(root, command = genshinimpact, image=btngs,borderwidth = 0, ).place(x = 108,y = 260)
button2=Button(root, command = arknights, image=btnak,borderwidth = 0).place(x = 108,y = 360)
button3=Button(root, command = ML, image=btnml,borderwidth = 0).place(x = 108,y = 460)
button4=Button(root, command = pubg, image=btnpubg, borderwidth = 0).place(x = 108,y = 560)







exitbutton = Button(root,font = ('bonobo'), height=2, width= 7,  bg="yellow", command = gbye.gbye, text="KELUAR").place(x=440,y=850)



root.mainloop()





