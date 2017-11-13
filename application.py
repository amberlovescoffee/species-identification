from flask import Flask
from flask import render_template

application = app = Flask(__name__)


@app.route('/')
def main():
    return render_template('base.html')


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