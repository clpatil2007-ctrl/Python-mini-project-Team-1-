import tkinter as tk
import turtle
import colorsys
from tkinter import Button,Label
from PIL import Image, ImageTk



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



    def BMI():
        import BMI
        BMI.main()


    def Ping_Pong():
        import Ping_Pong_game
        Ping_Pong_game.main()

    def Calci():
        import main
        main.calci_main()

    button4 = Button(root, font=('Areal', 27), bg='#90EE90', text='CALCULATOR', bd=5, command=Calci)
    button4.place(x=950, y=550)

    button1 = Button(root, font=('Areal', 28), bg='cyan', text='  NUMEROLOGY  ', bd=5, command=Num)
    button1.place(x=20, y=175)

    button2 = Button(root, font=('Areal', 30), bg='pink', text='  PING PONG  ', bd=5, command=Ping_Pong)
    button2.place(x=920, y=175)

    button3 = Button(root, font=('Areal', 24), bg='yellow', text=' BODY MASS INDEX ', bd=5, command=BMI)
    button3.place(x=20, y=550)
#Numerology
    try:
        # 1. Load the image using Pillow (Image.open)
        pil_image1 = Image.open("Numerology.png")

        # 2. RESIZE THE IMAGE: Change the size to 250x250 pixels
        # Use Image.Resampling.LANCZOS for high quality resizing
        pil_image1 = pil_image1.resize((340, 150), Image.Resampling.LANCZOS)

        # 3. Convert the PIL Image to a Tkinter PhotoImage object
        tk_image = ImageTk.PhotoImage(pil_image1)

        # 4. Store the reference globally
        tk_image_ref = tk_image

        # 5. Create the Label and display the image
        label = tk.Label(root, image=tk_image_ref)
        label.place(x=20, y=10)  # Adjusted placement for the new size/layout

    except FileNotFoundError:
        print("Error: Numerology.png not found. Please ensure the file is in the script directory.")
    except Exception as e:
        print(f"An error occurred with the image: {e}")
    # --- End Image Handling ---
#BMI
    try:
        pil_image2 = Image.open("BMI.png")

        pil_image2 = pil_image2.resize((340, 150), Image.Resampling.LANCZOS)

        tk_image1 = ImageTk.PhotoImage(pil_image2)

        # 4. Store the reference globally
        tk_image_ref1 = tk_image1

        label = tk.Label(root, image=tk_image_ref1)
        label.place(x=20, y=380)  # Adjusted placement for the new size/layout

    except FileNotFoundError:
        print("Error: BMI.png not found. Please ensure the file is in the script directory.")
    except Exception as e:
        print(f"An error occurred with the image: {e}")
    #Ping_pong
    try:

        pil_image3 = Image.open("Ping_pong.png")

        pil_image3 = pil_image3.resize((350, 150), Image.Resampling.LANCZOS)

        tk_image2 = ImageTk.PhotoImage(pil_image3)

        tk_image_ref2 = tk_image2

        label = tk.Label(root, image=tk_image_ref2)
        label.place(x=900, y=10)  # Adjusted placement for the new size/layout

    except FileNotFoundError:
        print("Error: Ping_pong.png not found. Please ensure the file is in the script directory.")
    except Exception as e:
        print(f"An error occurred with the image: {e}")

    #Calculator
    try:

        pil_image4 = Image.open("Calculator.png")

        pil_image4 = pil_image4.resize((320, 150), Image.Resampling.LANCZOS)

        tk_image3 = ImageTk.PhotoImage(pil_image4)

        tk_image_ref3 = tk_image3

        label = tk.Label(root, image=tk_image_ref3)
        label.place(x=930, y=380)  # Adjusted placement for the new size/layout

    except FileNotFoundError:
        print("Error: Calculator.png not found. Please ensure the file is in the script directory.")
    except Exception as e:
        print(f"An error occurred with the image: {e}")

    # 2. The main drawing loop
    while True:
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