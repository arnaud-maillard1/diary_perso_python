# Cours 11

- [ ] Jinja2
- [ ] Flask

## Exercice

Génrérer une page HTML à partir d'un template pour présenter les articles d'un magasin de sport.

1. Créer une template HTML
2. Y mettre des {{}}
3. Traiter une boucle for dans la template (articles)
4. Traiter une sous boucle for dans la template (variantes)

Un article a un nom et un prix.

Créer un fichier Python qui charge la template, et la remplit avec des données.

Avec Jinja :

```python
#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader, select_autoescape

# Select environment
e = Environment(loader=FileSystemLoader(
    'templates/'), autoescape=select_autoescape())

# Get the html template
template = e.get_template('market_template.html')

# articles = [
#     {'name': 'ballon', 'variantes': ['foot', 'volley']},
#     {'name': 'raquette', 'variantes': ['tennis', 'badminton']},
#     {'name': 'chaussures', 'variantes': ['rouge', 'bleu', 'vert']}
# ]

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
```

Avec Flask :

```python
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

```

Ca nous fourni une adresse IP sur laquelle on se rend et ça ne crée as de nouveau fichier `.html`.
