from flask import Flask, render_template, request, jsonify, redirect
import static.xox as xox
import static.gtn as gtn
import time

d = xox.xox()
gtn=gtn.gtn()
msg = ["You won the Game", "You lost the Game", "Play Now", "Game Over, Tie!"]

app = Flask(__name__, template_folder="templates")


@app.route('/', methods=["GET"])
def home():
    return render_template("header.html")+render_template("main.html")+render_template("footer.html")


@app.route('/about', methods=["GET"])
def about():
    return render_template("header.html")+render_template("about.html")+render_template("footer.html")


@app.route('/xox', methods=['GET'])
def XOXGame():
    d.restart()
    return render_template("header.html")+render_template("xox.html")+render_template("footer.html")


@app.route('/xox', methods=['POST'])
def XOXGam():
    data = request.json
    cell_id = data['cell_id']
    if (cell_id == -1):
        d.restart()
    elif not d.isSpaceFree(d.data, cell_id):
        return "-1"
    else:
        d.change(cell_id, 'X')
        if d.isWinner(d.data, 'X') == True:
            return ''.join(d.data)+'1'
        if d.isBoardFull():
            return ''.join(d.data)+'0'
        d.change(d.getComputerMove(), 'O')
        if d.isWinner(d.data, 'O'):
            return ''.join(d.data)+'2'
    return ''.join(d.data)+'-1'

@app.route('/guessnumber', methods=['GET'])
def Game2():
    return render_template("header.html")+render_template("gtn.html")+render_template("footer.html")
@app.route('/guessnumber', methods=['POST'])
def Game2_():
    data = request.json
    gnumber=int(data['number'])
    if gnumber==-1:
        gtn.__init__()
        return ""
    print(gtn.number,gtn.count)
    return str(gtn.isWinner(gnumber))


if (__name__ == '__main__'):
    app.run()
