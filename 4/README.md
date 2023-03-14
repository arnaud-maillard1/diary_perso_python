# Cours 4

## Opérations fonctionnelles pour **tous** les conteneurs de données

```ipython
In [1]: {2,3,4,5}-{2,4} # retire le 2 et 4 du dictionnaire
Out[1]: {3, 5}

In [2]: {2,3,4,5,6}^{2,3,4} # garde uniquement ceux qui sont que dans 1 des dictionnaires
Out[2]: {5, 6}
```

## Opérateurs

- All :

  ```ipython
  In [3]: all((1,2,3,4))
  Out[3]: True

  In [4]: all((1,0,3,4))
  Out[4]: False
  ```

- Any :

  ```ipython
  In [10]: any((0,0,0))
  Out[10]: False


  In [11]: any((0,0,1))
  Out[11]: True
  ```

- Swapper :

  ```ipython
  In [12]: a = 1

  In [13]: b = 2

  In [14]: a,b = b,a

  In [15]: a
  Out[15]: 2

  In [16]: b
  Out[16]: 1
  ```

- Variable poubelle `_` :

  ```ipython
  In [19]: l = [1,2,3,4]

  In [20]: \_ = 4

  In [21]: _ ,a, b, _ = l

  In [22]: \_
  Out[22]: 4

  In [23]: a
  Out[23]: 2

  In [24]: b
  Out[24]: 3
  ```

- Enumerate :

  ```ipython
    In [27]: l = [3,2,5,6]

    In [28]: list(enumerate(l))
    Out[28]: [(0, 3), (1, 2), (2, 5), (3, 6)]

    l = [3,2,5,6]
    In [35]: for i, v in enumerate(l) :
        ...:     print(f"i = {i}, v = {v}")
        ...:
    i = 0, v = 3
    i = 1, v = 2
    i = 2, v = 5
    i = 3, v = 6
  ```

# Yield return

```ipython
In [39]: def foo():
    ...:     i = 0
    ...:     while True :
    ...:         i += 1
    ...:         yield i
    ...:

In [40]: foo()
Out[40]: <generator object foo at 0x7fb82e7f7d60>

In [41]: next(foo())
Out[41]: 1

In [42]: next(foo())
Out[42]: 1

In [43]: next(foo())
Out[43]: 1

In [44]: foo()
Out[44]: <generator object foo at 0x7fb82cc30a50>

In [45]: g = foo()

In [46]: next(g)
Out[46]: 1

In [47]: next(g)
Out[47]: 2
```

# Opérateur zip

```ipython
In [49]: a = [42, 43,44,45]

In [50]: b = [23,24,25,26]

In [51]: zip(a,b)
Out[51]: <zip at 0x7fb82cd843c0>

In [52]: list(zip(a,b))
Out[52]: [(42, 23), (43, 24), (44, 25), (45, 26)]

In [53]: b = [23,24]

In [54]: list(zip(a,b))
Out[54]: [(42, 23), (43, 24)]

In [55]: list(zip(range(10), foo())) # avec foo qui est définit en dessus
Out[55]:
[(0, 1),
 (1, 2),
 (2, 3),
 (3, 4),
 (4, 5),
 (5, 6),
 (6, 7),
 (7, 8),
 (8, 9),
 (9, 10)]
```

La fonction `zip` seule nous retourne un générateur qui est consommable par des boucles `for`, `list()`, ...

```ipython
In [56]: zip(a,b)
Out[56]: <zip at 0x7fb82cd58280>

In [57]: for i, v in zip(a,b) :
    ...:     print(f"i = {i}, v = {v}")
    ...:
i = 42, v = 23
i = 43, v = 24
```

# Opérateur `*`

Ca destructure la valeur

Pour une liste : `l = [1,2,3,4]`, si on donne comme argument `*l`, alors on aura comme argument `1,2,3,4` et donc c'est la liste sans les corchets donc 5 éléments

