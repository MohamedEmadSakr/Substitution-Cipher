import tkinter as tk
from tkinter import font
from tkinter import scrolledtext
import string
from collections import Counter

def decrypt(text, s):
    result = ""

    # Traverse text
    for i in range(len(text)):
        char = text[i]

        # Skip non-alphabetic characters (including spaces)
        if not char.isalpha():
            result += char
            continue

        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Decrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result

def brute_force_decrypt(ciphertext):
    decrypted_texts = []

    # Perform frequency analysis on the ciphertext
    frequencies = Counter(ciphertext.lower())
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    most_common = ''.join([freq[0] for freq in sorted_frequencies if freq[0] in string.ascii_lowercase])
    common_letters = 'etaoinshrdlcumwfgypbvkjxqz'

    # Try all possible shift values (0 to 25)
    for s in range(26):
        decrypted = decrypt(ciphertext, s)
        decrypted_texts.append(decrypted)

    # Sort decrypted texts based on letter frequency similarity
    decrypted_texts = sorted(decrypted_texts, key=lambda x: sum(c.lower() in most_common for c in x), reverse=True)

    return decrypted_texts

def on_entry_click(event):
    if entry.get() == "Enter your message here":
        entry.delete(0, tk.END)  # Clear the placeholder text
        entry.configure(fg="#000000")  # Set text color to black

def on_focusout(event):
    if entry.get() == "":
        entry.insert(tk.END, "Enter your message here")  # Restore the placeholder text
        entry.configure(fg="#808080")  # Set text color to light gray

def submit():
    text = entry.get()  # Retrieve text from the entry box
    result_text.delete('1.0', tk.END)  # Clear the existing text
    
    decrypted_texts = brute_force_decrypt(text)  # Perform decryption
    
    # Display the decrypted texts in the text box
    for decrypted in decrypted_texts:
        result_text.insert(tk.END, "Decrypted: " + decrypted + "\n")

# Create the main window
window = tk.Tk()
window.title("Text Input GUI")
window.geometry("600x500")
window.configure(bg="#f0f0f0")

# Create a custom font for labels
label_font = font.Font(family="Helvetica", size=14, weight="bold")

# Create a label for instructions
instruction_label = tk.Label(window, text="Substitution cipher", font=label_font, fg="#333333", bg="#f0f0f0")
instruction_label.pack(pady=10)

# Create an entry box for text input
entry = tk.Entry(window, font=label_font, bd=0, relief=tk.SOLID, width=66)
entry.insert(tk.END, "Enter your message here")  # Placeholder text
entry.configure(fg="#808080")  # Set text color to light gray

# Bind events to the entry box
entry.bind("<FocusIn>", on_entry_click)
entry.bind("<FocusOut>", on_focusout)

entry.pack(ipady=5, padx=20, pady=5)

# Create a submit button
submit_button = tk.Button(window, text="Decrypt", font=label_font, fg="#ffffff", bg="#4caf50", activebackground="#3b8f3b", relief=tk.FLAT, command=submit)
submit_button.pack(pady=10)

# Create a scrolled text box for displaying the result
result_text = scrolledtext.ScrolledText(window, height=30, width=80, font=("Helvetica", 12), bd=0, relief=tk.SOLID)
result_text.pack(padx=20, pady=10)

# Start the Tkinter event loop
window.mainloop()
#the input words: WKLV LV D QRWKLQJ PHVVDJHdw wkh krxu ri wkh oryhv
#WKLQJ LV WKH VKLUW LQ WKH HOGHUO\ndw zdb lw lv ylyhq wr pdnh pb idoo\ndw wkh krxu ri wkh oryhv\ndw wkh uxq ri wkh vwxglhv