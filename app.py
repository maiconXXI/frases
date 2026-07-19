from flask import Flask, render_template, jsonify
from database import obter_frase
import os

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
    porta = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=porta)