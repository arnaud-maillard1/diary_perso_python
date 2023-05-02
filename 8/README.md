# Cours 8

# Software Design Principles

Un principe de conception est une règle gnérale qui guide le développement d'un logiciel. Il est souvent exprimé sous forme de phrase, et peut être utilisé pour évaluer la qualité d'un logiciel.

- [x] SSOT
- [x] SOLID
- [x] KISS
- [x] DRY/WET
- [x] YAGNI

## SSOT (Single Source of Truth)

La règle du SSOT s'applique aux données et pas à la redondance du code. Elle stipule que les données doivent être stockées dans un seul endroit. Si une donnée doit être modifiée, elle doit être modifiée dans un seul endroit.

Mauvais exemple :

```python
equipageDes42MillesEtUneNuits = {
"capitaine" : 42, # Le capitaine a 42 ans
"moussailon" : 42,
"machininiste" : 42
}
```

Bon exemple :

```python
ageEquipage = 42

equipageDes42MillesEtUneNuits = {
"capitaine" : ageEquipage,# Le capitaine a un certain age
"moussailon" : ageEquipage,
"machininiste" : ageEquipage
}
```

### DRY (Don't Repeat Yourself)

Le contraire est le WET (Write Everything Twice).

Exemple de code WET :

```python
def calculerSomme(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

sommePommes = calculerSomme(liste[pommes])
sommePoires = calculerSomme(liste[poires])
sommeBananes = calculerSomme(liste[bananes])
```

Une meilleure solution :

```python
sommes = {}
for key, values in liste.items():
    sommes[key] = calculerSomme(values)
```

Et avec une compréhension :

```python
sommes = {key: calculerSomme(values) for key, values in liste.items()}
```

### KISS (Keep It Simple, Stupid)

Une fonction ça devrait entre 10 lignes et un écran. Si c'est plus compliqué, c'est qu'il y a un problème.

### YAGNI (You Ain't Gonna Need It)

Ne pas coder des fonctionnalités qui ne sont pas nécessaires. C'est une bonne règle pour éviter de coder des fonctionnalités qui ne seront jamais utilisées.

Par exemple le gars qui a construit le moteur d'avion sur l'image ci-dessous n'a pas suivi cette règle. Il a installé une selle dessus parce qu'il se disait que ça pourrait être utile un jour, mais ca n'a jamais été utilisé :

