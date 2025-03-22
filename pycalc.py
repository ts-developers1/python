import tkinter as tk
BG_COLOR = "#2C3E50" 
BTN_COLOR = "#34495E"  
BTN_HOVER = "#1ABC9C"  
TEXT_COLOR = "#ECF0F1"  
FONT = ("Arial", 22, "bold")

def on_click(button_text):
    current = entry_var.get()
    if button_text == "=":
        try:
            result = str(eval(current))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current + button_text)


root = tk.Tk()
root.title("TS-Calculator")
root.geometry("400x500")
root.configure(bg=BG_COLOR)


entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=FONT, bg=BG_COLOR, fg=TEXT_COLOR, 
                 bd=10, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, pady=10)

# Buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack()

for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        btn = tk.Button(frame, text=button_text, font=FONT, width=5, height=2,
                        bg=BTN_COLOR, fg=TEXT_COLOR, relief="ridge",
                        activebackground=BTN_HOVER, activeforeground="black",
                        command=lambda b=button_text: on_click(b))
        btn.grid(row=i, column=j, padx=5, pady=5, sticky="nsew")


for i in range(4):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()
