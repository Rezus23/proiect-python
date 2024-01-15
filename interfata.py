import tkinter as tk
from forex_python.converter import CurrencyRates
from proiect import ConverterApp

def execute_converter():
    root = tk.Tk()
    app = ConverterApp(root)
    main_window.destroy()
    root.mainloop()
   


main_window = tk.Tk()
main_window.geometry("900x400")
main_window.title("Converter Opener")

label = tk.Label(main_window, text="Catre convertor", font=('Times New Roman',25))
label.pack(pady=25)

button = tk.Button(main_window, text="Open it!", command=execute_converter)
button.pack(pady=100)

main_window.mainloop()