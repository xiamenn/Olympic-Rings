# lab7_olympic.py
import turtle
import draw_USA_flag
import print_me_first

# Named constants
RADIUS = 40
RING_COLORS = ["blue", "black", "red", "yellow", "green"]
RING_POSITIONS = [(-100, 0), (0, 0), (100, 0), (-50, -50), (50, -50)]
PEN_WIDTH = 5
FONT_SIZE = 60
FONT_STYLE = ("Helvetica", FONT_SIZE, "bold")


def drawCircle(x, y, color):
    """
    Function name: drawCircle
    Function description: Draws a colored circle at specified coordinates
    @param x: x-coordinate for the circle
    @param y: y-coordinate for the circle
    @param color: color of the circle
    """
    turtle.hideturtle()
    turtle.pensize(PEN_WIDTH)
    turtle.pencolor(color)
    turtle.penup()
    turtle.goto(x, y - RADIUS)  # Position to start drawing the circle
    turtle.pendown()
    turtle.circle(RADIUS)
    turtle.penup()


def main():
    # Set up the screen
    screen = turtle.Screen()
    screen.title("USA Olympic Team")
    screen.bgpic("usa.png")  # Make sure usa.png is in the same directory

    # Draw USA flag
    draw_USA_flag.draw_USA_flag()

    # Write "USA OLYMPIC TEAM" at the top
    turtle.penup()
    turtle.goto(0, 250)
    turtle.pendown()
    turtle.color("blue")
    turtle.write("USA OLYMPIC TEAM", align="center", font=FONT_STYLE)
    turtle.penup()

    # Draw Olympic rings
    for i in range(5):
        drawCircle(RING_POSITIONS[i][0], RING_POSITIONS[i][1], RING_COLORS[i])

    # Print programmer info at bottom right
    turtle.goto(150, -250)
    info = print_me_first.print_me_first("Xianhang Meng", "Lab 7 - Olympic Rings")
    turtle.write(info, align="right")

    turtle.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    main()