import tkinter
from tkinter.constants import END
from tkinter import messagebox
from random import randint

tk = tkinter.Tk()
tk.title("Password Generator 1.0")
tk.iconbitmap("C:\PY\\passgen\p.ico")
tk.geometry("600x400")

def pw_rand():
        #Clear entry box on each execution
        pw_entry.delete(0, END)

        #Get password length and convert to int
        if my_entry.get().isdigit():
            pw_length = int(my_entry.get())
        else:
            messagebox.showerror("Error!", "Invalid input")

        #Create variable to hold password
        my_password = ''

        #Loop through password length
        for i in range(pw_length):
            my_password += chr(randint(33, 126))

        #Output password to screen
        pw_entry.insert(0, my_password)

#Create copy function
def clipper():
    #Clear clipboard   
    tk.clipboard_clear()
        
    #Copy to clipboard
    tk.clipboard_append(pw_entry.get())
    messagebox.showinfo("Success!", "Copied to clipboard")

#Create label frame & entry box for number of character
lf_entry = tkinter.LabelFrame(tk, text="How Many Characters?")
lf_entry.pack(pady=20)
my_entry = tkinter.Entry(lf_entry, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#Create label frame & entry box for returned password
lf_pw = tkinter.LabelFrame(tk, text="Your Password:")
lf_pw.pack(pady=20)
pw_entry = tkinter.Entry(lf_pw, text='', font=("Helvetica", 24))
pw_entry.pack(pady=20, padx=20)

#Create a frame for buttons
my_frame = tkinter.Frame(tk)
my_frame.pack(pady=20)

#Create buttons
my_button = tkinter.Button(my_frame, text="Generate Password", command=pw_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button = tkinter.Button(my_frame, text="Copy to clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

tk.mainloop()

