import turtle
import time
import random

WIDTH, HEIGHT = 1000, 700
COLORS =['red','green','blue','orange','cyan','black','yellow','violet','brown','gray']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric.. Try Again!")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("Number of racers should be between 2 - 10")

def race(colors):
    turtles =create_turtles(colors)
    
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            x, y = racer.pos()
            if y >= HEIGHT //2 -10:
                return colors[turtles.index(racer)]
            
    
def create_turtles(colors):
    turtles =[]  # we dont know how many turtles we are going to have so we
    spacingx = WIDTH // (len(colors)+1)
    for idx, color in enumerate(colors):
        racer = turtle.Turtle() 
        racer.color(color)
        racer.shape('turtle')
        racer.left(90) 
        racer.penup()
        racer.setpos(-WIDTH//2 +(idx +1) * spacingx, -HEIGHT//2+ 20)
        racer.pendown()
        turtles.append(racer) 
        
    return turtles

    
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Aryush Python Turtle Racing")
    
    screen.cv._rootwindow.lift()
    screen.cv._rootwindow.attributes("-topmost", True)
    screen.cv._rootwindow.attributes("-topmost", False)

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is {winner} turtle")
time.sleep(5)

















# racer = turtle.Turtle()  #obj tya vako arrow banako
# racer.speed(1)# 0 -fastest, 10 -fast, 6-normal, 3-slow, 1-slowest
# racer.penup()#sang sangei move vako line harauxa
# racer.shape('turtle')
# racer.color('red')
# racer.forward(100) #angle(speed)
# racer.left(90)
# racer.forward(100)
# racer.pendown() #bicha mai aba line aauna thalxa
# racer.right(90)
# racer.backward(100)




