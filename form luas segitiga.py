from tkinter import BOTH, END, YES, Button, Entry, Frame, Label, Tk, W
from webbrowser import BackgroundBrowser
class LuasPersegiPanjang:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x400")
        self.parent.title(title)\
      
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # pasang Label
        Label(mainFrame, text='Alas:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtalas = Entry(mainFrame) 
        self.txtalas.grid(row=0, column=1, padx=5, pady=5)  
        self.txttinggi = Entry(mainFrame) 
        self.txttinggi.grid(row=1, column=1, padx=5, pady=5) 
        self.txtLuas = Entry(mainFrame) 
        self.txtLuas.grid(row=3, column=1, padx=5, pady=5) 
        
        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=2, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas Segitiga  
    def onHitung(self, event=None):
        alas = int(self.txtalas.get())
        tinggi = int(self.txttinggi.get())
        luas = 1/2 * alas* tinggi
        self.txtLuas.delete(0,END)
        self.txtLuas.insert(END,str(luas))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = LuasPersegiPanjang(root, "Program Luas Segitiga")
    root.mainloop() 