from tkinter import Tk, Button, Label

class firstGUI :
    def __init__(self, master) :
        self.master = master
        master.title("Simple GUI")

        self.label = Label(master, text="First GUI")
        self.label.pack()

        self.greet_button = Button(master, text="Geet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()
    
    def greet(self) :
        print("Hello World")

root = Tk()
gui = firstGUI(root)
root.mainloop()