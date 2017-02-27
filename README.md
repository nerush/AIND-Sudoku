# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: As constraint propagation is used per unit, we also apply naked twins strategy per unit, where unit may represent a column,
 a row, a 3x3 box or a diagonal. For each of the unit of the given Sudoku, the naked twins constraint is the same:
 for any found naked twin in the given unit, eliminate digits of the twin from the other peers' values. Having our naked twin
 strategy defined, we implement it in the naked_twins function, which is used by reduce_puzzle function along with the other
 strategies.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: In order to solve the diagonal Sudoku problem, we need to extend basic version of sudoku solver with two more diagonals.
   As we abstract units in unitlist variable, we can simply append unitlist with the two diagonals in order to support
   the diagonal Sudoku solver almost for free. Having our constraints defined, we apply three strategies (elimination,
   only choice and naked twins) until there is no progress in solving the Sudoku, and then we try to solve it recursively
   by applying DFS starting on one of the unfilled squares with the fewest possibilities until the puzzle gets finally solved,
   or return False if no solution exists.


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.
