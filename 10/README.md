# Cours 10

## Itertools

Fonctions pour créer des itérateurs efficaces.

- `product` : produit cartésien
- `permutations` : permutations
- `combinations` : combinaisons
- `combinations_with_replacement` : combinaisons avec remplacement

## Functools

Pour calculer le n-ième nombre de Fibonacci, on peut utiliser la formule suivante :

```python
def fib(n):
    if n <= 2 : return 1
    return fib(n-1) + fib(n-2)
```

Ce qui nous donne un algorithme récursif pas très efficace qui recalculera plusieurs fois les mêmes valeurs.

On peut améliorer avec un cache créé à la volée :

```python
def fib(n, cache={}):
    if n in cache:
        return cache[n]
    if n < 2:
        return n
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]
```

Ce qui est déjà mieux, mais on peut faire encore mieux avec le décorateur : `functools.cache` :

```python
import functools

@functools.lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```

**La fonction `lru_cache` fait donc ce qui s'appelle de la *mémoïsation*ou de la programmation dynamique.**

## Heapq

```ipython
In [17]: import heapq

In [18]: heap = []

In [19]: heapq.heappush(heap, 42)

In [20]: heap
Out[20]: [42]

In [21]: heapq.heappush(heap, 23)

In [22]: heap
Out[22]: [23, 42]

In [23]: heapq.heappush(heap, 77)

In [24]: heapq.heappush(heap, 25)

In [25]: heap
Out[25]: [23, 25, 77, 42]

```

L'ordre vu comme ceci n'est pas compréhensible, mais si on le voit comme **un arbre binaire**, on comprend mieux :

```
      23
    /    \
          42
        /  \
       25   77
```

Tous les nombre à droite de 23 seront plus grands que 23, et tous les nombres à gauche de 23 seront plus petits que 23.
