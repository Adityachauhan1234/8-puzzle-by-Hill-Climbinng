class PuzzleSolver:
    def __init__(self, start_state, target_state):
        self.start_state = start_state
        self.target_state = target_state

    def find_adjacent_states(self, current_state):
        adjacent_states = []
        zero_position = current_state.index(0)  # Find the blank tile (represented by 0)
        row, col = divmod(zero_position, 3)  # Get row and column of the blank tile

        # Define possible movement directions (up, down, left, right)
        potential_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for move in potential_moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:  # Check if move is within bounds
                swap_position = new_row * 3 + new_col
                new_state = list(current_state)
                # Swap blank tile with the adjacent tile
                new_state[zero_position], new_state[swap_position] = new_state[swap_position], new_state[zero_position]
                adjacent_states.append(tuple(new_state))

        return adjacent_states

    def calculate_heuristic(self, state):
        """Calculate the Manhattan distance between the current state and the goal."""
        manhattan_distance = 0
        for tile_value in range(1, 9):
            current_index = state.index(tile_value)
            goal_index = self.target_state.index(tile_value)
            current_row, current_col = divmod(current_index, 3)
            goal_row, goal_col = divmod(goal_index, 3)
            manhattan_distance += abs(current_row - goal_row) + abs(current_col - goal_col)
        return manhattan_distance

    def solve_using_hill_climbing(self):
        current_state = tuple(self.start_state)
        print(f"Starting hill climbing from state: {current_state}")

        while True:
            possible_states = self.find_adjacent_states(current_state)
            best_next_state = None
            best_heuristic_value = self.calculate_heuristic(current_state)

            # Check all neighbors to find the one with the smallest heuristic
            for next_state in possible_states:
                heuristic_value = self.calculate_heuristic(next_state)
                if heuristic_value < best_heuristic_value:
                    best_heuristic_value = heuristic_value
                    best_next_state = next_state

            if best_next_state is None:
                # No better state found, local minimum reached
                print("No better moves available. Solution may be at a local minimum.")
                return current_state

            current_state = best_next_state
            print(f"Moving to state with better heuristic: {current_state}")

            if current_state == tuple(self.target_state):
                print("Goal state achieved successfully!")
                return current_state


def main():
    # Initial and goal configurations of the 8-puzzle
    start_state = [1, 2, 3, 4, 5, 6, 0, 7, 8]  # Random initial configuration
    target_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # The goal configuration

    solver = PuzzleSolver(start_state, target_state)
    final_state = solver.solve_using_hill_climbing()

    print("Final reached state:", final_state)


if __name__ == "__main__":
    main()
