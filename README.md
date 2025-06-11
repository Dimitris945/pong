# pong
This is a simple implementation of the classic Pong game using Python and the Pygame library. The game features a player-controlled paddle, an AI opponent, a moving ball, and scoring system.

Features
Player paddle controlled via mouse movement
AI paddle that follows the ball with basic logic
Ball movement with collision detection
Scoring system displayed on the screen
Center net for visual effect
Requirements
Python 3.x
Pygame library
Installation
Make sure Python 3.x is installed on your system.
Install Pygame if not already installed:
 
pip install pygame
Usage
Save the game code in a file, for example pong.py.
Run the game using the command:
 
python pong.py
Controls
Move your mouse vertically to control the left paddle.
The right paddle (AI) moves automatically.
Gameplay
The goal is to score points by getting the ball past your opponent's paddle.
Each time the ball hits a paddle, it bounces back.
When the ball passes your paddle, the opponent scores a point.
The game continues indefinitely until you close the window.
Customization
You can modify the game parameters in the code, such as:

Paddle size (PADDLE_WIDTH, PADDLE_HEIGHT)
Ball speed (ball_vx, ball_vy)
Colors and fonts
License
This project is for educational purposes. Feel free to modify and expand it.

Acknowledgments
Based on Pygame library tutorials and examples.
Enjoy playing your Pong game!
