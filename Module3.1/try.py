import tkinter as tk
import os
import subprocess
def userchoice():
    try:
        choice = int(entry.get())
        if choice == 1:
            result_label.config(text="You have chosen option 1. Please enter the country name.")
            # Disable the entry widget temporarily until the country name is entered
            entry.config(state=tk.DISABLED)
            country_entry.config(state=tk.NORMAL)
            country_button.config(state=tk.NORMAL)
            back_button.config(state=tk.DISABLED)
        elif choice == 2:
            result_label.config(text="You have chosen option 2")
        else:
            result_label.config(text="Please enter a valid choice")
    except ValueError:
        result_label.config(text="Please enter a valid choice.")


def process_country():
    country = country_entry.get().strip().lower()
    country = country[0].upper() + country[1:]
    with open('./A/country.txt', 'w') as f:
        f.write(country)
    fields_label.config(text="Enter the number of fields you want to see:")
    country_entry.config(state=tk.DISABLED)
    country_button.config(state=tk.DISABLED)
    fields_entry.config(state=tk.NORMAL)
    fields_button.config(state=tk.NORMAL)
    back_button.config(state=tk.DISABLED) 


def display_fields():
    n = int(fields_entry.get())
    fields_label.config(text="Enter field names one by one:")
    fields_entry.config(state=tk.DISABLED)
    fields_button.config(state=tk.DISABLED)
    
    # Create all the field entry widgets
    for i in range(n):
        field_entry = tk.Entry(root)
        field_entry.pack()
        fields_list.append(field_entry)
    
    # Enable the submit button after all fields have been entered
    submit_button.config(state=tk.NORMAL)
    back_button.config(state=tk.NORMAL)

def submit_fields():
    field_names = [field_entry.get() for field_entry in fields_list]
    confirmation_label.config(text=f"Fields entered: {', '.join(field_names)}")
    print(field_names)
    with open('./A/fields.txt', 'w') as f:
        for field in field_names:
            f.write(field + '\n')

    try:
        result = subprocess.run(['make', '-C', './A'], capture_output=True, text=True)
        os_output_label.config(text=f"Make command result: {result.stdout}")
    except Exception as e:
        os_output_label.config(text=f"Error executing make command: {e}")

    try :
        result = subprocess.run(['cat', './A/output_1.txt'], capture_output=True, text=True)
        os_output_label.config(text=f"Output: {result.stdout}")
    except Exception as e:
        os_output_label.config(text=f"Error executing cat command: {e}")



def go_back_to_menu():
# Reset the GUI to its initial state
    entry.config(state=tk.NORMAL)
    entry.delete(0, tk.END)
    country_entry.delete(0, tk.END)
    fields_entry.delete(0, tk.END)
    result_label.config(text="")
    fields_label.config(text="")
    confirmation_label.config(text="")
    os_output_label.config(text="")
    for widget in fields_list:
        widget.destroy()
    fields_list.clear()
    country_button.config(state=tk.DISABLED)
    fields_button.config(state=tk.DISABLED)
    submit_button.config(state=tk.DISABLED)
    back_button.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("CL LAB PROJECT")

# Create an entry widget to get user input
entry = tk.Entry(root)
entry.pack()

# Display text
text = tk.Label(root, text="1. Show the details of statistics of a country and the world's percentage")
text.pack()
text = tk.Label(root, text="2. Show the details of statistics of a country over a specified period of time")
text.pack()

# create a button to take user input of 1 or 2
button = tk.Button(root, text="Enter your choice", command=userchoice)
button.pack()

# Create a label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Country entry and button
country_entry = tk.Entry(root)
country_entry.pack()
country_button = tk.Button(root, text="Enter", command=process_country)
country_button.pack()
country_entry.config(state=tk.DISABLED)
country_button.config(state=tk.DISABLED)

# Fields entry and button
fields_label = tk.Label(root, text="")
fields_label.pack()
fields_entry = tk.Entry(root)
fields_entry.pack()
fields_button = tk.Button(root, text="Enter", command=display_fields)
fields_button.pack()
fields_entry.config(state=tk.DISABLED)
fields_button.config(state=tk.DISABLED)

# Create a button to submit fields
submit_button = tk.Button(root, text="Submit", command=submit_fields)
submit_button.pack()
submit_button.config(state=tk.DISABLED)

# Confirmation label
confirmation_label = tk.Label(root, text="")
confirmation_label.pack()


# Label to display the output of os.system('make -C ./A')
os_output_label = tk.Label(root, text="")
os_output_label.pack()


# Create a button to go back to the menu
back_button = tk.Button(root, text="Go back to menu", command=go_back_to_menu)
back_button.pack()
# List to store field entries
fields_list = []

# Run the application
root.mainloop()
