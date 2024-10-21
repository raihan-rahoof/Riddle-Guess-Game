# Riddle Adventure Game

## Overview
This Python-based text adventure game challenges players with riddles, weapon choices, and strategic decisions across two exciting levels. The game demonstrates object-oriented programming principles and adheres to SOLID design principles for clean, maintainable code.

## How the Game Works

### Level 1
- The player starts with 3 lives.
- They must solve a randomly selected riddle.
- If successful, they choose a weapon from a set of 3.
- Finally, they must pick the correct key to open a door.
- Failing any step costs a life. The level is completed when all steps are successful.

### Level 2
- The player starts with 0 lives and can gain up to 3.
- They must fight a villain by choosing the correct weapon.
- If victorious, they face a final riddle.
- Solving the riddle wins the game.

## Features
- **Randomized riddles, weapons, and challenges** for high replayability.
- **Object-oriented design** with separate classes for game elements (Riddle, Weapon, Key).
- **Error handling** for user inputs.
- **Implementation of SOLID principles** for clean, efficient code.

## SOLID Principles Implementation

- **Single Responsibility Principle**: Each class has one job. For example, `RiddleRepository` is responsible only for managing riddles.
- **Open-Closed Principle**: New riddles, weapons, or keys can be added without modifying existing code.
- **Liskov Substitution Principle**: `LevelOne` and `LevelTwo` both inherit from the `Level` abstract base class and can be used interchangeably.
- **Interface Segregation Principle**: The `Level` abstract base class defines a minimal interface that concrete levels must implement.
- **Dependency Inversion Principle**: High-level modules (like `Game`) depend on abstractions (like `Level`), not concrete implementations.

## How to Run
1. Ensure you have Python 3.x installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Run the game using the command: 
   ```bash
   python game.py
