import tkinter
root = tkinter.Tk()

tkinter.Button(root, text="1").grid(column=1, row=1, padx = 5, pady = 20)
tkinter.Button(root, text="2").grid(column=2, row=1, padx = 5, pady = 20)
tkinter.Button(root, text="3").grid(column=3, row=1, padx = 5, pady = 20)
tkinter.Button(root, text="+").grid(column=4, row=1, padx = 20, pady = 20)

tkinter.Button(root, text="4").grid(column=1, row=2, padx = 20, pady = 10)
tkinter.Button(root, text="5").grid(column=2, row=2, padx = 20, pady = 10)
tkinter.Button(root, text="6").grid(column=3, row=2, padx = 20, pady = 10)
tkinter.Button(root, text="-").grid(column=4, row=2, padx = 20, pady = 20)

tkinter.Button(root, text="7").grid(column=1, row=3, padx = 20, pady = 20)
tkinter.Button(root, text="8").grid(column=2, row=3, padx = 20, pady = 20)
tkinter.Button(root, text="9").grid(column=3, row=3, padx = 20, pady = 20)
tkinter.Button(root, text="x").grid(column=4, row=3, padx = 20, pady = 20)

tkinter.Button(root, text="0").grid(column=3, row=4, padx = 20, pady = 20)
tkinter.Button(root, text="=").grid(column=4, row=4, padx = 20, pady = 20)

root.mainloop()