## 7.5-积分榜

### 问题描述

玩游戏：四位玩家需要记录每一轮得分，并且实时统计总分。


### 解答思路

（1）网页设计：设计一个大标题，一个表格，表格列名包含玩家名称，每一行记录每一轮的玩家得分，最后一行对目前的得分进行统计，在下方4个积分输入框，用于登记每一轮的玩家得分，另外提供“重制积分”的功能，可以支持新的一轮积分记录。

（2）应用设计

```html
costTable/  # 应用目录
-- templates  # 资源文件目录（通常包含html/css/js等）
  -- index.html
-- main.py  # 程序入口（Web后端代码）
```

（3）解答示例Python代码（`main.py`）

```python
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

```

（4）解答示例HTML代码（`index.html`）

```html
<!DOCTYPE html>
<html>
<head>
    <title>Scoreboard</title>
    <style>
        body {
            background-color: #F0F0F0;
            margin: 0;
            padding: 0;
            font-family: Arial, sans-serif;
        }

        #header {
            background-color: #333;
            color: white;
            padding: 20px;
            text-align: center;
        }

        #scoreboard {
            margin: 20px auto;
            max-width: 600px;
            background-color: white;
            padding: 20px;
            border-radius: 5px;
        }

        #scoreboard table {
            width: 100%;
            border-collapse: collapse;
        }

        #scoreboard th, #scoreboard td {
            padding: 10px;
            text-align: center;
            border-bottom: 1px solid #ddd;
        }

        #scoreboard th {
            background-color: #333;
            color: white;
        }

        #scoreboard tr.champion td {
            background-color: #FFD700;
        }

        .input-field {
            margin-bottom: 10px;
        }

        .reset-button {
            background-color: #CD9B1D;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-left: 40%;
        }

        .submit-button {
            background-color: #333;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            margin-left: 40%;
        }

        .reset-button:hover, .submit-button:hover {
            background-color: #555;
        }
    </style>
</head>
<body>
    <div id="header">
        <h1>积分榜</h1>
    </div>

    <div id="scoreboard">
        <form action="/" method="POST">
            <table>
                <tr>
                    <th>玩家名称</th>
                    {% for player in players %}
                        <th> {{ player }} </th>
                    {% endfor %}

                </tr>
                {% for turn in turns %}
                <tr>
                     <td>第{{ turn.round }}轮</td>
                     <td>{{ turn.first }}</td>
                     <td>{{ turn.second }}</td>
                     <td>{{ turn.third }}</td>
                     <td>{{ turn.fourth }}</td>
                </tr>
                {% endfor %}

                <tr>
                    <td>总计</td>
                    <td> {{ sums[0] }} </td>
                    <td> {{ sums[1] }} </td>
                    <td> {{ sums[2] }} </td>
                    <td> {{ sums[3] }} </td>
                </tr>

            </table>

            <hr>

            <div class="input-field">
                <label for="player1">玩家一:</label>
                <input type="number" id="player1" name="1" required>
            </div>

            <div class="input-field">
                <label for="player2">玩家二:</label>
                <input type="number" id="player2" name="2" required>
            </div>

            <div class="input-field">
                <label for="player3">玩家三:</label>
                <input type="number" id="player3" name="3" required>
            </div>

            <div class="input-field">
                <label for="player4">玩家四:</label>
                <input type="number" id="player4" name="4" required>
            </div>

            <button class="submit-button" type="submit">记录本次</button>
        </form>
        <hr>
        <form action="/reset" method="POST">
            <button class="reset-button" type="submit">重置积分</button>
        </form>
    </div>
</body>
</html>
```

（5）预览入口：

```html
127.0.0.1:5000
```