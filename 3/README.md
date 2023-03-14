# Cours 3

## Surcharge d'opérateurs

Toutes les surcharges d'opérateurs sont disponibles dans le [data model python](https://docs.python.org/3/reference/datamodel.html#), mais pour les opérateurs numériques, on peut se référer à la [section sur les opérateurs numériques](https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types)

### Exemple 1

```ipython
In [12]: class Number:
    ...:     def __init__(self, number):
    ...:         self.number = number
    ...:     def __add__(self, n) :
    ...:         return self.number + n
    ...:     def __sub__(self, n) :
    ...:         return self.number - n
    ...:     def __mul__(self, n) :
    ...:         return self.number * n
    ...:     def __floordiv__(self, n) : # //
    ...:         return self.number / n
    ...:     def __truediv__(self, n): # /
    ...:         return self.number / n
    ...:

In [13]: n = Number(42)

In [14]: n - 33
Out[14]: 9

In [15]: n*10
Out[15]: 420

In [16]: n+8
Out[16]: 50
```

Attention, ici le type retourné est un `int` et non un `Number`.

### Exemple 2

```ipython
In [5]: class Number:
   ...:     def __init__(self, number):
   ...:         self.number = number
   ...:     def __add__(self, n) :
   ...:         return Number(self.number + n)
   ...:     def __repr__(self):
   ...:         return str(self.number)
   ...:

In [6]: n = Number(42)

In [7]: n
Out[7]: 42

In [8]: Number(42)
Out[8]: 42
```

Ici, on utilise `__repr__` pour afficher un `Number` comme un `int`.

### Exemple 3

```ipython
In [9]: class Number:
   ...:     def __init__(self, number):
   ...:         self.number = number
   ...:     def __add__(self, n) :
   ...:         return Number(self.number + n)
   ...:     def __repr__(self):
   ...:         return f"Number({self.number})"
   ...:

In [10]: Number(42)
Out[10]: Number(42)
```

On utilise ici une `f-string` pour afficher un `Number` comme on le souhaite.

### Exemple 4

```ipython
In [11]: class Number:
    ...:     def __init__(self, number):
    ...:         self.number = number
    ...:     def __add__(self, n) :
    ...:         return Number(self.number + n)
    ...:     def __repr__(self):
    ...:         return f"Number({self.number})"
    ...:     def __str__(self) :
    ...:         return str(self.number)
    ...:

In [12]: print(Number(42))
42

In [13]: Number(42)
Out[13]: Number(42)
```

Finalement on peut voir la différence entre `__repr__` et `__str__` ci-dessus.

### Exemple 5

```ipython
In [14]: n+33
Out[14]: Number(75)

In [15]: 33+n
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In [15], line 1
----> 1 33+n

TypeError: unsupported operand type(s) for +: 'int' and 'Number'
```

Ici on voit que l'opérateur `+` n'est pas associatif.

### Exemple 6

```ipython
In [16]: class Number:
    ...:     def __init__(self, number):
    ...:         self.number = number
    ...:     def __add__(self, n) :
    ...:         print("Add")
    ...:         return Number(self.number + n)
    ...:     def __radd__(self, n):
    ...:         print("Radd")
    ...:         return self + n # utilisation de la surcharge déjà faite auparavant
    ...:     def __repr__(self):
    ...:         return f"Number({self.number})"
    ...:     def __str__(self) :
    ...:         return str(self.number)
    ...:

In [17]: Number(42)
Out[17]: Number(42)

In [18]: n = Number(42)

In [19]: n +33
Add
Out[19]: Number(75)

In [20]: 33 + n
Radd
Add
Out[20]: Number(75)
```

Ici on surcharge `__radd__` pour que l'opérateur `+` soit associatif. Afin de simplifier le code on utilise la surcharge déjà faite auparavant dans `__radd__`.

## Listes et compréhensions

### Exemple 1

```ipython
In [1]: u = [1,2,3,4,5]

In [2]: type(u)
Out[2]: list

In [3]: []
Out[3]: []

In [4]: [x+ 10 for x in [1,2,3,4]]
Out[4]: [11, 12, 13, 14]

In [5]: [x % 2 for x in [1,2,3,4]]
Out[5]: [1, 0, 1, 0]

In [6]: [x + 10 for x in [1,2,3,4] if x < 3]
Out[6]: [11, 12]
```

On peut utiliser des **compréhensions** de listes pour créer des listes.

### Exemple 2

```ipython
In [8]: [x + 10 for y in [[1,2],[3,4]] for x in [1,2,3,4] if x < 3]
Out[8]: [11, 12, 11, 12]
```

C'est inversé par rapport à l'ordre logique et c'est aussi plutôt moche.

### Exemple 3

```ipython
In [13]: u = [str(x) for x in [1,2,3,4]]

In [14]: u
Out[14]: ['1', '2', '3', '4']

In [15]: '-'.join(u)
Out[15]: '1-2-3-4'
```

Au lieu de faire une boucle for avec une condition spéciale pour que qu'après le chiffre 4 il y ait un tiret, on peut utiliser la fonction `join` qui permet de concaténer les éléments d'une liste avec un séparateur.

Donc quand on commence à avoir des spécialités dans le code python, c'est souvent qu'il existe une solution plus simple.

## Import this

La commande `import this` permet d'afficher le _Zen of Python_ qui est une liste de règles à suivre pour écrire du code Python.

```ipython
In [9]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## PEP 8

C'est le `Style Guide for Python Code` qui est une liste de règles à suivre pour écrire du code Python disponible [ici](https://peps.python.org/pep-0008/)
