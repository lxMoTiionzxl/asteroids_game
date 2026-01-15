# Asteroids Game

A classic Asteroids game implementation using Python and Pygame.

## Objective

The principal objective of this project is to practice working with a larger codebase, focusing on:
- **Project Structure**: Organizing code into logical modules and files.
- **Object-Oriented Programming (OOP)**: Using a class-based approach with inheritance and polymorphism to manage complex game logic.
- **Scalability**: Building a foundation that can handle many different game objects (Player, Asteroids, Shots) efficiently.

## Project Structure

The project is structured with several classes, each handling a specific part of the game:

- `main.py`: The entry point of the game. It handles the main loop, event processing, and drawing logic.
- `circleshape.py`: The base class for all circular game objects, handling position, velocity, and collision detection.
- `player.py`: Contains the `Player` class, which handles player movement, rotation, and shooting.
- `asteroid.py`: Defines the `Asteroid` class, including logic for splitting asteroids when hit.
- `asteroidField.py`: Manages the spawning and timing of asteroids appearing on the screen.
- `shot.py`: Handles the projectiles fired by the player.
- `constants.py`: A central file for game configuration like screen dimensions, speeds, and spawn rates.
- `logger.py`: Utility for logging game state and events.

## Features

- **Class-based Architecture**: Every game element is an instance of a specialized class.
- **Collision Detection**: Circle-based collision logic implemented in the base class.
- **Game Mechanics**: Includes player rotation, movement, shooting, and asteroid splitting.
- **Logging**: Captures game events and state transitions.

## Getting Started

### Prerequisites

- Python 3.x
- [Pygame](https://www.pygame.org/)

### Installation

You can use `pip` or `uv` to manage dependencies.

#### Using pip
1. Clone the repository.
2. Install the dependencies:
   ```bash
   pip install pygame==2.6.1
   ```

#### Using uv
If you have [uv](https://github.com/astral-sh/uv) installed:
```bash
uv sync
```

### Running the Game

#### Using Python
Execute the following command in the project root:
```bash
python main.py
```

#### Using uv
```bash
uv run main.py
```

## How to Play

- **Rotate**: Use your keyboard (A/D or Left/Right arrows) to rotate the ship.
- **Move**: Use W or Up arrow to move forward.
- **Shoot**: Use Spacebar to fire shots.
- **Goal**: Avoid colliding with asteroids and shoot them to clear the field.
