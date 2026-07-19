import sqlite3
import random

def obter_frase():

    conexao = sqlite3.connect("banco/frases.db")

    cursor = conexao.cursor()

    cursor.execute("SELECT texto, autor FROM frases")

    frases = cursor.fetchall()

    conexao.close()

    return random.choice(frases)