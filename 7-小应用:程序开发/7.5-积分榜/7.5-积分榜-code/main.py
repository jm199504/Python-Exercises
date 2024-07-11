from flask import Flask, render_template, request


app = Flask(__name__)

players = ['玩家 1', '玩家 2', '玩家 3', '玩家 4']

rounds = 1


class Turn:
    def __init__(self, _round, first, second, third, fourth):
        self.round = _round
        self.first = int(first)
        self.second = int(second)
        self.third = int(third)
        self.fourth = int(fourth)


turns = []


@app.route('/', methods=['GET', 'POST'])
def scoreboard():
    global rounds
    if request.method == 'POST':
        result = request.form
        turns.append(Turn(rounds, result['1'], result['2'], result['3'], result['4']))
        rounds += 1
    sums = [sum(turn.first for turn in turns), sum(turn.second for turn in turns),
            sum(turn.third for turn in turns), sum(turn.fourth for turn in turns)]
    return render_template('scoreboard.html', players=players, turns=turns, sums=sums)


@app.route('/reset', methods=['POST'])
def reset():
    global rounds
    rounds, turns, sums = 0, [], []
    return render_template('scoreboard.html', players=players, turns=turns, sums=sums)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
