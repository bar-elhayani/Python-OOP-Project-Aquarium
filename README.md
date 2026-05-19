# Python-OOP-Project-Aquarium

# OOP Aquarium

A Python aquarium simulation demonstrating core object-oriented programming principles
through a hierarchy of marine animals living in a dynamic grid-based aquarium.

## Class Hierarchy
- **Animal** — Abstract base class defining shared behavior: food management, aging, movement, and death
- **Fish** — Extends Animal with vertical direction for diagonal swimming
- **Crab** — Extends Animal with horizontal-only movement
- **Molly / Scalar** — Concrete Fish subclasses with unique shapes and movement
- **Ocypode / Shrimp** — Concrete Crab subclasses that reverse direction on collision
- **Aquarium** — Manages the grid, animal placement, step simulation, and collision detection
- **Exceptions** — Custom exceptions for invalid input, placement conflicts, and size constraints

## OOP Concepts
- **Inheritance** — Multi-level hierarchy: Animal → Fish/Crab → specific animal types
- **Polymorphism** — Each animal implements its own `move()` and `get_animal()` behavior
- **Abstraction** — Animal and intermediate classes define abstract methods enforced in subclasses
- **Encapsulation** — Animal state (food, age, position) managed through dedicated methods

## Features
- Dynamic grid simulation with ASCII-rendered animals
- Collision detection between crabs with direction reversal
- Food, aging, and death mechanics per simulation step
- Custom exception handling for invalid operations

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
