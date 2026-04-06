# Replace the "ANSWER HERE" for your answer
from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK

from pycparser.c_ast import Return

def roots(a, b, c):
    discriminante = ((b**2 -4* a * c) * 0.5)
    if discriminante > 0:
        r1 = round(-b + discriminante**0.5)/(2*a)
        r2 = round(-b - discriminante**0.5)/(2*a)
        return f"({r1}, {r2})"
    elif discriminante == 0:
        r = -b/(2*a)
        return f"({r})"
    elif discriminante < 0:
        return"( )"

def value_y(a, b, c, x):
    return a * (x**2) + b * x + c

def to_string(a, b, c):
    if a == 0 and b == 0:
        return (f"f(x) = {c}")
    elif a == 0:
        return (f"f(x) = {b} * X + {c}")
    elif b == 0:
        return (f"f(x) = {a} * X^2 + {c}")
    elif c == 0:
        return (f"f(x) = {a} * X^2 + {b} * X")
    else:
        return (f"f(x) = {a} * X^2 + {b} * X + {c}")

def derivation(a, b, c):
    if (2 * a) == 0:
        return(f"f'(x) = {b}")
    elif b == 0:
        return(f"f'(x) = {2 * a} * X")
    else:
        return (f"f'(x) = {2 * a} * X + {b}")
