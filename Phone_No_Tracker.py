import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

def get_phone_info():
    mobileNo = entry.get()
    try:
        parsed_number = phonenumbers.parse(mobileNo)
        info_str = ""
        info_str += f"Is number valid: {phonenumbers.is_valid_number(parsed_number)}\n"
        info_str += f"Time Zone: {timezone.time_zones_for_number(parsed_number)}\n"
        info_str += f"Carrier Name: {carrier.name_for_number(parsed_number, 'en')}\n"
        info_str += f"Location: {geocoder.description_for_number(parsed_number, 'en')}\n"
        messagebox.showinfo("Phone Number Information", info_str)
    except phonenumbers.phonenumberutil.NumberParseException:
        messagebox.showerror("Error", "Invalid phone number format. Please try again.")

# Create main window
root = tk.Tk()
root.title("Phone Number Information Tool")

# Create labels and entry
label = tk.Label(root, text="Enter mobile number with country code:")
label.pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Create button
button = tk.Button(root, text="Get Information", command=get_phone_info)
button.pack(pady=5)

# Run the main event loop
root.mainloop()