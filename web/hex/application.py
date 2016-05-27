from flask import Flask, g, jsonify, render_template, request

import games_puzzles_algorithms.games.hex.game_state as game

app = Flask(__name__)
column_dimension = 12
row_dimension = 12
state = game.GameState.root(row_dimension, column_dimension)


@app.route('/_reset_game', methods=['GET'])
def reset_game():
    global state, row_dimension, column_dimension

    state = game.GameState.root(row_dimension, column_dimension)

    return jsonify(error=False, board=state.board._cells.tolist(),
                   row_dimension=row_dimension,
                   column_dimension=column_dimension)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()