```ipython

In [77]: def toto(*args, **kwargs) :
    ...:     print("Args", args)
    ...:     print("Kwargs", kwargs)
    ...:

In [78]: l
Out[78]: [3, 2, 5, 6]

In [79]: toto(*l, "salut", 4, *l)
Args (3, 2, 5, 6, 'salut', 4, 3, 2, 5, 6)
Kwargs {}

In [80]: toto(*l, "salut", 4, *l, ala=23)
Args (3, 2, 5, 6, 'salut', 4, 3, 2, 5, 6)
Kwargs {'ala': 23}

In [81]: toto(*l, "salut", 4, *l, ala=23, te=2)
Args (3, 2, 5, 6, 'salut', 4, 3, 2, 5, 6)
Kwargs {'ala': 23, 'te': 2}

```

```ipython
In [83]: def operate(a,b, **kwargs) :
    ...:     if 'add' in kwargs :
    ...:         print(f"{a}+{b} = {a+b}")
    ...:     if 'sub' in kwargs :
    ...:         print(f"{a}-{b} = {a-b}")
    ...:

In [88]: operate(3,4, sub=0)
3-4 = -1

In [89]: operate(3,4, add=8)
3+4 = 7
```

# Exemple avec map et zip

Map utilise une fonction et une liste en argument pour construire une map qu'on convertit en liste ensuite : [lien](https://www.geeksforgeeks.org/python-map-function/)

```ipython
In [108]: lastname
Out[108]: ['Gremaud', 'Cardinale']

In [109]: firstname
Out[109]: ['Benjamin', 'Adrien']

In [110]: map(lambda x : ' '.join(x),list(zip(firstname, lastname)))
Out[110]: <map at 0x7fb82c891fd0>

In [111]: list(map(lambda x : ' '.join(x),list(zip(firstname, lastname))))
Out[111]: ['Benjamin Gremaud', 'Adrien Cardinale']
```

# Exercice donnée

Exercez-vous avec les éléments suivants:

```python
in
all
any
map
filter
*
**
```

On a une liste de noms de poissons chaque élément est un tuple avec

- Le nom du poisson
- Son espèce
- Son sexe
- Mort ou vivant (bool)

On vous demande :

1. Filtrer la liste pour ne récupérer que les poissons mâles
2. Afficher que les noms de poissons
3. Établir une liste (set) de toutes les espèces présentes dans l'aquarium
4. Créer une fonction `fish(name, group, genre, status)` qui affiche :
   `Poisson {name} de l'espèce {group} est {"vivant" if status else "mort"}`
5. Executer la fonction pour chaque élément de la liste (vous utiliserez `*`)
6. Comment savoir en une ligne si il y a des poissons mort dans l'aquarium
7. Est-ce qu'il y a un "Scalaire" (nom de l'espèce) dans votre aquarium ?

```python
import random

fish_names = ["Trout", "Salmon", "Bass", "Catfish", "Tuna", "Mackerel", "Sardine", "Haddock", "Halibut", "Cod"]
fish_species = ["Oncorhynchus mykiss", "Salmo salar", "Micropterus salmoides", "Ictalurus punctatus", "Thunnus albacares", "Scomber scombrus", "Sardina pilchardus", "Melanogrammus aeglefinus", "Hippoglossus hippoglossus", "Gadus morhua"]
fish_gender = ["Male", "Female"]
fish_status = [True, False]

fish_list = []

for i in range(100):
    name = random.choice(fish_names)
    species = random.choice(fish_species)
    gender = random.choice(fish_gender)
    status = random.choice(fish_status)
    fish_list.append((name, species, gender, status))

print(fish_list)
```

## Exercice

1. Filtrer la liste pour ne récupérer que les poissons mâles

   ```ipython
   list(filter(lambda x : x[2] == 'Male', fish_list))
   ```

