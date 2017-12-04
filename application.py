from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

application = app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('main'))


@app.route('/home')
def main():
    return render_template('main.html')


@app.route('/search_result')
def search_result():
    return "This is the search result page."


@app.route('/species')
def species():
    return "This is the species page."


@app.route('/all_classification')
def all_classification():
    return "This is all classification page."


@app.route('/order_classification')
def order_classification():
    return "This is order classification page."


if __name__ == '__main__':
    app.run(debug=True)