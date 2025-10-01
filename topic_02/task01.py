from math import sqrt


def disc(a: float, b: float, c: float) -> float:
    return b**2 - 4*a*c

a, b, c = 1, -3, 2
print(f"Дискримінант для a={a}, b={b}, c={c}: {disc(a, b, c)}")

def root(a: float, b: float, c: float): 
    d = disc(a, b, c)
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x = -b / (2 * a)
        return x,
    else:
        return None
print(f"Корені: {root(a, b, c)}")
