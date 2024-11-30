## Simple Calculator

This is a **simple calculator** application built using Python's `Tkinter` library. It features a sleek **blue-themed UI** with dynamic button creation and basic error handling. The calculator allows basic mathematical operations such as addition, subtraction, multiplication, division, and more.

### Features:
- **Basic operations:** Addition, subtraction, multiplication, division, and percentage.
- **Clear functionality:** Clear the input screen with a `C` button.
- **Equals functionality:** Evaluate mathematical expressions using the `=` button.
- **Blue-themed UI:** A soothing blue color scheme applied to the buttons and screen.
- **Error handling:** Display "Error" if the user inputs an invalid expression.

---

### Installation:

1. Make sure Python 3.x is installed on your system.
2. The `Tkinter` library should come pre-installed with Python. If not, install it using the following command (for Linux-based systems):
   ```bash
   sudo apt-get install python3-tk
   ```

---

### Usage:

1. **Clone this repository** to your local machine.
   ```bash
   git clone https://github.com/your-username/simple-calculator.git
   ```

2. **Run the Python script**:
   ```bash
   python simple_calculator.py
   ```

3. The calculator window will open, and you can start performing calculations.

---

### Code Walkthrough:

1. **Creating the Window**:
   - We use `Tk()` to create the main window and set its dimensions (`400x600`).
   - The title is set to **"Simple Calculator"**.

2. **Input Screen**:
   - A `StringVar` (`scvalue`) holds the current expression to be evaluated.
   - The input screen is an `Entry` widget with a blue-themed background and dark blue text.

3. **Dynamic Button Creation**:
   - The `create_button` function creates buttons dynamically, using the button's text and background/foreground colors.
   - Buttons are assigned colors based on their types (number, operator, special, equals).

4. **Button Click Event**:
   - The `click(event)` function handles the user interaction with the buttons:
     - When `=` is pressed, the expression is evaluated using `eval()`.
     - If an error occurs, the screen displays "Error".
     - The `C` button clears the screen.
     - Other buttons append their text to the expression.

5. **Colors**:
   - Colors are applied to the buttons using a dictionary (`button_colors`) to distinguish between different types:
     - Numbers: Light blue background, dark blue text.
     - Operators: Medium blue background, dark text.
     - Special buttons (`C`, `=`): Bright blue background, white text.

---

### Screenshots:

![image](https://github.com/user-attachments/assets/1c33ac9d-8708-4e01-856e-b6c74f998bb7)
