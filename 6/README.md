# Cours 6

## Named tuple

```python
from collections import namedtuple

Type = namedtuple('TypeName', ('field1', 'field2'))
t = Type('a', 'b')
t[0] # a
t.field1 # a
```

## Broadcasting

1. Définir un vecteur ligne de 5 éléments avec NumPy
2. Modifier ce vecteur en une matrice de 5x5 tel que chaque colonne corrrespond à la transposée du vecteur ligne

```python
v = 1 2 3
m = 1 1 1
    2 2 2
    3 3 3
```

Solution:

```ipython
In [1]: import numpy as np
In [48]: v = np.arange(1,6)
In [50]: u = np.ones(5)
In [58]: v
Out[58]: array([1, 2, 3, 4, 5])

In [59]: u
Out[59]: array([1., 1., 1., 1., 1.])

In [60]: v[:]
Out[60]: array([1, 2, 3, 4, 5])

In [61]: v[:,np.newaxis]
Out[61]:
array([[1],
       [2],
       [3],
       [4],
       [5]])

In [62]: u*v
Out[62]: array([1., 2., 3., 4., 5.])

In [63]: u*v[:,np.newaxis]
Out[63]:
array([[1., 1., 1., 1., 1.],
       [2., 2., 2., 2., 2.],
       [3., 3., 3., 3., 3.],
       [4., 4., 4., 4., 4.],
       [5., 5., 5., 5., 5.]])
```

## Click

Permet de créer des CLI (command line interface) en Python.

### Exercice

Ecrire un programme en Click qui résoud l'équation quadratique.
Le programme prend 3 éléments A, B, C et affiche les solutions réelles ou imaginaires

**Exercice dans le fichier ex_click.py**
