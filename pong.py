# Required modules
import turtle

# Window
window = turtle.Screen()
window.title('Pong')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

# Score
scoreA = 0
scoreB = 0

# Paddle A (left)
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B (right)
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
# Ball speed
ball.dx = 0.5
ball.dy = -0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0  Player B: 0', align='center',
          font=('Courier', 24, 'normal'))


def paddleAUP():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleADOWN():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleBUP():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleBDOWN():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Listening key presses
window.listen()
window.onkeypress(paddleAUP, 'w')
window.onkeypress(paddleADOWN, 's')

window.onkeypress(paddleBUP, 'Up')
window.onkeypress(paddleBDOWN, 'Down')

# Game loop
while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    elif ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write(f'Player A: {scoreA}  Player B: {scoreB}', align='center',
                  font=('Courier', 24, 'normal'))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(f'Player A: {scoreA}  Player B: {scoreB}', align='center',
                  font=('Courier', 24, 'normal'))

    # Paddle and ball collision detection
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1