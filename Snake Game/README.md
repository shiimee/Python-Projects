# Snake Game

The classic retro snake game, written with Python's built-in `turtle` module. Steer the snake to eat food and grow longer without hitting the walls or your own tail. Your best score is saved between sessions. It was built as practice in object-oriented Python and simple game loops.

## Features

- Arrow-key steering, and the snake can't reverse straight back into itself
- Food appears at a random spot, and each piece eats adds a point and a body segment
- Hitting a wall or the tail resets the round instead of closing the game
- The high score is saved in `data.txt`

## Tech stack

- Python 3
- Standard library only: `turtle` (built on Tkinter), `random` and `time`

## Setup and run

You need Python 3 with Tkinter, which the python.org installers include. On Debian/Ubuntu, install it with `sudo apt install python3-tk`.

Run the game from inside this folder, because it reads and writes `data.txt` in the current directory:

```bash
cd "Snake Game"
python3 main.py
```

## Example usage

- Steer with the arrow keys (`↑` `↓` `←` `→`).
- Eat the pink dots to score and grow.
- When you crash, your score goes back to 0. If you beat the high score, the new high score is saved.
- To reset the high score, set the number in `data.txt` to `0`.

## Files

- `main.py`: sets up the screen, key bindings, game loop and collision checks
- `snake.py`: the snake's body, movement, growth and reset
- `food.py`: places food at random spots
- `scoreboard.py`: shows the score and high score, and saves the high score
- `data.txt`: the stored high score