![YAGNI](https://res.cloudinary.com/practicaldev/image/fetch/s--u53Aunfr--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tq3ggyimlj9h32ektgrx.png)

### SOLID

On va pas encore parler de ca c'est un peu tôt pour ceux qui n'ont pas eu POO

# Pipenv

C'est pour avoir une sorte de bac à sable ou l'on peut installer des packages python sans les installer globalement sur son ordinateur.

## Création d'un environnement virtuel

**Pour créer un enivronnement on utilise la commande : `python3 -mvenv venv`**

Exemple :

```bash
➜  projet git:(master) ✗ python3 -mvenv venv
➜  projet git:(master) ✗ ls -a
.  ..  __init__.py  __main__.py  venv
➜  projet git:(master) ✗ ls -la
total 0
drwxrwxrwx 1 arnaud-maillard1 arnaud-maillard1 4096 Apr 18 11:15 .
drwxrwxrwx 1 arnaud-maillard1 arnaud-maillard1 4096 Apr 18 11:04 ..
-rwxrwxrwx 1 arnaud-maillard1 arnaud-maillard1   44 Apr 18 11:06 __init__.py
-rwxrwxrwx 1 arnaud-maillard1 arnaud-maillard1   35 Apr 18 11:08 __main__.py
drwxrwxrwx 1 arnaud-maillard1 arnaud-maillard1 4096 Apr 18 11:19 venv
```

On voit qu'il a créé un dossier `venv`

## Activation de l'environnement virtuel

**Pour activer l'environnement virtuel on utilise la commande : `source venv/bin/activate`**

Exemple :

```bash
➜  projet git:(master) ✗ source venv/bin/activate
(venv) ➜  projet git:(master) ✗ which python3
/mnt/c/Users/arnau/OneDrive/Documents/HEIGVD/Semestre_6/Python/diary_perso_python/8/projet/venv/bin/python3
(venv) ➜  projet git:(master) ✗ deactivate
➜  projet git:(master) ✗ which python3
/usr/bin/python3
➜  projet git:(master) ✗
```

## Installation de packages

**Pour installer un package on utilise la commande : `pip install <package>` lorsqu'on a déjà activé l'environnement**

Exemple :

```bash
(venv) ➜  projet git:(master) ✗ pip install autopep8
Collecting autopep8
  Downloading autopep8-2.0.2-py2.py3-none-any.whl (45 kB)
     |████████████████████████████████| 45 kB 944 kB/s
Collecting pycodestyle>=2.10.0
  Using cached pycodestyle-2.10.0-py2.py3-none-any.whl (41 kB)
Collecting tomli; python_version < "3.11"
  Using cached tomli-2.0.1-py3-none-any.whl (12 kB)
Installing collected packages: pycodestyle, tomli, autopep8
Successfully installed autopep8-2.0.2 pycodestyle-2.10.0 tomli-2.0.1
(venv) ➜  projet git:(master) ✗ pip list
Package       Version
------------- -------
autopep8      2.0.2
numpy         1.24.2
pip           20.0.2
pkg-resources 0.0.0
pycodestyle   2.10.0
scipy         1.10.1
setuptools    44.0.0
tomli         2.0.1
(venv) ➜  projet git:(master) ✗
```

## Ouvrir l'environnement virtuel dans VSCode

**Pour ouvrir l'environnement virtuel dans VSCode on utilise la commande : `code .`**

Exemple :

```bash
(venv) ➜  projet git:(master) ✗ code .
```

Et on voit dans VSCode que l'environnement virtuel est activé lorsqu'on se trouve sur un fichier python :

![Python env](https://i.stack.imgur.com/MAXsQ.png)

## Différence entre pipenv et un environnement anaconda

# Pint

C'est une librairie python qui permet de faire des conversions de unités. Par exemple :

```python
from pint import UnitRegistry
ureg = UnitRegistry()
distance = 10 * ureg.kilometer
print(distance.to(ureg.meter))
```

# Debugger python

On a une erreur dans notre code et on aimerait debugger :

```bash
(venv) ➜  projet git:(master) ✗ python3 -mhello
Hello world !
Traceback (most recent call last):
  File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/mnt/c/Users/arnau/OneDrive/Documents/HEIGVD/Semestre_6/Python/diary_perso_python/8/projet/hello/__main__.py", line 3, in <module>
    sayHello()
  File "/mnt/c/Users/arnau/OneDrive/Documents/HEIGVD/Semestre_6/Python/diary_perso_python/8/projet/hello/__init__.py", line 7, in sayHello
    i = i/0
ZeroDivisionError: division by zero
(venv) ➜  projet git:(master) ✗ ipython
/home/arnaud-maillard1/.local/lib/python3.8/site-packages/IPython/core/interactiveshell.py:882: UserWarning: Attempting to work in a virtualenv. If you encounter problems, please install IPython inside the virtualenv.
  warn(
Python 3.8.10 (default, Mar 13 2023, 10:26:41)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.6.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import hello

In [2]: hello.sayHello
Out[2]: <function hello.sayHello()>

In [3]: hello.sayHello()
Hello world !
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
Cell In [3], line 1
----> 1 hello.sayHello()

File /mnt/c/Users/arnau/OneDrive/Documents/HEIGVD/Semestre_6/Python/diary_perso_python/8/projet/hello/__init__.py:7, in sayHello()
      5 i = i+1
      6 i = i*10
----> 7 i = i/0

ZeroDivisionError: division by zero

In [4]: %debug
> /mnt/c/Users/arnau/OneDrive/Documents/HEIGVD/Semestre_6/Python/diary_perso_python/8/projet/hello/__init__.py(7)sayHello()
      3     print("Hello world !")
      4     i = 3
      5     i = i+1
      6     i = i*10
----> 7     i = i/0

ipdb> u
> <ipython-input-3-42affdb2d76d>(1)<module>()
----> 1 hello.sayHello()

ipdb> d
> /mnt/c/Users/arnau/OneDrive/Documents/HEIGVD/Semestre_6/Python/diary_perso_python/8/projet/hello/__init__.py(7)sayHello()
      3     print("Hello world !")
      4     i = 3
      5     i = i+1
      6     i = i*10
----> 7     i = i/0
```

On peut naviguer dans le debug avec les commandes suivantes :

- `u` pour remonter dans le code
- `d` pour descendre dans le code
- `n` pour aller à la ligne suivante
- `c` pour continuer l'exécution du code
- `q` pour quitter le debug
- `h` pour afficher l'aide

On peut même faire des commandes python dans le debug :

```bash
In [5]: %debug
> /mnt/c/Users/arnau/OneDrive/Documents/HEIGVD/Semestre_6/Python/diary_perso_python/8/projet/hello/__init__.py(7)sayHello()
      3     print("Hello world !")
      4     i = 3
      5     i = i+1
      6     i = i*10
----> 7     i = i/0
ipdb> print(i)
40
ipdb> i = 50
ipdb> print(i)
50
ipdb>
```
