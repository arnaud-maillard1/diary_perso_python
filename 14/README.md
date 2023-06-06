# Cours 14

# Exceptions

On voit ici que la gestions des erreurs complique le code :

```c
bool foo (int a, int b, int *c) {
    if (b == 0) {
        return true;
    }
    *c = a / b;
    return false;
}

bool bar(int a, int b, int *c) {
    if(c == NULL) {
        return true;
    }
    if (a % 2 != 0 || b % 2 != 0) {
        return true;
    }
    return foo(a, b, c);
}

int main() {
    bar(23, 42, NULL);
    error :
        printf("Error");
        return 1;
}
```


Les exceptions en python permettent de simplifier le code :

```ipython
In [1]: try :
   ...:     12/0
   ...: except :
   ...:     raise ValueError('Division par 0')
   ...:
---------------------------------------------------------------------
ZeroDivisionError                   Traceback (most recent call last)
Cell In [1], line 2
      1 try :
----> 2     12/0
      3 except :

ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

ValueError                          Traceback (most recent call last)
Cell In [1], line 4
      2     12/0
      3 except :
----> 4     raise ValueError('Division par 0')

ValueError: Division par 0

In [2]: try :
   ...:     12/2
   ...: except :
   ...:     raise ValueError('Division par 0')
   ...:

```

# Exempe 1

On peut faire ceci :

```python
codes = [4,8,15,16,23,42]

def get_code(i) :
    if (i > len(codes)) :
        raise ValueError('Mauvais valeur de i')
    return codes[i]
```

Mais c'est mieux de faire ceci :

```python
codes = [4,8,15,16,23,42]

def get_code(i) :
    try :
        return codes[i]
    except IndexError :
        raise ValueError('Mauvais valeur de i')
```

# Exercice 1

On aimerait créer un décorateur qui logue dans un fichier les argumenets passés à une fonction, ainsi que le temps d'exécution de la fonction. Ce décorateur s'utilise comme ceci :

```python
@heig
def myFunc(a,b) :
    return[(a + b) for i in range(1000000)]
```

Les paramètres à loguer sont: 

1. Le nom de la fonction appelée
2. Les arguments passés à la fonction
3. Le temps d'exécution de la fonction
4. La valeur de retour de la fonction
5. L'heure et la date de l'appel

Les concepts et bibliothèques utilsées seront: 

- import logging (à configurer pour écrire dans un fichier)
- les décorateurs (voir fonction wrap)
- exception (si y'a un problème avec la fonction)
- import inspect (pour connaître le nom de la fonction)
- import time (pour mesurer le temps d'exécution)