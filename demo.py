import tkinter as tk
import turtle
import colorsys
from tkinter import Button,Label


def draw_turtle_design(t, screen):
    screen.bgcolor('grey')
    t.speed(0)
    n = 70
    h = 0
    # Use a faster, non-blocking method for drawing the background
    t.penup()


    def Num():
        import Numerology
        Numerology.Num_main()

    def Calci():
        import main
        Calculator.calci_main()

    def BMI():
        import BMI
        BMI.main()


    def Ping_Pong():
        import Ping_Pong_game
        Ping_Pong_game.main()

    button1 = Button(root, font=('Areal', 28), bg='cyan', text='NUMEROLOGY ', bd=5, command=Num)
    button1.place(x=142, y=50)

    button3 = Button(root, font=('Areal', 30), bg='pink', text='  PING PONG  ', bd=5, command=Ping_Pong)
    button3.place(x=830, y=50)

    button4 = Button(root, font=('Areal', 27), bg='#90EE90', text='CALCULATOR', bd=5, command=Calci)
    button4.place(x=865, y=500)

    button2 = Button(root, font=('Areal', 29), bg='yellow', text='        BMI        ', bd=5, command=BMI)
    button2.place(x=142, y=500)


    # 2. The main drawing loop
    for i in range(360):
        # Calculate color
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 1 / n

        # Draw with the new color
        t.color(c)
        t.left(9)
        t.fd(1)

        # Ensure the pen is down for drawing the circles
        t.pendown()
        for j in range(2):
            t.left(2)
            t.circle(140)
        t.penup()
        # Lift the pen to not draw lines between complex steps

    # To avoid the turtle remaining visible, you can hide it after drawing
    t.hideturtle()


# --- Main Tkinter Application Setup ---
# 1. Create the main Tkinter root window
root = tk.Tk()
root.title("Multi Application Program!")
root.geometry("1400x800")
root.configure(background='#556B2F')#olive green

# 2. Create a Frame to hold the drawing area (optional, but good for layout)
frame = tk.Frame(root)
frame.pack()

# 3. Create the Tkinter Canvas
canvas_width = 1000
canvas_height = 720
canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height, bg="light gray")
canvas.pack()

# 4. Embed the TurtleScreen into the Tkinter Canvas
# This is the crucial step!
turtle_screen = turtle.TurtleScreen(canvas)

# 5. Create a Turtle object that draws on the embedded screen
my_turtle = turtle.RawTurtle(turtle_screen)

# 6. Execute the drawing function
# Note: Since the loop is very long (360 iterations), it will take time and
# block the main window. For smoother GUI, this drawing should be done
# in a separate thread or scheduled using `root.after()`.
# For simplicity, we run it directly here.
draw_turtle_design(my_turtle, turtle_screen)

# 7. Start the Tkinter event loop
root.mainloop()