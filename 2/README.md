# Cours 2

## Structure de données

- Scalaires :
  - Integers
  - Floats
  - Complex
  - Strings
  - Boolean
  - None
- Conteneurs []

  - Listes [] - `1` Dernirère valeur - `:1` Tout jusqu'à la dernière valeur - `2:-2`de la troisième valeur jusqu'à l'avant dernière
  - `::2` Le tableau par pas de 2 - si of fait `l = m` et qu'on ajoute une valeur à `l`, `m` est aussi modifié
  - n'est pas hashable
  - Possède un itérateur :

    ```python
    # list of vowels
    phones = ['apple', 'samsung', 'oneplus']
    phones_iter = iter(phones)
    print(next(phones_iter))
    print(next(phones_iter))
    print(next(phones_iter))
    # Output:
    # apple
    # samsung
    # oneplus
    ```

- Tuples () : liste non modifiable
  - Hashable (hash)
  - Possède un itérateur
  - Non modifiable
- Dictionnaires {}

  - {23: 'deux-trois'}
  - .items() : retourne les clés et les valeurs
  - .values() : retourne les valeurs
  - .keys() : retourne les clés
  - Problème : lent à parcourir
  - Les clés doivent être hashables (donc pas de listes comme clés)
  - Hash Table

    ```python
    >>> In [24]: e = {42 : 1, 'str' :2, (2+3j):3, 'None':4, (1,2,3): 6}

    >>> In [25]: f = {42 : 1, 'str' :2, (2+3j):3, 'None':4, [1,2,3]: 6}
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    Cell In [25], line 1
    ----> 1 f = {42 : 1, 'str' :2, (2+3j):3, 'None':4, [1,2,3]: 6}

    TypeError: unhashable type: 'list'
    ```

- Set {}

  - Dictionnaire sans valeur (que des clés)
  - Exemple :

    ```python
    In [27]: u = {1,2,3}

    In [28]: type(u)
    Out[28]: set
    ```

  - Rend les éléments uniques :

    ```python
    In [29]: l = [1,1,1,1,2,3,3,3,4,5,5,5,6]

    In [30]: set(l)
    Out[30]: {1, 2, 3, 4, 5, 6}
    ```

## Compréhension de liste

Fait un strip sur chaque élément d'une liste :

```python
[s.strip() for s in list]
```

Imagions que la liste vienne d'un fichier texte :

```python
f = open('file.txt', 'r')
[s.strip() for s in f.readlines()]
```

## Classes

### Méthodes "magiques"

- `__init__` : constructeur qui peut prendre des paramètres
- `__next__` : itérateur : retourne la valeur suivante d'une séquence
- `__iter__` : itérateur : retourne un itérateur sur une séquence

## Tips and tricks

- Pour effacer le terminal `ipython` : `clear` ou `ctrl + l`
- Pour envler les espaces et retour à la ligne d'une string : `strip()`
- Utiliser `random.choice()` pour choisir un élément aléatoire dans une liste
