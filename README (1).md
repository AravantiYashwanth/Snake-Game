
# Snake Game in Python

This is a simple implementation of the classic Snake game using Python's Turtle graphics module. The game features basic mechanics like moving the snake, eating food, growing the snake, and handling collisions with walls and the snake's own tail.

## Features

- **Snake Movement**: Control the snake using the arrow keys (Up, Down, Left, Right).
- **Food**: Eat food to grow the snake and increase your score.
- **Collision Detection**: The game detects collisions with walls and the snake's own tail, ending the game if either happens.
- **Scoreboard**: The score is displayed on the screen and updates every time the snake eats food.
- **Game Over**: If the snake hits the wall or its own tail, the game ends with a "Game Over" message.

## Requirements

- Python 3.x
- Turtle module (Usually comes pre-installed with Python)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/snake-game.git
   ```

2. Navigate to the project directory:

   ```bash
   cd snake-game
   ```

3. Run the `main.py` script:

   ```bash
   python main.py
   ```

## How to Play

1. When you start the game, press "OK" to begin.
2. Use the arrow keys to control the snake:
   - **Up Arrow**: Move Up
   - **Down Arrow**: Move Down
   - **Left Arrow**: Move Left
   - **Right Arrow**: Move Right
3. Eat food to grow the snake and increase your score.
4. The game ends when the snake hits the wall or its own tail.
5. Press "Space" to start a new game.

## Files

- `main.py`: The main script that runs the game.
- `snake.py`: Contains the `Snake` class that defines the snake's behavior.
- `food.py`: Contains the `Food` class that defines the behavior of the food.
- `scoreboard.py`: Contains the `Score` class for managing and displaying the score.

## Acknowledgments

- This project was created using the Python Turtle module.
- Inspired by the classic Snake game.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
