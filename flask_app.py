from flask import Flask, render_template
from flask import Response, make_response
import logging

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
	return render_template('index.html')

@app.route("/menu/")
def menu1_flask():
    return render_template('menu.html')


@app.route("/menu3/")
def menu3_flask():
    return render_template('menu3.html')

@app.route("/romance/")
def romance_flask():
    return render_template('romance.html')


@app.route("/action/")
def action_flask():
    return render_template('action.html')

@app.route("/horror/")
def horror_flask():
    return render_template('horror.html')

@app.route("/thriller/")
def thriller_flask():
    return render_template('thriller.html')

@app.route("/anime/")
def anime_flask():
    return render_template('anime.html')


@app.route("/drama/")
def drama_flask():
    return render_template('drama.html')


@app.route("/SF/")
def SF_flask():
    return render_template('SF.html')


@app.route("/criminal/")
def criminal_flask():
    return render_template('criminal.html')


@app.route("/fantasy/")
def fantasy_flask():
    return render_template('fantasy.html')


@app.route("/musical/")
def musical_flask():
    return render_template('musical.html')

@app.route("/adv/")
def adv_flask():
    return render_template('adv.html')

@app.route("/comedy/")
def comedy_flask():
    return render_template('comedy.html')

@app.route("/all/")
def all_flask():
    return render_template('all.html')


@app.route("/documentary/")
def documentary_flask():
    return render_template('documentary.html')


@app.route("/family/")
def adventure_flask():
    return render_template('family.html')

@app.route("/war/")
def war_flask():
    return render_template('war.html')

@app.route("/noir/")
def noir_flask():
    return render_template('noir.html')

@app.route("/mystery/")
def mystery_flask():
    return render_template('mystery.html')

if __name__ == '__main__':
    app.run(debug=True)