# Tic Tac Toe with AI Opponent

A web-based Tic Tac Toe game built with Flask, featuring an AI opponent with adjustable difficulty levels. The game allows players to choose between playing against another human or an AI opponent, with the option to select their preferred symbol (X or O) and difficulty level.

## Features

- **Two Game Modes**:
  - Player vs Player (PVP)
  - Player vs Computer (PVC)
- **Difficulty Levels**:
  - Easy: Computer has a 10% chance of making the optimal move
  - Hard: Computer always makes the best possible move using the Minimax algorithm
- **Interactive UI**:
  - Color-coded symbols (X in blue, O in red)
  - Celebratory animations for wins
  - "Computer is thinking..." animation during AI turns
- **Game Features**:
  - Real-time game state updates
  - Win/draw detection
  - Game reset functionality
  - Turn-based gameplay

## Technical Details

### AI Implementation

The computer opponent uses the Minimax algorithm with alpha-beta pruning to determine the best possible moves. The implementation includes:

- **Minimax Algorithm**: Recursively evaluates all possible game states to find the optimal move
- **Difficulty Levels**:
  - Hard Mode: Always chooses the best move using Minimax
  - Easy Mode: 10% chance of choosing the best move, 90% chance of choosing a random non-optimal move
- **First Move Optimization**: When playing as X, the computer always starts in the center position for optimal play

### Backend

- Built with Flask (Python)
- RESTful API endpoints for game moves and state management
- Real-time game state synchronization
- Error handling and input validation

### Frontend

- Responsive design using HTML, CSS, and JavaScript
- Dynamic UI updates without page reloads
- Smooth animations and transitions
- Mobile-friendly interface

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd tic-tac-toe
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## How to Play

1. Choose your game mode (Player vs Player or Player vs Computer)
2. If playing against the computer:
   - Select your preferred symbol (X or O)
   - Choose the difficulty level (Easy or Hard)
3. Take turns placing your symbol on the 3x3 grid
4. The first player to get three of their symbols in a row (horizontally, vertically, or diagonally) wins
5. If all squares are filled without a winner, the game is a draw
6. Click "Reset Game" to start a new game

## Project Structure

```
tic-tac-toe/
├── app.py              # Flask application and game logic
├── requirements.txt    # Python dependencies
├── static/            # Static files (CSS, JS, images)
│   └── style.css      # Stylesheet
└── templates/         # HTML templates
    └── index.html     # Main game interface
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE). 