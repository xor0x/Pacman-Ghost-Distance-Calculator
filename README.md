# # Pacman Ghost Distance Calculator

## Overview
This project implements a ghost distance calculator for a Pacman-like game board. It finds the shortest path distances from Pacman to all ghosts on the board using a Breadth-First Search (BFS) algorithm.

## Features
- Loads a game board from a .npy file
- Locates Pacman and ghosts on the board
- Calculates shortest path distances using BFS
- Returns a sorted list of ghost positions and their distances from Pacman

## Requirements
- Python 3.x
- NumPy library

## Installation
1. Clone this repository:

2. Install the required dependencies:
   ```
   pip install numpy
   ```

## Usage
Run the script from the command line, providing the path to your board file:

```
python main.py --board path/to/your/board.npy
```

For example:
```
python main.py --board C:\board3.npy
```
