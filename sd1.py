import tkinter as tk

def convert_temperature():
    original_unit = original_unit_var.get()
    temperature = float(temperature_entry.get())
    
    if original_unit == "Celsius":
        fahrenheit = (temperature * 9/5) + 32
        kelvin = temperature + 273.15
        result_text.set(f"{temperature} {original_unit} is equivalent to:\n{fahrenheit:.2f} Fahrenheit\n{kelvin:.2f} Kelvin")
    elif original_unit == "Fahrenheit":
        celsius = (temperature - 32) * 5/9
        kelvin = (temperature - 32) * 5/9 + 273.15
        result_text.set(f"{temperature} {original_unit} is equivalent to:\n{celsius:.2f} Celsius\n{kelvin:.2f} Kelvin")
    else:
        celsius = temperature - 273.15
        fahrenheit = (temperature - 273.15) * 9/5 + 32
        result_text.set(f"{temperature} {original_unit} is equivalent to:\n{celsius:.2f} Celsius\n{fahrenheit:.2f} Fahrenheit")

# Create the main window
root = tk.Tk()
root.title("Temperature Conversion")

# Create and set variables
original_unit_var = tk.StringVar()
result_text = tk.StringVar()

# Create labels
label1 = tk.Label(root, text="Enter the original temperature unit:")
label1.pack()

# Create a dropdown for selecting the original unit
unit_options = ["Celsius", "Fahrenheit", "Kelvin"]
original_unit_menu = tk.OptionMenu(root, original_unit_var, *unit_options)
original_unit_menu.pack()

# Create an entry field for temperature input
label2 = tk.Label(root, text="Enter the temperature value:")
label2.pack()
temperature_entry = tk.Entry(root)
temperature_entry.pack()

# Create a button to trigger conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

# Create a label to display the result
result_label = tk.Label(root, textvariable=result_text)
result_label.pack()

# Start the GUI event loop
root.mainloop()