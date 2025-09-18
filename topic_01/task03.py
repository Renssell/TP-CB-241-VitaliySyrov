def disc(a: float, b: float, c: float) -> float:
    return b**2 - 4*a*c

a, b, c = 1, -3, 2
print(f"Дискримінант для a={a}, b={b}, c={c}: {disc(a, b, c)}")
