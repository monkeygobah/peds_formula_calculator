import tkinter as tk
from tkinter import ttk

def calculate_goal_feed():
    # Get values from the entry fields
    age_input = age_entry.get()
    weight = float(weight_entry.get())
    formula_kcal_per_oz = int(formula_combobox.get())
    caloric_input = caloric_entry.get()

    # Determine caloric need based on age
    caloric_needs = {
        'p': (110, 150),
        '0-6': 120,
        '6-12': (90, 120),
        '12-24': (85, 90),
        '24-84': (60, 75),
        '84-216': (30, 60),
        '216+': (30, 35)
    }

    # Check if user specified caloric value
    if caloric_input:
        kcal_per_kg = float(caloric_input)
    else:
        age_category = convert_age_to_category(age_input)
        kcal_per_kg = get_caloric_need(age_category, caloric_needs)
        if not kcal_per_kg:
            result_label.config(text="Invalid age category!")
            return

    kcal_day = weight * kcal_per_kg
    ounces_per_day = kcal_day / formula_kcal_per_oz 
    goal_amount_oz_per_feed = ounces_per_day / 8

    result_label.config(text=f"Goal Amount Per Feed: {goal_amount_oz_per_feed:.2f} oz. q 3 hours")

def convert_age_to_category(age_input):
    if age_input.lower() == 'p':
        return 'p'
    else:
        age_in_months = float(age_input)
        if 0 <= age_in_months <= 6:
            return '0-6'
        elif 6 < age_in_months <= 12:
            return '6-12'
        elif 12 < age_in_months <= 24:
            return '12-24'
        elif 24 < age_in_months <= 84:
            return '24-84'
        elif 84 < age_in_months <= 216:
            return '84-216'
        else:
            return '216+'

def get_caloric_need(age_category, caloric_needs):
    if age_category in caloric_needs:
        need = caloric_needs[age_category]
        if isinstance(need, tuple):
            return sum(need) / 2
        return need
    return None

app = tk.Tk()
app.title("Feeding Calculator")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Age Input
age_label = ttk.Label(frame, text="Age (p or in months):")
age_label.grid(column=0, row=0, sticky=tk.W, pady=5)
age_entry = ttk.Entry(frame)
age_entry.grid(column=1, row=0, sticky=tk.W, pady=5)

# Weight Input
weight_label = ttk.Label(frame, text="Weight (in kg):")
weight_label.grid(column=0, row=1, sticky=tk.W, pady=5)
weight_entry = ttk.Entry(frame)
weight_entry.grid(column=1, row=1, sticky=tk.W, pady=5)

# Formula Input
formula_label = ttk.Label(frame, text="Formula (kcal/oz):")
formula_label.grid(column=0, row=2, sticky=tk.W, pady=5)
formula_combobox = ttk.Combobox(frame, values=["20", "30"])
formula_combobox.set("20")
formula_combobox.grid(column=1, row=2, sticky=tk.W, pady=5)

# Optional caloric need input
caloric_label = ttk.Label(frame, text="Caloric Need (optional):")
caloric_label.grid(column=0, row=3, sticky=tk.W, pady=5)
caloric_entry = ttk.Entry(frame)
caloric_entry.grid(column=1, row=3, sticky=tk.W, pady=5)

# Calculate button
calculate_btn = ttk.Button(frame, text="Calculate", command=calculate_goal_feed)
calculate_btn.grid(column=0, row=4, columnspan=2, pady=20)

# Result label
result_label = ttk.Label(frame, text="", font=("Arial", 12))
result_label.grid(column=0, row=5, columnspan=2, pady=10)

app.mainloop()
