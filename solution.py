assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    "Cross product of elements in A and elements in B."
    return [s + t for s in a for t in b]


boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
diagonals = [['A1','B2','C3','D4','E5','F6','G7','H8','I9'], ['I1','H2','G3','F4','E5','D6','C7','B8','A9']]
unitlist = row_units + column_units + square_units + diagonals
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def get_twins(unit):
    """Get list naked twins. Each naked twin is represented as a list of 2 boxes.
    """
    inverse = {}
    for k, v in unit.items():
        inverse[v] = inverse.get(v, [])
        inverse[v].append(k)
    twins = [k for v, k in inverse.items() if len(k) == 2]
    return twins


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    for unit in unitlist:
        filtered = {k:values[k] for k in unit if len(values[k]) == 2}
        twins = get_twins(filtered)
        for twin in twins:
            candidates = [u for u in unit if u not in twin]
            if len(candidates) > 0:
                for t in twin:
                    for c in candidates:
                        new_value = ''.join(sorted(set(values[c]) - set(values[t])))
                        values[c] = new_value
    return values


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    init = lambda c: '123456789' if c == '.' else c
    return dict(zip(boxes, map(init, grid)))


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print


def eliminate(values):
    filtered = {k: v for k, v in values.items() if len(v) == 1}
    for key, value in filtered.items():
        for peer in peers[key]:
            values[peer] = values[peer].replace(value, '')
    return values


def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        # Check how many boxes have a determined value
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])

        # Your code here: Use the Eliminate Strategy
        eliminate(values)
        # Your code here: Use the Only Choice Strategy
        only_choice(values)
        # Check how many boxes have a determined value, to compare
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        # If no new values were added, stop the loop.
        stalled = solved_values_before == solved_values_after
        # Sanity check, return False if there is a box with zero available values:
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def search(values):
    result = reduce_puzzle(values)
    if result is False:
        return False
    if all(len(values[box]) == 1 for box in boxes):
        return values
    # Choose one of the unfilled squares with the fewest possibilities
    length, address = min((len(values[box]), box) for box in boxes if len(values[box]) > 1)
    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for possible_value in values[address]:
        new_sudoku = values.copy()
        new_sudoku[address] = possible_value
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    return search(grid_values(grid))


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments

        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
