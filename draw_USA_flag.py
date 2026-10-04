# draw_USA_flag.py
import turtle


def draw_USA_flag():
    """
    Function name: draw_USA_flag
    Function description: Draws the USA flag using turtle graphics
    """
    # Create a screen
    screen = turtle.getscreen()
    screen.bgcolor("white")

    flag = turtle.Turtle()
    flag.speed(1000)
    flag.penup()
    flag.shape("turtle")

    # Flag dimensions
    flag_height = 250
    flag_width = 475

    # Starting points
    start_x = -237
    start_y = 125

    # Stripe dimensions
    stripe_height = flag_height / 13
    stripe_width = flag_width
    star_size = 10

    def draw_fill_rectangle(x, y, height, width, color):
        flag.goto(x, y)
        flag.pendown()
        flag.color(color)
        flag.begin_fill()
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
        flag.end_fill()
        flag.penup()

    def draw_star(x, y, color, length):
        flag.goto(x, y)
        flag.setheading(0)
        flag.pendown()
        flag.begin_fill()
        flag.color(color)
        for turn in range(0, 5):
            flag.forward(length)
            flag.right(144)
            flag.forward(length)
            flag.right(144)
        flag.end_fill()
        flag.penup()

    def draw_stripes():
        x = start_x
        y = start_y
        for stripe in range(0, 6):
            for color in ["red", "white"]:
                draw_fill_rectangle(x, y, stripe_height, stripe_width, color)
                y = y - stripe_height
        draw_fill_rectangle(x, y, stripe_height, stripe_width, 'red')
        y = y - stripe_height

    def draw_square():
        square_height = (7 / 13) * flag_height
        square_width = (0.76) * flag_height
        draw_fill_rectangle(start_x, start_y, square_height, square_width, 'navy')

    def draw_six_stars_rows():
        gap_between_stars = 30
        gap_between_lines = stripe_height + 6
        y = 112
        for row in range(0, 5):
            x = -222
            for star in range(0, 6):
                draw_star(x, y, 'white', star_size)
                x = x + gap_between_stars
            y = y - gap_between_lines

    def draw_five_stars_rows():
        gap_between_stars = 30
        gap_between_lines = stripe_height + 6
        y = 100
        for row in range(0, 4):
            x = -206
            for star in range(0, 5):
                draw_star(x, y, 'white', star_size)
                x = x + gap_between_stars
            y = y - gap_between_lines

    # Draw the flag components
    draw_stripes()
    draw_square()
    draw_six_stars_rows()
    draw_five_stars_rows()
    flag.hideturtle()