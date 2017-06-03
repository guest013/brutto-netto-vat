import tkinter as tk
from tkinter import messagebox

def show_tax(rate):
    b = brutto.get()
    n = round(b / rate, 2)
    # Format string with 2 digits after the decimal point
    netto.set(format(n, '.2f'))
    t = round(b - n, 2)
    vat.set(format(t, '.2f'))

def message():
    messagebox.showinfo(':)', 'Mojej mamie. Żeby czasem było łatwiej')

root = tk.Tk()
root.config(bd=2)
root.resizable(0, 0)
root.title('Obliczacz')

brutto = tk.DoubleVar()
netto = tk.StringVar()
vat = tk.StringVar()

tk.Label(root, text='Wprowadź wartość brutto').grid(row=0, column=0, columnspan=5)

e = tk.Entry(root, textvariable=brutto)
e.grid(row=1, column=1, columnspan=3, sticky='WE', padx=5, pady=5)

tk.Label(root, text='Wybierz stawkę podatku VAT').grid(row=2, column=0, columnspan=5)

b = tk.Button(root, width=6, text='5 %', command=lambda r=1.05: show_tax(r))
b.grid(row=3, column=0, padx=5, pady=5)

b = tk.Button(root, width=6, text='8 %', command=lambda r=1.08: show_tax(r))
b.grid(row=3, column=2, padx=5, pady=5)

b = tk.Button(root, width=6, text='23 %', command=lambda r=1.23: show_tax(r))
b.grid(row=3, column=4, padx=5, pady=5)

tk.Label(root).grid(row=4, column=0, columnspan=5)

tk.Label(root, text='Netto').grid(row=5, column=0, columnspan=2, sticky='WE')
tk.Label(root, text='VAT').grid(row=5, column=3, columnspan=2, sticky='WE')

l = tk.Label(root, textvariable=netto, relief='raised')
l.grid(row=6, column=0, columnspan=2, sticky='WE')

l = tk.Label(root, textvariable=vat, relief='raised')
l.grid(row=6, column=3, columnspan=2, sticky='WE')

b = tk.Button(root, text='?', command=message)
b.grid(row=7, column=2)

root.mainloop()
