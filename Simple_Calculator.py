from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            # Evaluate the expression in the screen
            value = eval(screen.get())
            scvalue.set(value)
        except Exception as e:
            # Handle any error and display 'Error' message
            scvalue.set("Error")
        screen.update()
                
    elif text == "C":
        # Clear the screen
        scvalue.set("")
        screen.update()
    
    else:
        # Append the button text to the screen value
        if scvalue.get() == "Error":
            scvalue.set("")  # Reset the screen if "Error" is present
        scvalue.set(scvalue.get() + text)
        screen.update()

# Create the main application window
root = Tk()
root.geometry("400x600")  # Adjusted size for better layout
root.title("Simple Calculator")

# Screen for displaying the result
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold", justify=RIGHT, bd=8, relief=SUNKEN, bg="#e6f7ff", fg="#00264d")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# Function to create buttons dynamically with colors
def create_button(frame, text, padx, pady, bg_color, fg_color):
    b = Button(frame, text=text, padx=padx, pady=pady, font="lucida 20 bold", relief=RAISED, bg=bg_color, fg=fg_color)
    b.pack(side=LEFT, padx=10, pady=5)
    b.bind("<Button-1>", click)
    return b

# Define button texts and colors
button_texts = [
    ["9", "8", "7", "C"],
    ["6", "5", "4", "/"],
    ["3", "2", "1", "*"],
    ["0", ".", "00", "-"],
    ["%", "=", "+", ""]
]

# Define colors for the blue theme
button_colors = {
    "number": {"bg": "#cceeff", "fg": "#00264d"},  # Light blue background, dark blue text
    "operator": {"bg": "#80d4ff", "fg": "#001a33"},  # Medium blue background, dark text
    "special": {"bg": "#3399ff", "fg": "#ffffff"},  # Bright blue background, white text
    "equals": {"bg": "#005c99", "fg": "#ffffff"}  # Deep blue background, white text
}

# Create the buttons with the blue theme
for row in button_texts:
    f = Frame(root, bg="#e6f7ff")  # Very light blue frame background
    for text in row:
        if text:  # Add only if text is not empty
            if text.isdigit() or text == "." or text == "00":
                colors = button_colors["number"]
            elif text in ["/", "*", "-", "+", "%"]:
                colors = button_colors["operator"]
            elif text == "=":
                colors = button_colors["equals"]
            else:  # "C" or other special buttons
                colors = button_colors["special"]
            
            create_button(f, text, 20, 20, colors["bg"], colors["fg"])
    f.pack()

root.mainloop()
