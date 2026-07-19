from flask import Flask, render_template, jsonify
from database import obter_frase

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/sortear")
def sortear():

    texto, autor = obter_frase()

    return jsonify({
        "texto": texto,
        "autor": autor
    })

if __name__ == "__main__":
    app.run(debug=True)