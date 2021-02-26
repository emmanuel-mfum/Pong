# Pong
Python program emulating the famous Pong game.

The Pong game is an arcade table tennis-themed game. 
The goal of this game is to score as much as possible against an opponent (on the same keyboard).

This game was built using Python and the Turtle Graphics GUI.

This project can be split into 8 parts

1. Create a Screen
2. Create and move a paddle
3. Create another paddle
4. Create the ball and make it move
5. Detect collision with the wall and name the ball bounce
6. Detect collision with the paddle
7. Detect when the paddle misses
8. Keep the score


Creating a Screen

That part was the easiest. Using the Screen class of the turtle module, I set up a black screen with a width of 800px and a height of 600px.


Creating and moving a paddle

To make a paddle, I made a Class named "Paddle" in paddle.py . This class is a subclass of the Turtle class.I set up the shape of the paddle as well as its dimensions in the constructor of the class. I also designed methodds in the same class in order to move a Paddle object by using methods from the Turtle class. The paddles will only be able to move in the y-axis only. I then created a Paddle object in the file "main.py"

Creating another paddle

Since it is the pong game, we need 2 paddles, so I made another paddle. I added a parameter to the constructor of the Paddle class, namely "position". This parameter corresponds to a tuple reprsenting the (x,y) starting position of a paddle. The tuple is then passed in as an argument.

Creating a ball and make it move

To create a ball, I made another class named "Ball". This class is also a subclass of the Turtle class. I set the shape of the ball to be a circle and its shape to be "white".
To make the ball move, I made a function in the class Ball, named move(). This method will make the ball go to another location on the screen ny increasing both its x and y coordinate. I also made two methods called bounce_x() and bounce_y() which reverses respectivey the course of the ball of the x-axis or the y-axis.

Detecting a collision with the wall

To detect such a collision, I included an if statement in the main.py file where I check if the y-coordinate of the ball goe beyond a certain limit (280 or -280). If it does go beyond, the ball will bounce and change its course on the y-axis.

Detecting a collision with a paddle

To detect such a collision, I included an if statement in the main.py file where I check if the distance between the ball and a paddle is less than a certain limit (50px) or if the ball x-coordinate goes beyond a certain limit on the x-axis (320 and -320). I do it for both left and right paddle.

Detecting when the paddle misses

To detect when the paddle misses, I check if the x-coordinate of the ball goes beyond a certain limit (380 or -380) for each paddle in the main.py file. If so, I reset the ball position on the screen and a point is awarded to the opposite side.

Keeping the score

To keep the score, I create a class called Scoreboard, which is also a subclass of the Turtle class. An instance of this class will display the score on the top of the screen annd update the score displayed everytime one of the two sides scores.

