import tkinter as tk
from typing import Self
from forex_python.converter import CurrencyRates
import deschidere


class ConverterApp:

    def __init__(self, master):
        self.master = master
        self.master.title("Converter App")
        self.master.config(bg='#73d6ff')
        
        self.create_currency_converter()
        self.create_memory_converter()
        self.create_physics_converter()
        back_button = tk.Button(master, text="EXIT",bg="#FF0000", command=exit,)
        back_button.grid(row=1, column=2,pady=10)

    def create_currency_converter(self):
        currency_frame = tk.Frame(self.master,bd =2, relief=tk.RIDGE,bg='#39A388')
        currency_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        currency_label = tk.Label(currency_frame, text="Currency Converter", font=("Calibri", 16, "bold"),bg='#39A388')
        currency_label.grid(row=0, column=0, columnspan=2, pady=10)
        #row1
        amount_label = tk.Label(currency_frame, text="Amount:", bg='#39A388')
        amount_label.grid(row=1, column=0, pady=5, padx=5, sticky=tk.E)
        self.amount_entry = tk.Entry(currency_frame)
        self.amount_entry.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)
        #row2
        from_currency_label = tk.Label(currency_frame, text="From Currency:",bg='#39A388')
        from_currency_label.grid(row=2, column=0, pady=5, padx=5, sticky=tk.E)

        c = CurrencyRates()
        available_currencies = list(c.get_rates("USD").keys())
        self.from_currency_var = tk.StringVar()

        self.from_currency_var.set("USD")  
        from_currency_menu = tk.OptionMenu(currency_frame, self.from_currency_var, *available_currencies)
        from_currency_menu.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)
        #row3
        to_currency_label = tk.Label(currency_frame, text="To Currency:",bg='#39A388')
        to_currency_label.grid(row=3, column=0, pady=5, padx=5, sticky=tk.E)
        self.to_currency_var = tk.StringVar()
        self.to_currency_var.set("EUR")  
        to_currency_menu = tk.OptionMenu(currency_frame, self.to_currency_var, *available_currencies)
        to_currency_menu.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)
        #row4
        convert_button = tk.Button(currency_frame, text="Convert", command=self.convert_currency, bg='#FFD700' )
        convert_button.grid(row=4, column=0, columnspan=2, pady=10)
        #output
        self.result_label_currency = tk.Label(currency_frame, text="")
        self.result_label_currency.grid(row=5, column=0, columnspan=2, pady=5)

    def create_memory_converter(self):
        memory_frame = tk.Frame(self.master, bd =2, relief=tk.RIDGE, bg='#6e82b7')
        memory_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        memory_label = tk.Label(memory_frame, text="Memory Converter", font=("Calibri", 16, "bold"),bg='#6e82b7')
        memory_label.grid(row=0, column=0, columnspan=2, pady=10)
        #row 1
        value_label = tk.Label(memory_frame, text="Value:",bg='#6e82b7')
        value_label.grid(row=1, column=0, pady=5, padx=5, sticky=tk.E)
        self.value_entry = tk.Entry(memory_frame)
        self.value_entry.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)
        from_base_label = tk.Label(memory_frame, text="From Base:",bg='#6e82b7')
        #row2
        from_base_label.grid(row=2, column=0, pady=5, padx=5, sticky=tk.E)
        self.from_base_var = tk.StringVar()
        self.from_base_var.set("Decimal")  
        from_base_menu = tk.OptionMenu(memory_frame, self.from_base_var, "Decimal", "Binary", "Hexadecimal")
        from_base_menu.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)
        #row3
        to_base_label = tk.Label(memory_frame, text="To Base:",bg='#6e82b7')
        to_base_label.grid(row=3, column=0, pady=5, padx=5, sticky=tk.E)
        self.to_base_var = tk.StringVar()
        self.to_base_var.set("Binary") 
        to_base_menu = tk.OptionMenu(memory_frame, self.to_base_var, "Decimal", "Binary", "Hexadecimal")
        to_base_menu.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)
        #row4
        convert_memory_button = tk.Button(memory_frame, text="Convert", bg='#f7e8d8', command=self.convert_memory)
        convert_memory_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.result_label_memory = tk.Label(memory_frame, text="")
        #output
        self.result_label_memory.grid(row=5, column=0, columnspan=2, pady=5)

    def create_physics_converter(self):
        physics_frame = tk.Frame(self.master, bd =2, relief=tk.RIDGE,bg='#95daf8')
        physics_frame.grid(row=0, column=2, padx=10, pady=10, sticky=tk.W)
        physics_label = tk.Label(physics_frame, text="Physics Converter", font=("Calibri", 16, "bold"),bg='#95daf8')
        physics_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        length_label = tk.Label(physics_frame, text="Length:",bg='#95daf8')
        length_label.grid(row=1, column=0, pady=5, padx=5, sticky=tk.E)
        self.length_entry = tk.Entry(physics_frame)
        self.length_entry.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)
        from_length_label = tk.Label(physics_frame, text="From:",bg='#95daf8')
        from_length_label.grid(row=2, column=0, pady=5, padx=5, sticky=tk.E)
        self.from_length_var = tk.StringVar()
        self.from_length_var.set("inch")  
        from_length_menu = tk.OptionMenu(physics_frame, self.from_length_var, "inch", "mils", "feet", "cm", "miles")
        from_length_menu.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)
        to_length_label = tk.Label(physics_frame, text="To:",bg='#95daf8')
        to_length_label.grid(row=3, column=0, pady=5, padx=5, sticky=tk.E)
        self.to_length_var = tk.StringVar()
        self.to_length_var.set("cm")  
        to_length_menu = tk.OptionMenu(physics_frame, self.to_length_var, "inch", "mils", "feet", "cm", "miles")
        to_length_menu.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)
        convert_length_button = tk.Button(physics_frame, text="Convert",bg='#73d6ff', command=self.convert_length)
        convert_length_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.result_label_length = tk.Label(physics_frame, text="")
        self.result_label_length.grid(row=5, column=0, columnspan=2, pady=5)

        volume_label = tk.Label(physics_frame, text="Volume:",bg='#95daf8')
        volume_label.grid(row=1, column=6, pady=15, padx=15, sticky=tk.E)
        self.volume_entry = tk.Entry(physics_frame)
        self.volume_entry.grid(row=1, column=7, pady=5, padx=5, sticky=tk.W)
        from_volume_label = tk.Label(physics_frame, text="From:",bg='#95daf8')
        from_volume_label.grid(row=2, column=6, pady=5, padx=5, sticky=tk.E)
        self.from_volume_var = tk.StringVar()
        self.from_volume_var.set("liters")  
        from_volume_menu = tk.OptionMenu(physics_frame, self.from_volume_var, "liters", "cubic meters", "US gallons", "UK gallons", "cups", "ounces")
        from_volume_menu.grid(row=2, column=7, pady=5, padx=5, sticky=tk.W)
        to_volume_label = tk.Label(physics_frame, text="To:",bg='#95daf8')
        to_volume_label.grid(row=3, column=6, pady=5, padx=5, sticky=tk.E)
        self.to_volume_var = tk.StringVar()
        self.to_volume_var.set("cubic meters")  
        to_volume_menu = tk.OptionMenu(physics_frame, self.to_volume_var, "liters", "cubic meters", "US gallons", "UK gallons", "cups", "ounces")
        to_volume_menu.grid(row=3, column=7, pady=5, padx=5, sticky=tk.W)
        convert_volume_button = tk.Button(physics_frame, text="Convert", bg='#73d6ff', command=self.convert_volume)
        convert_volume_button.grid(row=4, column=6, columnspan=2, pady=10)
        self.result_label_volume = tk.Label(physics_frame, text="")
        self.result_label_volume.grid(row=5, column=6, columnspan=2, pady=5)

        mass_label = tk.Label(physics_frame, text="Mass:",bg='#95daf8')
        mass_label.grid(row=1, column=3, pady=10, padx=10, sticky=tk.E)
        self.mass_entry = tk.Entry(physics_frame)
        self.mass_entry.grid(row=1, column=4, pady=5, padx=5, sticky=tk.W)
        from_mass_label = tk.Label(physics_frame, text="From:",bg='#95daf8')
        from_mass_label.grid(row=2, column=3, pady=5, padx=5, sticky=tk.E)
        self.from_mass_var = tk.StringVar()
        self.from_mass_var.set("kg")  
        from_mass_menu = tk.OptionMenu(physics_frame, self.from_mass_var, "kg", "carats", "lbs")
        from_mass_menu.grid(row=2, column=4, pady=5, padx=5, sticky=tk.W)
        to_mass_label = tk.Label(physics_frame, text="To:",bg='#95daf8')
        to_mass_label.grid(row=3, column=3, pady=5, padx=5, sticky=tk.E)
        self.to_mass_var = tk.StringVar()
        self.to_mass_var.set("carats")  
        to_mass_menu = tk.OptionMenu(physics_frame, self.to_mass_var, "kg", "carats", "lbs")
        to_mass_menu.grid(row=3, column=4, pady=5, padx=5, sticky=tk.W)
        convert_mass_button = tk.Button(physics_frame, text="Convert",bg='#73d6ff', command=self.convert_mass)
        convert_mass_button.grid(row=4, column=3, columnspan=2, pady=10)
        self.result_label_mass = tk.Label(physics_frame, text="")
        self.result_label_mass.grid(row=5, column=4, pady=5)
    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()
            c = CurrencyRates()
            rate = c.get_rate(from_currency, to_currency)
            converted_amount = round(amount * rate, 3)
            result_str = f"{amount} {from_currency} = {converted_amount} {to_currency}"
            self.result_label_currency.config(text=result_str)

        except ValueError:
            self.result_label_currency.config(text="Invalid input. Please enter a valid number.")
        except Exception as e:
            self.result_label_currency.config(text=f"Error fetching exchange rates: {str(e)}")

    def convert_memory(self):
        try:
            value = self.value_entry.get()
            from_base = self.from_base_var.get()
            to_base = self.to_base_var.get()

            if from_base == to_base:
                converted_value = value
            else:
                if from_base == "Decimal":
                    value = int(value)
                elif from_base == "Binary":
                    value = int(value, 2)
                elif from_base == "Hexadecimal":
                    value = int(value, 16)

                if to_base == "Decimal":
                    converted_value = str(value)
                elif to_base == "Binary":
                    converted_value = bin(value)
                elif to_base == "Hexadecimal":
                    converted_value = hex(value)

            result_str = f"{value} ({from_base}) = {converted_value} ({to_base})"
            self.result_label_memory.config(text=result_str)
        except ValueError:
            self.result_label_memory.config(text="Invalid input. Please enter a valid number or format.")

    def convert_length(self):
        try:
            entry = float(self.length_entry.get())
            from_unit = self.from_length_var.get()
            to_unit = self.to_length_var.get()

            conversion_factors = {
            ('inch', 'inch'): 1,
            ('inch', 'mils'): 1000,
            ('inch', 'feet'): 1/12,
            ('inch', 'cm'): 2.54,
            ('inch', 'miles'): 1/63360,

            ('mils', 'inch'): 0.001,
            ('mils', 'mils'): 1,
            ('mils', 'feet'): 0.001/12,
            ('mils', 'cm'): 0.001 * 2.54,
            ('mils', 'miles'): 0.001/63360,

            ('feet', 'inch'): 12,
            ('feet', 'mils'): 12*1000,
            ('feet', 'feet'): 1,
            ('feet', 'cm'): 30.48,
            ('feet', 'miles'): 1/5280,

            ('cm', 'inch'): 1/2.54,
            ('cm', 'mils'): 1/2.54 * 1000,
            ('cm', 'feet'): 1/30.48,
            ('cm', 'cm'): 1,
            ('cm', 'miles'): 1/160934.4,

            ('miles', 'inch'): 63360,
            ('miles', 'mils'): 63360*1000,
            ('miles', 'feet'): 5280,
            ('miles', 'cm'): 160934.4,
            ('miles', 'miles'): 1,
            }

            conversion_factor = conversion_factors[(from_unit, to_unit)]
            converted_value = round(entry * conversion_factor, 3)

            result_str = f"{entry} {from_unit} = {converted_value} {to_unit}"
            self.result_label_length.config(text=result_str)
        except ValueError:
            self.result_label_length.config(text="Invalid input. Please enter a valid number.")

    def convert_volume(self):
        try:
            volume = float(self.volume_entry.get())
            from_unit = self.from_volume_var.get()
            to_unit = self.to_volume_var.get()

            conversion_factors = {
            ('liters', 'liters'): 1,
            ('liters', 'cubic meters'): 0.001,
            ('liters', 'US gallons'): 0.264172,
            ('liters', 'UK gallons'): 0.219969,
            ('liters', 'cups'): 4.22675,
            ('liters', 'ounces'): 33.814,

            ('cubic meters', 'liters'): 1000,
            ('cubic meters', 'US gallons'): 264.172,
            ('cubic meters', 'UK gallons'): 219.969,
            ('cubic meters', 'cups'): 4226.75,
            ('cubic meters', 'ounces'): 33814,

            ('US gallons', 'liters'): 3.78541,
            ('US gallons', 'cubic meters'): 0.00378541,
            ('US gallons', 'UK gallons'): 0.832674,
            ('US gallons', 'cups'): 16,
            ('US gallons', 'ounces'): 128,

            ('UK gallons', 'liters'): 4.54609,
            ('UK gallons', 'cubic meters'): 0.00454609,
            ('UK gallons', 'US gallons'): 1.20095,
            ('UK gallons', 'cups'): 20,
            ('UK gallons', 'ounces'): 160,

            ('cups', 'liters'): 0.236588,
            ('cups', 'cubic meters'): 0.000236588,
            ('cups', 'US gallons'): 0.0625,
            ('cups', 'UK gallons'): 0.05,
            ('cups', 'ounces'): 8,

            ('ounces', 'liters'): 0.0295735,
            ('ounces', 'cubic meters'): 2.95735e-05,
            ('ounces', 'US gallons'): 0.0078125,
            ('ounces', 'UK gallons'): 0.00625,
            ('ounces', 'cups'): 0.125,
            }

            conversion_factor = conversion_factors[(from_unit, to_unit)]
            converted_value = round(volume * conversion_factor, 3)
            result_str = f"{volume} {from_unit} = {converted_value} {to_unit}"
            self.result_label_volume.config(text=result_str)

        except ValueError:
            self.result_label_volume.config(text="Invalid input. Please enter a valid number.")
    
    def convert_mass(self):
        try:
            mass = float(self.mass_entry.get())
            from_unit = self.from_mass_var.get()
            to_unit = self.to_mass_var.get()
            conversion_factors=({
            ('kg', 'kg'): 1,
            ('kg', 'carats'): 5000,
            ('kg', 'lbs'): 2.20462,

            ('carats', 'kg'): 0.0002,
            ('carats', 'carats'): 1,
            ('carats', 'lbs'): 0.000440925,

            ('lbs', 'kg'): 0.453592,
            ('lbs', 'carats'): 2267.96,
            ('lbs', 'lbs'): 1,
            })

            conversion_factor = conversion_factors[(from_unit, to_unit)]
            converted_value = round(mass * conversion_factor, 3)

            result_str = f"{mass} {from_unit} = {converted_value} {to_unit}"
            self.result_label_mass.config(text=result_str)
        except ValueError:
            self.result_label_mass.config(text="Invalid input. Please enter a valid number.")
    def exit():
        Self.master.destroy()

if __name__ == "__main__":
    app = ConverterApp(tk.Tk())
    app.master.mainloop()