2. Afficher que les noms de poissons

   ```ipython
   In [40]: fish_list_columns = list(zip(*fish_list)) # une liste pour les noms, une pour l'espèce, ...

   In [41]: fish_list_columns[0]
   Out[41]:
   ('Tuna',
    'Cod',
    'Salmon',
    'Cod',
    'Catfish',
    'Cod',
    'Haddock',
    'Trout',
    'Bass',
    'Salmon',
    'Salmon',
    'Tuna',
    'Salmon',
    ...
     'Tuna',
    'Catfish',
    'Salmon',
    'Sardine',
    'Catfish')
   ```

3. Établir une liste (set) de toutes les espèces présentes dans l'aquarium

   ```ipython
   In [47]: species = set(fish_list_columns[1])

   In [48]: species
   Out[48]:
   {'Gadus morhua',
    'Hippoglossus hippoglossus',
    'Ictalurus punctatus',
    'Melanogrammus aeglefinus',
    'Micropterus salmoides',
    'Oncorhynchus mykiss',
    'Salmo salar',
    'Sardina pilchardus',
    'Scomber scombrus',
    'Thunnus albacares'}
   ```

4. Créer une fonction `fish(name, group, genre, status)` qui affiche :
   `Poisson {name} de l'espèce {group} est {"vivant" if status else "mort"}`

   ```ipython
   In [53]: def fish(name, group, genre, status) :
       ...:         print(f"Poisson {name} de l'espèce {group} est {'vivant' if status else 'mort'}")
       ...:
   ```

   Attention il ne faut pas mettre de double guillemets, mais des simples guillemets

5. Executer la fonction pour chaque élément de la liste (vous utiliserez `*`)

```ipython
In [63]: for x in fish_list :
    ...:     fish(*x)
    ...:
Poisson Tuna de l'espèce Oncorhynchus mykiss est mort
Poisson Cod de l'espèce Ictalurus punctatus est mort
Poisson Salmon de l'espèce Thunnus albacares est vivant
Poisson Cod de l'espèce Micropterus salmoides est mort
Poisson Catfish de l'espèce Micropterus salmoides est mort
Poisson Cod de l'espèce Melanogrammus aeglefinus est vivant
Poisson Haddock de l'espèce Micropterus salmoides est vivant
Poisson Trout de l'espèce Salmo salar est vivant
Poisson Bass de l'espèce Thunnus albacares est mort
Poisson Salmon de l'espèce Sardina pilchardus est mort
Poisson Salmon de l'espèce Micropterus salmoides est mort
Poisson Tuna de l'espèce Melanogrammus aeglefinus est mort
Poisson Salmon de l'espèce Sardina pilchardus est vivant
Poisson Bass de l'espèce Gadus morhua est vivant
...
```

Mais pourquoi ça ça ne marche pas ? :

```ipython
In [69]: print([fish(*x) for x in fish_list])
Poisson Tuna de l'espèce Oncorhynchus mykiss est mort
Poisson Cod de l'espèce Ictalurus punctatus est mort
Poisson Salmon de l'espèce Thunnus albacares est vivant
...
Poisson Salmon de l'espèce Micropterus salmoides est mort
Poisson Sardine de l'espèce Melanogrammus aeglefinus est mort
Poisson Catfish de l'espèce Gadus morhua est vivant
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
```

6. Comment savoir en une ligne si il y a des poissons mort dans l'aquarium

Pourquoi les 2 marchent ?

```ipython
In [79]: any(filter(lambda x : x[3]==False, fish_list))
Out[79]: True
```

```ipython
In [80]: any(list(filter(lambda x : x[3]==False, fish_list)))
Out[80]: True
```

7. Est-ce qu'il y a un "Scalaire" (nom de l'espèce) dans votre aquarium ?

```ipython
In [90]: any(list(filter(lambda x : x[1]=='Gadus morhua', fish_list)))
Out[90]: True

In [91]: any(list(filter(lambda x : x[1]=='Scalaire', fish_list)))
Out[91]: False
```
