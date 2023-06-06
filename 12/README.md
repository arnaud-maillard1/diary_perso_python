# Cours 12

- Classes
- Paquets/Modules

## Classes

- Toute classe et objet sont des instances de la classe `type`
- Créer de l'héritage entre classes avec une flèche et des carrés (UML)
- Que la flèche d'héritage on la prononce "est un"
- Qu'une classe peut hériter de plusieurs classes, mais c'est pas bien
- Que c'est pas bien à cause du problème du diamant
- On doit toujours appeler le constructeur de la classe parente avec `super().__init__(...)`
- On peut avoir un getter avec `@property` et un setter avec `@<nom>.setter`
- Il existe en Python un vrai constructeur appelé `__new__(cls)`
- Le `__init__` n'est pas un constructeur, c'est un initialisateur
- Une fonctionnalité "très avancée" de Python sont les metaclasses
- Une metaclasse est typiquement utilisée pour créer des Singleton
- Un Singleton c'est un patron de conception (design pattern) qui permet de créer une classe qui n'a qu'une seule instance
- Un logger est typiquement un Singleton%
