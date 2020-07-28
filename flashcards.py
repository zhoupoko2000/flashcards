from flask import (Flask, render_template, abort, jsonify, request,
                   redirect, url_for)

from model import dbfoo, save_db, load_db, remove_db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        cards=load_db()
    )


@app.route('/card/<int:index>')
def card_view(index):
    try:
        card = load_db()[index]
        return render_template("card.html",
                               card=card,
                               index=index,
                               max_index=len(load_db())-1)
    except IndexError:
        abort(404)


@app.route('/add_card', methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        # form has been submitted, process data
        card = {"question": request.form['question'],
                "answer": request.form['answer']}

        save_db(card)
        return redirect(url_for('card_view', index=len(load_db())-1))
    else:
        return render_template("add_card.html")


@app.route('/remove_card/<int:index>', methods=["GET", "POST"])
def remove_card(index):
    try:
        if request.method == "POST":
            remove_db(load_db()[index])
            return redirect(url_for('welcome'))
        else:
            return render_template("remove_card.html", card=load_db()[index])
    except IndexError:
        abort(404)


@app.route("/api/card/")
def api_card_list():
    return jsonify(load_db())


@app.route("/api/card/<int:index>")
def api_card_detail(index):
    try:
        return load_db()[index]
    except IndexError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')