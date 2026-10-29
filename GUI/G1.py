import tkinter as tk

r = tk.Tk()
r.title("GUI Application")
r.geometry("500x400")

l1 = tk.Label(
    r,
    text="This is my first GUI App",
    bg="Yellow",
    fg="Blue",
    font=("Californian FB", 14)
)

l1.pack()
r.mainloop()