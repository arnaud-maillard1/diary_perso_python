import turtle

# Configuration de la fenêtre Turtle
window = turtle.Screen()
window.bgcolor("red")
window.title("Rosace")

# Configuration de la tortue
t = turtle.Turtle()
t.color("green")
t.speed(50)  # Vitesse de dessin plus rapide

# Dessin des cercles en forme de rosace
for _ in range(36):  # 36 cercles pour une rosace complète
    t.circle(100)  # Rayon du cercle
    t.right(10)  # Angle de rotation à droite

# Fermeture de la fenêtre Turtle lorsqu'on clique dessus
turtle.done()
