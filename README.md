# PLP Academy Python Assignment - Week 5

This repository contains the Python assignment for Week 5 of the PLP Academy. The focus of this assignment is to demonstrate **object-oriented programming (OOP)** concepts such as **inheritance**, **polymorphism**, and **encapsulation**.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [File Structure](#file-structure)
- [How to Run](#how-to-run)
- [Technologies Used](#technologies-used)
- [Author](#Author)

---

## Overview

The project includes a Python program that demonstrates OOP principles using a `Vehicle` class and its subclasses (`Car`, `Plane`, and `Boat`). Each subclass overrides the `move()` method to showcase **polymorphism**. The program also includes an example usage section to demonstrate how the classes interact.

---

## Features

- **Base Class**: `Vehicle` serves as the base class with a placeholder `move()` method.
- **Inheritance**: Subclasses (`Car`, `Plane`, `Boat`) inherit from the `Vehicle` class.
- **Polymorphism**: Each subclass implements its own version of the `move()` method.
- **Encapsulation**: Demonstrated through the structure of the classes.
- **Ease of Testing**: Includes a `unittest`-based test suite for validating functionality.

---

## File Structure

```
plp_academy-python_assignment_week_5/
│
├── vehicles.py         # Main Python file containing the Vehicle class and its subclasses
├── test_vehicles.py    # Unit tests for the Vehicle classes
├── README.md           # Project documentation
└── __pycache__/        # Auto-generated Python cache files (ignored in .gitignore)
```

---

## How to Run

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd plp_academy-python_assignment_week_5
   ```

2. **Run the Program**:
   Execute the `vehicles.py` file to see the polymorphism in action:
   ```bash
   python3 vehicles.py
   ```

   ### Expected Output:
   ```
   Driving 🚗
   Flying ✈️
   Sailing 🚤
   ```

---

## Technologies Used

- **Python 3.8+**: The programming language used for the assignment.

---

## Author

**Collins Orego**  
DevOps Enthusiast | Python Developer  
[GitHub Profile](https://github.com/Collins101-dev)