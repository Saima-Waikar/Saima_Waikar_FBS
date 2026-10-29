import tkinter as tk

r = tk.Tk()
r.title("My GUI")
r.geometry("400x300")

tk.Label(r, text="Enter your name").grid(row=0, column=0)

e = tk.Entry(r)
e.grid(row=0, column=1)

def show():
    print(e.get())

btn = tk.Button(r, text="Submit", command=show)
btn.grid(row=1, column=0)

r.mainloop()
