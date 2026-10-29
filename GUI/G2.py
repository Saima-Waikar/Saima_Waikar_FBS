import tkinter as tk

r = tk.Tk()
r.title("My GUI")
r.geometry("400x300")

tk.Label(r, text="Enter your name").pack()

e = tk.Entry(r)
e.pack()

def show():
    print(e.get())

btn = tk.Button(r, text="Submit", command=show)
btn.pack()

r.mainloop()
