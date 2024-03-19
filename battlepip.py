import random
import re

"""
CONSTANTS
"""
BOARD_SIZE = 6
PLAYER = "Player"
OPPONENT = "Opponent"

# create an empty game board
def create_board():
  return [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# display the game board
def display_board(board):
  print("Package Manager:")
  print("  " + " ".join(str(i) for i in range(1, BOARD_SIZE + 1)))
  for i, row in enumerate(board):
    print(str(i + 1) + " " + " ".join(row))

# includes placement on the board 
def validate_coordinate_alignment(start_x, start_y, end_x, end_y, size):
  """Validates coordinates, ensuring they are within bounds and correctly aligned"""
  if not (1 <= start_x <= BOARD_SIZE and 1 <= start_y <= BOARD_SIZE and
          1 <= end_x <= BOARD_SIZE and 1 <= end_y <= BOARD_SIZE):
    return False
  
  if start_x != end_x and start_y != end_y:
    return False  # Coordinates are not aligned

  if start_x == end_x and abs(start_y - end_y) != size - 1:
    return False # Coordinates are not the right distance apart

  if start_y == end_y and abs(start_x - end_x) != size - 1:
    return False # Coordinates are not the right distance apart

  return True  # Coordinates passed validation

def validate_coordinate_availability(x, y, size, board, direction):
  """Checks if a package placement at given coordinates is valid (no overlaps)."""
  for i in range(size):
    if direction == 'horizontal':
      if board[y][x + i] != ' ':
        return False
    else:  # 'vertical'
      if board[y + i][x] != ' ':
        return False
  return True

def validate_placement_input(coord_input):
    """Validates the format of coordinate input. Returns True if valid, False otherwise."""
    pattern = r"^\d+,\d+ \d+,\d+$"  # Matches 'x,y x,y'
    if not re.match(pattern, coord_input):
        return False
    return True
  
def validate_attack_input(attack_input):
    """Validates the format of attack input and ensures coordinates are within bounds."""
    pattern = r"^\d+,\d+$" 
    if not re.match(pattern, attack_input):
        return False

    x, y = map(int, attack_input.split(','))

    if not (0 < x < BOARD_SIZE and 0 < y < BOARD_SIZE):
        return False

    return True

def get_package_placement(pkg_name, size, board, coord_list):
  """Handles user input and validation for package placement."""
  while True:
    coord_input = input(f"Placing {pkg_name}... Enter start and end coordinates (x,y x,y): ")
    if not validate_placement_input(coord_input):
          print("Invalid input format. Please use the format 'x,y x,y'.")
          continue  # Skip to the next iteration of the loop without executing the rest of the code
    try:
      start, end = coord_input.split()
      start_y, start_x = map(int, start.split(','))
      end_y, end_x = map(int, end.split(','))
      # Validate coordinates
      if not validate_coordinate_alignment(start_x, start_y, end_x, end_y, size):
        raise ValueError("Coordinates are out of bounds or do not match the package size.")

      direction = 'horizontal' if start_x == end_x else 'vertical'

      # Check placement validity using the refactored function 
      if not validate_coordinate_availability(start_x - 1, start_y - 1, size, board, direction):
        raise ValueError("A package already exists in the specified location.")

      # Placement is valid, place the package using our new helper
      place_package(board, start_x, start_y, direction, size, coord_list)
      
      return board

    except ValueError as e:
      print(f"Invalid input: {e}. Please try again.")

# place the PC's packages on the board
def place_pc_packages(board, pc_pkgs, placed_pkg_coords):
  for pkg, size in pc_pkgs.items():
    while True: 
      coordinates = generate_random_coordinates(BOARD_SIZE, size)
      direction = random.choice(['horizontal', 'vertical'])
      start_x, start_y = coordinates

      if validate_coordinate_availability(start_x - 1, start_y - 1, size, board, direction):
        place_package(board, *coordinates, direction, size, placed_pkg_coords)
        break

  return board

def generate_random_coordinates(board_size, ship_size):
  """Generates random valid start coordinates for a ship."""
  while True:
    start_x = random.randint(1, board_size)
    start_y = random.randint(1, board_size)
    if ship_fits_within_bounds(start_x, start_y, ship_size, board_size):
        return start_x, start_y

def ship_fits_within_bounds(start_x, start_y, ship_size, board_size):
    """Checks if a ship fits entirely within the board boundaries."""
    end_x = start_x + ship_size - 1
    end_y = start_y + ship_size - 1
    return 1 <= end_x <= board_size and 1 <= end_y <= board_size

def place_package(board, start_x, start_y, direction, ship_size, placed_pkg_coords):
  """Places a ship on the board."""
  for i in range(ship_size):
    if direction == 'horizontal':
      board[start_y - 1][start_x - 1 + i] = 'P'
      placed_pkg_coords.append((start_x - 1 + i, start_y - 1))
    else:  # 'vertical'
      board[start_y - 1 + i][start_x - 1] = 'P' 
      placed_pkg_coords.append((start_x - 1, start_y - 1 + i))

# check if the coordinate input is a hit or miss
def check_request(x, y, opposing_board, turn_player_board):
  if opposing_board[y][x] != ' ':
    opposing_board[y][x] = 'X'
    turn_player_board[y][x] = 'X'
    return True
  else:
    opposing_board[y][x] = '?'
    turn_player_board[y][x] = '?'
    return False

# check for win condition
def check_for_win(opponent_remaining_pkgs, opponent_name):
  print(f"{opponent_name} has {opponent_remaining_pkgs} folders remaining.")
  if opponent_remaining_pkgs == 0:
    if opponent_name == OPPONENT:
        print("Congratulations, you hacked them all!")
    else:
        print("Oh no!! Your system crashed :(")
        print("GAME OVER")
    return True
  else:
    print("--------------------------")
    print(f"{opponent_name}'s turn!")
    return False
  
# Main game function
def play_battlepip():
  player_board = create_board()
  pc_board = create_board()
  
  # Player package placement 
  player_pkgs = {'P1': 3, 'P2': 2}
  placed_player_pkgs = [] # keep track of placed coordinates
  player_remaining = player_pkgs
  initial_folders = sum(player_pkgs.values())
  player_remaining = initial_folders
  print("Sizes:", ', '.join([f"{k}: {v}" for k, v in player_pkgs.items()]))
  for pkg, size in player_pkgs.items():
    player_board = get_package_placement(pkg, size, player_board, placed_player_pkgs)
    display_board(player_board)
  
  # PC package placement 
  pc_pkgs = player_pkgs.copy()
  placed_pc_pkgs = [] # keep track of placed coordinates
  pc_remaining = initial_folders
  place_pc_packages(pc_board, pc_pkgs, placed_pc_pkgs)
  
  print("Opponent has filed their packages.")
  print(placed_pc_pkgs)
  print("Let's start the game!")
  print("--------------------------")
  print("Your turn!")
  # Main game loop
  while True:
    # Player's turn
    display_board(player_board)
    while True:  # Input validation loop
            attack_input = input("Request x,y to hack a folder: ")
            if validate_attack_input(attack_input):
                break  # Valid input, exit the loop
            else:
                print(f"Invalid input format. Please use the format 'x,y' within bounds of '1,1' - '{BOARD_SIZE}, {BOARD_SIZE}'.")

    x, y = map(int, attack_input.split(','))
    if check_request(x - 1, y - 1, pc_board, player_board):
      print("Hit a package!")
      pc_remaining -= 1
      if check_for_win(pc_remaining, OPPONENT):
        break
    else:
      print("Response: 404.")

    # PC's turn
    random_x, random_y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
    while player_board[random_y][random_x] in ['X', '?']: # Prevent repeat guesses
      random_x, random_y = random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1)
     
    if check_request(random_x, random_y, player_board, pc_board):
      result = "hit your package :0"
      player_remaining -= 1
      if check_for_win(player_remaining, PLAYER):
        break
    else: 
      result = "returned 404"
    print(f"Opponent {result} at {random_x + 1},{random_y + 1}")
    

# Start the game
play_battlepip()
