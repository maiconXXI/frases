import sqlite3
import os

# Cria a pasta banco, se ela não existir
os.makedirs("banco", exist_ok=True)

# Conecta ao banco
conexao = sqlite3.connect("banco/frases.db")

cursor = conexao.cursor()

# Cria a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS frases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL,
    autor TEXT
)
""")

# Frases iniciais
frases = [
    ("Você pode mais do que acredita.", "Autor Desconhecido"),
    ("Você precisa enxergar todas as possibilidades e também as impossibilidades.", "Autor Desconhecido"),
    ("Concentre os esforços nos seus pensamentos.", "Autor Desconhecido"),
    ("Supere todas as ofensas. Acredite, os erros do ofensor são maiores que o seu.", "Autor Desconhecido"),
    ("Quem ofende, teme ser ofendido.", "Autor Desconhecido"),
    ("Se o ofensor usa a ofensa como arma, saiba que a ofensa o fere.", "Autor Desconhecido"),
    ("Se blinde e explore as vulnerabilidades do inimigo.", "Autor Desconhecido"),
    ("Leia sobre guerra, psicologia, filosofia e comportamento sociais.", "Autor Desconhecido"),
    ("Hoje é o dia. O presente é o mais importante.", "Autor Desconhecido"),
    ("Esforça-te.", "Autor Desconhecido"),
    ("Alimente-se de fundamentos.", "Autor Desconhecido"),
    ("Seja um monstro quando o assunto for superação.", "Autor Desconhecido"),
    ("Confie em você mesmo.", "Autor Desconhecido"),
    ("União é a chave.", "Autor Desconhecido"),
    ("Sempre, após superar um obstáculo, a visão se expande.", "Autor Desconhecido"),
    ("Busque superar tudo que vier pela frente.", "Autor Desconhecido"),
    ("O infortúnio pode fortalecer. Fortaleça-te.", "Autor Desconhecido"),
    ("A derrota é para quem desiste por definitivo.", "Autor Desconhecido"),
    ("Observe-se.", "Autor Desconhecido"),
    ("Aproprie-se do que é seu.", "Autor Desconhecido"),
    ("Faça bom uso do cérebro na hora certa. Esforça-te a pensar.", "Autor Desconhecido"),
    ("Suporte a tempestade e verá um oásis.", "Autor Desconhecido"),
    ("Se prepare para ser contrariado.", "Autor Desconhecido"),
    ("Ganhe o mundo. Use a mente. Esgote suas opções.", "Autor Desconhecido"),
    ("Se desafie. Caso seu inconsciente tente te sabotar, assuma o controle dos seus pensamentos e aplique-se à situação.", "Autor Desconhecido"),
    ("Ganhe.", "Autor Desconhecido"),
    ("Procure entender como é uma pessoa pelas coisas que ela fala.", "Autor Desconhecido"),
    ("Confie em você, confie no que você aprendeu e percebeu, veja por você mesmo.", "Autor Desconhecido"),
    ("Fortaleça-te para suportar todas as adversidades.", "Autor Desconhecido"),
    ("O seu bem maior é ter o controle sobre você mesmo.", "Autor Desconhecido"),
    ("É necessário que o fruto podre suma.", "Autor Desconhecido"),
    ("Planeje e siga, desfrute dos ganhos.", "Autor Desconhecido"),
    ("A inteligência consiste em reunir todo seu conhecimento e tomar a melhor decisão com base nisso.", "Autor Desconhecido"),
    ("Honre suas dores.", "Autor Desconhecido"),
    ("Estudando, você aprende além do que se quer aprender.", "Autor Desconhecido"),
    ("Valor ou boa sorte.", "Autor Desconhecido"),
    ("Não te esqueça da sua dor.", "Autor Desconhecido"),
    ("Trabalhe sua mente, liquide a parte que tenta te sabotar.", "Autor Desconhecido"),
    ("O cuidado deverá ser eterno, assim como os cálculos.", "Autor Desconhecido"),
    ("Além de atacar-te, os seus inimigos esperam uma chance para rir de ti.", "Autor Desconhecido"),
    ("Não vacile, não erre, torne-se bom e honrado.", "Autor Desconhecido"),
    ("Você nasceu.", "Autor Desconhecido"),
    ("Você já tem muitos inimigos, não seja você próprio o seu.", "Autor Desconhecido"),
    ("Esteja em harmonia com seus erros e acertos. Não erre.", "Autor Desconhecido"),
    ("Lide com a vida, já tem pessoas demais choramingando.", "Autor Desconhecido"),
    ("Não espere a paz, acostume-se com a guerra.", "Autor Desconhecido"),
    ("O poder sempre vai jogar na ferida, previna-se e ganhe.", "Autor Desconhecido"),
    ("A arte da guerra consiste na camuflagem e no engano.", "Autor Desconhecido"),
    ("Não há nada tão imortal que um homem não tenha vencido.", "Autor Desconhecido"),
    ("Se for errado não faça, principalmente quando houver testemunha.", "Autor Desconhecido"),
    ("Somos vulneráveis, mas somos a espécie dominante.", "Autor Desconhecido"),
    ("Que não parta dos outros afirmações para suas ideias, mas da razão.", "Autor Desconhecido"),
    ("Um homem forte é gerado pelas circunstâncias e não pelo tempo.", "Autor Desconhecido"),
    ("Um homem forte é reconhecido até pelo inimigo.", "Autor Desconhecido"),
    ("Quando estiver agindo certo e for contrariado por muitas pessoas, diga: estamos diante de um delírio coletivo.", "Autor Desconhecido"),

]

cursor.executemany(
    "INSERT INTO frases (texto, autor) VALUES (?, ?)",
    frases
)

conexao.commit()
conexao.close()

print("Banco criado com sucesso!")