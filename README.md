# Python-OOP-Project-Aquarium

A terminal-based aquarium simulation built in Python using object-oriented design principles.

## Features
- Add and manage animals in a dynamic aquarium grid
- Simulate movement, feeding, aging, and death
- Collision detection between animals
- Menu-based user interface

## Animals
- **Molly / Scalar** — Fish that swim diagonally (horizontal + vertical movement)
- **Ocypode / Shrimp** — Crabs that walk along the ocean floor; reverse direction on collision

## Code Structure
- **Animal** — Abstract base class for all animals; handles food, age, movement, and death
- **Fish** — Extends Animal; adds vertical direction for diagonal swimming
- **Crab** — Extends Animal; horizontal movement only
- **Molly / Scalar** — Fish subclasses with unique ASCII representations
- **Ocypode / Shrimp** — Crab subclasses with unique ASCII representations
- **Aquarium** — Manages the grid, animal placement, movement simulation, and collision detection
- **Exceptions** — Custom exceptions for invalid input, placement conflicts, and aquarium size

## Requirements
Python 3.x — no external libraries needed

## Usage
```bash
python main.py
```

## Testing
```bash
python -m pytest test_Molly.py
```

## Authors
Bar Elhayani
Ben-Gurion University — Introduction to Computer Science Course
