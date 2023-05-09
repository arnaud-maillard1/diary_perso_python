#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader, select_autoescape

# Select environment
e = Environment(loader=FileSystemLoader(
    'templates/'), autoescape=select_autoescape())

# Get the html template
template = e.get_template('market_template.html')


articles = [
    {'name': 'ballon', 'variantes': [
        {'name': 'foot', 'price': 10}, {'name': 'volley', 'price': 15}]},
    {'name': 'raquette', 'variantes': [
        {'name': 'tennis', 'price': 20}, {'name': 'badminton', 'price': 25}]},
    {'name': 'chaussures', 'variantes': [
        {'name': 'rouge', 'price': 30}, {'name': 'bleu', 'price': 35}, {'name': 'vert', 'price': 40}]}
]
# Render the template
render = template.render(marketName='Loulou Sport',
                         articles=articles)

# Write the rendered template to a file
with open("market.html", "w") as fh:
    fh.write(render)
