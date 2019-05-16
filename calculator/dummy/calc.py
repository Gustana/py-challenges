import tkinter
from tkinter import *
root = tkinter.Tk()

opr = StringVar()

def insertText(text) :
    entry1.insert(10, text)

def setOperation(text) :
    opr.set(text)

def result() :
    bil1 = int(entry1.get())
    bil2 = int(entry2.get())
    oprs = opr.get()

    if oprs == "+" :
        result = bil1 + bil2
    elif oprs == "x" :
        result = bil1 * bil2
    elif oprs == "-" :
        result = bil1 - bil2
    else :
        result = bil1 / bil2

    print(opr)
    print(result)

    entry3.delete(0, END)
    entry3.insert(0, str(result))

entry1 = tkinter.Entry(root)

operation = tkinter.Label(root, textvariable = opr)
operation.grid()

entry2 = tkinter.Entry(root)
entry2.grid()

entry3 = tkinter.Entry(root)

tkinter.Button(root, text="1", command = lambda:insertText("1")).grid(column=1, row=1, padx = 5, pady = 20)
tkinter.Button(root, text="2", command = lambda:insertText("2")).grid(column=2, row=1, padx = 5, pady = 20)
tkinter.Button(root, text="3", command = lambda:insertText("3")).grid(column=3, row=1, padx = 5, pady = 20)
tkinter.Button(root, text="+", command = lambda:setOperation("+")).grid(column=4, row=1, padx = 5, pady = 20)

tkinter.Button(root, text="4", command = lambda:insertText("4")).grid(column=1, row=2, padx = 20, pady = 10)
tkinter.Button(root, text="5", command = lambda:insertText("5")).grid(column=2, row=2, padx = 20, pady = 10)
tkinter.Button(root, text="6", command = lambda:insertText("6")).grid(column=3, row=2, padx = 20, pady = 10)
tkinter.Button(root, text="-", command = lambda:setOperation("-")).grid(column=4, row=2, padx = 20, pady = 20)

tkinter.Button(root, text="7", command = lambda:insertText("7")).grid(column=1, row=3, padx = 20, pady = 20)
tkinter.Button(root, text="8", command = lambda:insertText("8")).grid(column=2, row=3, padx = 20, pady = 20)
tkinter.Button(root, text="9", command = lambda:insertText("9")).grid(column=3, row=3, padx = 20, pady = 20)
tkinter.Button(root, text="x", command = lambda:setOperation("x")).grid(column=4, row=3, padx = 20, pady = 20)

tkinter.Button(root, text=":", command = lambda:setOperation(":")).grid(column=4, row=4, padx = 20, pady = 20)
tkinter.Button(root, text="0", command = lambda:insertText("0")).grid(column=2, row=4, padx = 20, pady = 20)
tkinter.Button(root, text="=", command = lambda:result()).grid(column=3, row=4, padx = 20, pady = 20)

root.mainloop()