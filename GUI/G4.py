import tkinter as tk

r = tk.Tk()
r.title("My GUI")
r.geometry("400x300")

tk.Label(r, text="Enter your name").place(x=50, y=50)

e = tk.Entry(r)
e.place(x=170, y=50)

def show():
    print(e.get())

btn = tk.Button(r, text="Submit", command=show)
btn.place(x=150, y=100)

r.mainloop()
