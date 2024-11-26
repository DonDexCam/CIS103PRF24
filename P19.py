#Donavan Bryant using Tkinter to make a smily face

from tkinter import*
def main():
    mainwin=Tk()
    color='#8000ff'
    color='light blue'
    wcan=Canvas(mainwin,bg=color,
                width=600,height=800)
    wcan.pack()
    wcan.create_oval(600,22,14,450,
                     fill='white',outline='black',width=5)
    wcan.create_oval(133,100,187,200,
                     fill='orange',outline="black",width=5)
    wcan.create_oval(380,149,250,200,
                     fill='orange',outline='black',width=5)
    wcan.create_line(275,275,200,275,
                     width=35,fill='green')
    wcan.create_line(500,500,310,310,
                     width=10,fill='blue')
    wcan.create_line(600,425,25,450,
                     width=10,fill='blue')
    wcan.create_line(100,500,310,310,
                     width=10,fill='blue')
    
    mainwin.mainloop()
main()
