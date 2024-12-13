from cwiczenie_04 import przelicz_walute
import tkinter as tk


def przelicz():
    kwota = float(amount.get())
    waluta = currency.get()
    result = przelicz_walute(kwota, waluta)
    result_label.config(text=result)

root = tk.Tk()

label = tk.Label(root, text="Kalkulator walut")
label.pack()

currency_label = tk.Label(root, text="Waluta")
currency_label.pack()

currency = tk.Entry(root)
currency.pack()

amount_label = tk.Label(root, text="Kwota")
amount_label.pack()

amount = tk.Entry(root)
amount.pack()

calculate_button = tk.Button(root, text="Przelicz", command=przelicz)
calculate_button.pack()

result_label = tk.Label(root, text="-")
result_label.pack()

root.mainloop()
# print(przelicz_walute(100, "USD"))
