
class Foo:
    # C'est pas vraiment un constructeur, mais plus un initialisateur,
    # car il reçoit en paramètre l'instance déjà créée
    def __init__(self, name):
        self.name = name

    # C'est le contructeur, il reçoit en paramètre la classe
    def __new__(cls):
        return super().__new__(cls)
