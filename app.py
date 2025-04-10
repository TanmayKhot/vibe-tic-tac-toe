from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Initialize game state
game_state = {
    'board': [''] * 9,
    'current_player': 'X',
    'game_over': False,
    'winner': None,
    'game_mode': None,
    'player_symbol': None,
    'difficulty': None
}

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != '':
            return board[i]
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != '':
            return board[i]
    
    # Check diagonals
    if board[0] == board[4] == board[8] != '':
        return board[0]
    if board[2] == board[4] == board[6] != '':
        return board[2]
    
    # Check for tie
    if '' not in board:
        return 'tie'
    
    return None

def get_empty_cells(board):
    return [i for i, cell in enumerate(board) if cell == '']

def minimax(board, depth, is_maximizing, player_symbol):
    computer_symbol = 'O' if player_symbol == 'X' else 'X'
    
    winner = check_winner(board)
    if winner:
        if winner == computer_symbol:
            return 10 - depth
        elif winner == player_symbol:
            return depth - 10
        else:
            return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for cell in get_empty_cells(board):
            board[cell] = computer_symbol
            score = minimax(board, depth + 1, False, player_symbol)
            board[cell] = ''
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for cell in get_empty_cells(board):
            board[cell] = player_symbol
            score = minimax(board, depth + 1, True, player_symbol)
            board[cell] = ''
            best_score = min(score, best_score)
        return best_score

def get_best_move(board, player_symbol):
    computer_symbol = 'O' if player_symbol == 'X' else 'X'
    best_score = float('-inf')
    best_move = None
    
    for cell in get_empty_cells(board):
        board[cell] = computer_symbol
        score = minimax(board, 0, False, player_symbol)
        board[cell] = ''
        
        if score > best_score:
            best_score = score
            best_move = cell
    
    return best_move

def get_random_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells) if empty_cells else None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/make_move', methods=['POST'])
def make_move():
    global game_state
    data = request.json
    position = int(data['position'])
    game_state['game_mode'] = data.get('game_mode')
    game_state['player_symbol'] = data.get('player_symbol')
    
    if game_state['board'][position] == '' and not game_state['game_over']:
        game_state['board'][position] = game_state['current_player']
        
        winner = check_winner(game_state['board'])
        if winner:
            game_state['game_over'] = True
            game_state['winner'] = winner
        else:
            game_state['current_player'] = 'O' if game_state['current_player'] == 'X' else 'X'
    
    return jsonify(game_state)

@app.route('/computer_move', methods=['POST'])
def computer_move():
    global game_state
    data = request.json
    game_state['board'] = data['board']
    game_state['player_symbol'] = data['player_symbol']
    game_state['current_player'] = 'O' if game_state['player_symbol'] == 'X' else 'X'
    difficulty = data.get('difficulty', 'hard')
    
    if not game_state['game_over']:
        # If it's the first move and computer is X, choose center for optimal play
        if game_state['board'].count('') == 9 and game_state['current_player'] == 'X':
            best_move = 4  # Center position
        else:
            if difficulty == 'easy':
                # Get the best move first
                best_move = get_best_move(game_state['board'], game_state['player_symbol'])
                # 10% chance to use the best move, 90% chance to use a random move
                if random.random() >= 0.1:  # 90% chance
                    # Get all empty cells except the best move
                    empty_cells = get_empty_cells(game_state['board'])
                    if best_move in empty_cells:
                        empty_cells.remove(best_move)
                    # Choose a random move from the remaining empty cells
                    best_move = random.choice(empty_cells) if empty_cells else best_move
            else:  # hard difficulty
                best_move = get_best_move(game_state['board'], game_state['player_symbol'])
            
        if best_move is not None:  # Only make a move if there's a valid position
            game_state['board'][best_move] = game_state['current_player']
            
            winner = check_winner(game_state['board'])
            if winner:
                game_state['game_over'] = True
                game_state['winner'] = winner
            else:
                game_state['current_player'] = game_state['player_symbol']
    
    return jsonify(game_state)

@app.route('/reset', methods=['POST'])
def reset():
    global game_state
    game_state = {
        'board': [''] * 9,
        'current_player': 'X',
        'game_over': False,
        'winner': None,
        'game_mode': game_state.get('game_mode'),
        'player_symbol': game_state.get('player_symbol'),
        'difficulty': game_state.get('difficulty')
    }
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True) 