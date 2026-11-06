# Turtle Crossing Game

A road-crossing game in the style of Crossy Road, written with Python's built-in `turtle` module. Guide a turtle from the bottom of the screen to the top through lanes of randomly spawned cars. Each successful crossing raises the level and makes the traffic faster and denser. It was built as practice in object-oriented Python and simple game loops.

## Features

- Cars spawn at random, in random colors and lanes
- Each level adds car speed and makes cars spawn more often
- The current level and high score are shown on screen
- At game over, the level reached is saved to `data.txt` if it is a new high score

## Tech stack

- Python 3
- Standard library only: `turtle` (built on Tkinter), `random` and `time`

## Setup and run

You need Python 3 with Tkinter, which the python.org installers include. On Debian/Ubuntu, install it with `sudo apt install python3-tk`.

Run the game from inside this folder, because it reads and writes `data.txt` in the current directory:

```bash
cd "Turtle Crossing Game"
python3 main.py
```

When the game ends, click the window to close it.

## Example usage

- Press `↑` to move forward and `↓` to move back.
- Reach the top of the screen to go up a level. The turtle then returns to the start.
- If a car hits you, the game shows "GAME OVER".
- To reset the high score, set the number in `data.txt` to `0`.

## Files

- `main.py`: sets up the screen, key bindings, game loop and collision checks
- `player.py`: turtle movement and returning to the start
- `car_manager.py`: spawns cars, moves them, speeds them up and removes off-screen cars
- `scoreboard.py`: shows the level and high score, and saves the high score
- `data.txt`: the stored high score
