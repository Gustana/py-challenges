import tkinter as tk

class firstGUI(tk.Tk) :
    def __init__(self, *args, **kwargs) :
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.title(self, "Simple Calc")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

       
    def show_frame(self, controller) :
        frame = self.frames[controller]
        frame.tkraise()

    def greet(self) :
        print("Hello World")

class StartPage(tk.Frame):

    def __init__(self, parent, controller) :
        tk.Frame.__init__(self, parent)

        for i in range(1) :
            for j in range(3) :
                tk.Label(self, text="%s" %j,
                borderwidth = 1).grid(row=i, column=j)

        btn_one = tk.Button(self, text="1")
        btn_one.pack(pady=10, padx=30)

app = firstGUI()
app.mainloop()