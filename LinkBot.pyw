import random
import tkinter as tk
from tkinter import messagebox
import webbrowser

def generate_links():
    try:
        loop_range = int(entry.get())
        if loop_range <= 0:
            messagebox.showerror("Error", "Please enter a number greater than 0.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    base_link = base_url_entry.get()
    if "XXXX" not in base_link:
        messagebox.showerror("Error", "Base URL must contain 'XXXX' as a placeholder for the number.")
        return

    random_numbers = [random.randint(1, 3000) for _ in range(loop_range)]
    links = [base_link.replace("XXXX", str(num)) for num in random_numbers]
    link_text = "\n".join(links)
    text.config(state='normal')
    text.delete('1.0', tk.END)
    text.insert(tk.END, link_text)
    text.config(state='disabled')
    
    global all_links
    all_links = links

def open_links():
    if not all_links:
        return
    
    for link in all_links:
        webbrowser.open_new_tab(link)

def copy_links():
    if not all_links:
        return

    link_text = "\n".join(all_links)
    root.clipboard_clear()
    root.clipboard_append(link_text)
    messagebox.showinfo("Links Copied", "Links have been copied to clipboard.")

def clear_links():
    text.config(state='normal')
    text.delete('1.0', tk.END)
    text.config(state='disabled')
    global all_links
    all_links = []

def openfloppa():
    webbrowser.open_new_tab("https://bumble.pink")

root = tk.Tk()
root.geometry("1000x500")
root.title("LinkBot v1.1 by itsbumble")

bg_color = "#263238"  # Dark Blue Gray
fg_color = "#FFFFFF"  # White
button_bg_color = "#37474F"  # Darker Blue Gray

root.config(bg=bg_color)

# Spacing between left side and stack
spacing_frame = tk.Frame(root, width=20, bg=bg_color)
spacing_frame.pack(side=tk.LEFT, fill=tk.Y)

# Stack moved to the left with spacing
stack_frame = tk.Frame(root, bg=bg_color)
stack_frame.pack(side=tk.LEFT, fill=tk.Y)

# Entry for Base URL
base_url_label = tk.Label(stack_frame, text="enter base url:", bg=bg_color, fg=fg_color, font=("Helvetica", 12))
base_url_label.pack(pady=10)

base_url_entry = tk.Entry(stack_frame, width=30, bg=button_bg_color, fg=fg_color)
base_url_entry.pack(pady=5)
base_url_entry.insert(0, "https://example.com/XXXX.jpeg")  # Default value

# Entry for Number of Links
entry_label = tk.Label(stack_frame, text="enter number of links:", bg=bg_color, fg=fg_color, font=("Helvetica", 12))
entry_label.pack(pady=10)

entry = tk.Entry(stack_frame, width=10, bg=button_bg_color, fg=fg_color)
entry.pack(pady=5)

# Buttons
button_generate = tk.Button(stack_frame, text="generate links", command=generate_links, bg=button_bg_color, fg=fg_color, font=("Helvetica", 12))
button_generate.pack(pady=5)

button_open = tk.Button(stack_frame, text="open links in browser", command=open_links, bg=button_bg_color, fg=fg_color, font=("Helvetica", 12))
button_open.pack(pady=5)

button_copy = tk.Button(stack_frame, text="copy links", command=copy_links, bg=button_bg_color, fg=fg_color, font=("Helvetica", 12))
button_copy.pack(pady=5)

button_clear = tk.Button(stack_frame, text="clear links", command=clear_links, bg=button_bg_color, fg=fg_color, font=("Helvetica", 12))
button_clear.pack(pady=5)

button_creator = tk.Button(stack_frame, text="support me", command=openfloppa, bg=button_bg_color, fg=fg_color, font=("Helvetica", 12))
button_creator.pack(side=tk.BOTTOM, anchor=tk.SW, pady=10)

# Output Text Box
text_frame = tk.Frame(root, bg=bg_color)
text_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

text = tk.Text(text_frame, wrap=tk.WORD, font=("Helvetica", 12), bg=button_bg_color, fg=fg_color)
text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

all_links = []

root.mainloop()
