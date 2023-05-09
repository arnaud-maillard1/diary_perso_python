#!/usr/bin/env python3

from flask import Flask, render_template


app = Flask(__name__)


articles = [
    {'name': 'ballon', 'variantes': [
        {'name': 'foot', 'price': 10}, {'name': 'volley', 'price': 15}]},
    {'name': 'raquette', 'variantes': [
        {'name': 'tennis', 'price': 20}, {'name': 'badminton', 'price': 25}]},
    {'name': 'chaussures', 'variantes': [
        {'name': 'rouge', 'price': 30}, {'name': 'bleu', 'price': 35}, {'name': 'vert', 'price': 40}]}
]
# Render the template


@app.route('/')
def index():
    return render_template('market_template.html', marketName="Loulou sport", articles=articles)


if __name__ == '__main__':
    app.run(debug=True)
