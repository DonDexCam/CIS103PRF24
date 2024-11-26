#Donavan Bryant using tkinter to convert celius to fahereinheit 

from tkinter import*
def Calc(txtbox,txtbox2,txtbox3,txtbox4):
    
    Work=txtbox.get()
    try:
        Work=float(Work)
        if Work<0:
            txtbox4.insert(0,'Must be positive number')
        else:
            
            Celsius=Work-273.15
            txtbox2.insert(0,Celsius)
            Fah=(9/5)*(Work-273)+32
            txtbox3.insert(0,Fah)
        
        
    except:
        txtbox4.insert(0,'invalid number')

    return
def Clear(txtbox,txtbox2,txtbox3,txtbox4):
    txtbox.delete(0,'end')
    txtbox2.delete(0,'end')
    txtbox3.delete(0,'end')
    txtbox4.delete(0,'end')
    return
def createwinmain():
    winmain=Tk()
    winmain.geometry('800x600')
    winmain.configure(bg='lightblue')
    winmain.title('Temperature conversion')
    txt=Label(winmain,
              font=('Times New Roman', 20),
              text='Temperature conversion',
              fg='red')
    txt.place(x=250,y=50)
    return(winmain,txt) 
def labeltxt(winmain):
    txtboxlbl=Label(winmain,font=('Times New Roman', 20),
                    text='Kelvin',
                    fg='yellow',bg='black')
    txtboxlbl.place(x=25,y=150)
    txtbox=Entry(winmain,width=20,
                 font=('Times New Roman',20))
    txtbox.place(x=250,y=150)
    return(txtboxlbl,txtbox)

    
def labeltxt2(winmain):
    txtboxlbl2=Label(winmain,font=('Times New Roman',20),
                     text='Celsius:',
                     fg='yellow',bg='black')
    txtboxlbl2.place(x=30,y=200)
    txtbox2=Entry(winmain,width=20,
                  font=('Times New Roman',20))
    txtbox2.place(x=250,y=200)
    return (txtboxlbl2,txtbox2)
def labeltxt3 (winmain):
    txtboxlbl3=Label(winmain,font=('Times New Roman',20),
                     text='Fahrenheit:',
                     fg='yellow',bg='black')
    txtboxlbl3.place(x=30,y=250)
    txtbox3=Entry(winmain,width=20,
                  font=('Times New Roman',20))
    txtbox3.place(x=250,y=250)
    return(txtboxlbl3,txtbox3)
def errbox(winmain):
    txtbox4=Entry(winmain,width=50,
                 font=('Times New Roman',20))
    txtbox4.place(x=40,y=300)
    return(txtbox4)

#Buttons
def btns(winmain,txtbox,txtbox2,txtbox3,txtbox4):
    cmdcopy=Button(winmain,
                   font=('Times New Roman',16),text='Calc',
                   command=lambda:Calc(txtbox,txtbox2,txtbox3,txtbox4))
    
    cmdcopy.place(x=100,y=350)
def btns2(winmain,txtbox,txtbox2,txtbox3,txtbox4):
    cmdclear=Button(winmain,
                    font=('Times New Roman',16),text='Clear',
                    command=lambda:Clear(txtbox,txtbox2,txtbox3,txtbox4))
    cmdclear.place(x=300,y=350)

def win001():
    (winmain,txt)=createwinmain()
    (txtboxtlbl,txtbox)=labeltxt(winmain)
    (txtboxlbl2,txtbox2)=labeltxt2(winmain)
    (txtboxlbl3,txtbox3)=labeltxt3(winmain)
    (txtbox4)=errbox(winmain)
    (cmdcopy)=btns(winmain,txtbox,txtbox2,txtbox3,txtbox4)
    (cmdclear)=btns2(winmain,txtbox,txtbox2,txtbox3,txtbox4)
    mainloop()
win001()
