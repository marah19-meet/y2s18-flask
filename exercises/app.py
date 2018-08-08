from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
#def home_page():
   # return render_template("index.html")
def my_players_are():
    players=["cristiano ronaldo","messi","mo salah"]
    return render_template("index.html",players=players,likes_same_sport=False)




if __name__ == '__main__':
    app.run(debug = True)