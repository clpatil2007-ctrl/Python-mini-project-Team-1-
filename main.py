from tkinter import *
import math as m
import Calculator as m1

def calci_main():
    """Initializes and runs the Scientific Calculator window."""
    window = Toplevel(m1.root)
    window.geometry("400x600")
    window.config(bg="gray5")
    window.title("Scientific Calculator")
    window.resizable(False, False)

    # --- Tkinter Variables and Display ---
    entry_str = StringVar()
    entry = Entry(window, textvariable=entry_str, font=("Bohnschrift Semibold", 26),
                  foreground='white', bg='gray20', border=0, justify='right')
    entry.grid(columnspan=4, ipady=15, pady=20, padx=10, sticky="ew")
    def calculate():
        """
        Evaluates the expression in the entry field after replacing function names
        with math module calls.
        """
        nonlocal entry_str
        try:
            expression = entry_str.get()

            # --- Replacement Logic for math module functions ---
            # Replace user-friendly strings with 'm.' prefixed math functions
            expression = expression.replace("sin", "m.sin")
            expression = expression.replace("cos", "m.cos")
            expression = expression.replace("tan", "m.tan")
            expression = expression.replace("sqrt", "m.sqrt")
            # log() is mapped to log base 10 (log10)
            expression = expression.replace("log", "m.log10")
            # ln() is mapped to natural log (log)
            expression = expression.replace("ln", "m.log")
            expression = expression.replace("factorial", "m.factorial")
            expression = expression.replace("degrees", "m.degrees")
            expression = expression.replace("radians", "m.radians")
            expression = expression.replace("pi", "m.pi")
            expression = expression.replace("e", "m.e")

            # Use eval to calculate the result
            result = eval(expression)

            # Display the result
            entry_str.set(str(result))

        except Exception as e:
            # Handle math errors (e.g., log(0), sqrt(-1)) or syntax errors
            entry_str.set("Error")
            # print(f"Calculation Error: {e}") # Optional: for debugging

    # --- Button Definitions and Placement ---

    # Row 1: Trig and Sqrt
    btn_tan = Button(window, text="tan", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "tan("))
    btn_tan.grid(row=1, column=0, sticky="nsew", padx=1, pady=1)

    btn_sin = Button(window, text="sin", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "sin("))
    btn_sin.grid(row=1, column=1, sticky="nsew", padx=1, pady=1)

    btn_cos = Button(window, text="cos", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "cos("))
    btn_cos.grid(row=1, column=2, sticky="nsew", padx=1, pady=1)

    btn_sqrt = Button(window, text="√", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                      border=1, command=lambda: entry_str.set(entry_str.get() + "sqrt("))
    btn_sqrt.grid(row=1, column=3, sticky="nsew", padx=1, pady=1)

    # Row 2: Logs and Conversions
    btn_log = Button(window, text="log", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "log("))
    btn_log.grid(row=2, column=0, sticky="nsew", padx=1, pady=1)

    btn_ln = Button(window, text="ln", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                    border=1, command=lambda: entry_str.set(entry_str.get() + "ln("))
    btn_ln.grid(row=2, column=1, sticky="nsew", padx=1, pady=1)

    btn_deg = Button(window, text="deg", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "degrees("))
    btn_deg.grid(row=2, column=2, sticky="nsew", padx=1, pady=1)

    btn_rad = Button(window, text="rad", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "radians("))
    btn_rad.grid(row=2, column=3, sticky="nsew", padx=1, pady=1)

    # Row 3: Factorial, Power, Constants (e, pi)
    btn_fact = Button(window, text="x!", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                      border=1, command=lambda: entry_str.set(entry_str.get() + "factorial("))
    btn_fact.grid(row=3, column=0, sticky="nsew", padx=1, pady=1)

    btn_power = Button(window, text="xʸ", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                       border=1, command=lambda: entry_str.set(entry_str.get() + "**"))
    btn_power.grid(row=3, column=1, sticky="nsew", padx=1, pady=1)

    btn_e = Button(window, text="e", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                   border=1,
                   command=lambda: entry_str.set(entry_str.get() + "m.e"))  # Corrected: 'e' must be 'm.e' in entry
    btn_e.grid(row=3, column=2, sticky="nsew", padx=1, pady=1)

    btn_pi = Button(window, text="π", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                    border=1,
                    command=lambda: entry_str.set(entry_str.get() + "m.pi"))  # Corrected: 'pi' must be 'm.pi' in entry
    btn_pi.grid(row=3, column=3, sticky="nsew", padx=1, pady=1)

    # Row 4: Parentheses, Clear, Delete
    btn_par_open = Button(window, text="(", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                          border=1, command=lambda: entry_str.set(entry_str.get() + "("))
    btn_par_open.grid(row=4, column=0, sticky="nsew", padx=1, pady=1)

    btn_par_close = Button(window, text=")", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                           border=1, command=lambda: entry_str.set(entry_str.get() + ")"))
    btn_par_close.grid(row=4, column=1, sticky="nsew", padx=1, pady=1)

    btn_clear = Button(window, text="C", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                       border=1, command=lambda: entry_str.set(""))
    btn_clear.grid(row=4, column=2, sticky="nsew", padx=1, pady=1)

    btn_del = Button(window, text="DEL", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get()[:-1]))
    btn_del.grid(row=4, column=3, sticky="nsew", padx=1, pady=1)

    # Row 5: 7, 8, 9, Division
    btn_7 = Button(window, text="7", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "7"))
    btn_7.grid(row=5, column=0, sticky="nsew", padx=1, pady=1)

    btn_8 = Button(window, text="8", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "8"))
    btn_8.grid(row=5, column=1, sticky="nsew", padx=1, pady=1)

    btn_9 = Button(window, text="9", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "9"))
    btn_9.grid(row=5, column=2, sticky="nsew", padx=1, pady=1)

    btn_div = Button(window, text="÷", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "/"))
    btn_div.grid(row=5, column=3, sticky="nsew", padx=1, pady=1)

    # Row 6: 4, 5, 6, Multiplication
    btn_4 = Button(window, text="4", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "4"))
    btn_4.grid(row=6, column=0, sticky="nsew", padx=1, pady=1)

    btn_5 = Button(window, text="5", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "5"))
    btn_5.grid(row=6, column=1, sticky="nsew", padx=1, pady=1)

    btn_6 = Button(window, text="6", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "6"))
    btn_6.grid(row=6, column=2, sticky="nsew", padx=1, pady=1)

    btn_mul = Button(window, text="×", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "*"))
    btn_mul.grid(row=6, column=3, sticky="nsew", padx=1, pady=1)

    # Row 7: 1, 2, 3, Subtraction
    btn_1 = Button(window, text="1", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "1"))
    btn_1.grid(row=7, column=0, sticky="nsew", padx=1, pady=1)

    btn_2 = Button(window, text="2", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "2"))
    btn_2.grid(row=7, column=1, sticky="nsew", padx=1, pady=1)

    btn_3 = Button(window, text="3", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "3"))
    btn_3.grid(row=7, column=2, sticky="nsew", padx=1, pady=1)

    btn_sub = Button(window, text="−", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "-"))
    btn_sub.grid(row=7, column=3, sticky="nsew", padx=1, pady=1)

    # Row 8: Dot, 0, Equals, Addition
    btn_0 = Button(window, text="0", font=("Calibari", 18), bg="gray25", fg="white",
                   border=1, command=lambda: entry_str.set(entry_str.get() + "0"))
    btn_0.grid(row=8, column=1, sticky="nsew", padx=1, pady=1)

    btn_dot = Button(window, text=".", font=("Calibari", 18), bg="gray25", fg="white",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "."))
    btn_dot.grid(row=8, column=0, sticky="nsew", padx=1, pady=1)

    btn_eq = Button(window, text="=", font=("Calibari", 18), bg="DarkOrange1", fg="white",
                    # Changed = color for prominence
                    border=1, command=calculate)
    btn_eq.grid(row=8, column=2, sticky="nsew", padx=1, pady=1)

    btn_add = Button(window, text="+", font=("Calibari", 18), bg="gray30", fg="DarkOrange1",
                     border=1, command=lambda: entry_str.set(entry_str.get() + "+"))
    btn_add.grid(row=8, column=3, sticky="nsew", padx=1, pady=1)

    # --- Grid Weight Configuration ---
    # This ensures the buttons resize proportionally when the window size changes
    for i in range(1, 9):  # Start from row 1 (buttons)
        window.grid_rowconfigure(i, weight=1)
    for j in range(4):
        window.grid_columnconfigure(j, weight=1)