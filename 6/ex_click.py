#!/usr/bin/env python3
import click


@click.command()
# @click.option('--a', default=1, help='Coefficient a')
@click.argument('a', type=float, default=1)
@click.argument('b', type=float, default=1)
@click.argument('c', type=float, default=1)
def quad(a, b, c):
    print(f"Quadratic equation: {a}x^2 + {b}x + {c} = 0")
    d = b**2 - 4*a*c
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")


if __name__ == '__main__':
    quad()
