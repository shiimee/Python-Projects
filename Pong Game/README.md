# Pong Game

A two-player version of classic Pong written with Python's built-in `turtle` module. Two players share one keyboard and each moves a paddle to bounce the ball back. The ball speeds up after every paddle hit, and the first player to reach 3 points wins. It was built as practice in object-oriented Python and simple game loops.

## Features

- Two players on one keyboard
- The ball speeds up after each paddle hit and resets to normal speed after a point
- Dashed center line and a large score display
- First to 3 points wins, and the game announces the winner

## Tech stack

- Python 3
- Standard library only: `turtle` (built on Tkinter) and `time`

## Setup and run

You need Python 3 with Tkinter, which the python.org installers include. On Debian/Ubuntu, install it with `sudo apt install python3-tk`.

```bash
cd "Pong Game"
python3 main.py
```

When the game ends, click the window to close it.

## Example usage

| Player | Up | Down |
|--------|----|------|
| Left   | `W` | `S` |
| Right  | `↑` | `↓` |

A player scores when the ball gets past the opposing paddle. The first player to 3 points sees "Left Player Wins!" or "Right Player Wins!".

## Files

- `main.py`: sets up the screen, key bindings, game loop and collision checks
- `ball.py`: ball movement, bouncing and speed-up
- `paddle.py`: paddle shape and movement
- `scoreboard.py`: score display and the winner message
- `matchline.py`: draws the dashed center line
