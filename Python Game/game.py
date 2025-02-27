import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Save From Red Game by Deepcore.Codes")
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Player Car
player_car = turtle.Turtle()
player_car.shape("square")
player_car.color("blue")
player_car.shapesize(stretch_wid=1, stretch_len=2)  # Make it look like a car
player_car.penup()
player_car.goto(0, -250)
player_car.speed(0)

# Obstacle Setup
obstacles = []

# Track Lines (create two lines to simulate a road)
def draw_road():
    road = turtle.Turtle()
    road.hideturtle()
    road.penup()
    road.color("white")
    road.width(3)
    
    road.goto(-350, 300)
    road.pendown()
    road.setheading(270)  # Heading downwards
    road.forward(600)

    road.penup()
    road.goto(350, 300)
    road.pendown()
    road.setheading(270)
    road.forward(600)
    
# Function to create obstacles
def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("red")
    obstacle.shapesize(stretch_wid=1, stretch_len=2)  # Looks like a car
    obstacle.penup()
    obstacle.speed(0)
    x = random.randint(-300, 300)
    y = random.randint(150, 300)
    obstacle.goto(x, y)
    obstacles.append(obstacle)

# Move the player car
def move_left():
    x = player_car.xcor()
    if x > -350:
        player_car.setx(x - 20)

def move_right():
    x = player_car.xcor()
    if x < 350:
        player_car.setx(x + 20)

# Move obstacles
def move_obstacles():
    global score
    for obstacle in obstacles:
        y = obstacle.ycor()
        y -= 10
        obstacle.sety(y)
        
        # If the obstacle reaches the bottom, reset it to the top
        if y < -300:
            obstacle.goto(random.randint(-300, 300), random.randint(150, 300))
            score += 1

# Detect collision with obstacles
def check_collision():
    global running
    for obstacle in obstacles:
        if player_car.distance(obstacle) < 20:
            running = False
            print(f"Game Over! Your score is {score}")

# Game Score
score = 0
running = True

# Keybindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Main game loop
def game_loop():
    global score, running
    draw_road()
    
    # Create initial obstacles
    for _ in range(5):
        create_obstacle()

    while running:
        screen.update()
        move_obstacles()
        check_collision()
        
        if running:
            time.sleep(0.1)  # Slow down the game loop for better control
    
    print("Game Over! Your final score is", score)
    screen.bye()

# Start the game loop
game_loop()
