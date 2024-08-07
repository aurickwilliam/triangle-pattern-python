
def increasing_triangle(n: int) -> None:
    for i in range(n):
        for j in range(i + 1):
            print("* ", end="")
        print()


def decreasing_triangle(n: int) -> None:
    for i in range(n):
        for j in range(i, n):
            print("* ", end="")
        print()


def right_triangle(n: int) -> None:
    for i in range(n):
        for j in range(i, n):
            print("  ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print()


def right_sided_triangle(n: int) -> None:
    for i in range(n):
        for j in range(i + 1):
            print("  ", end="")
        for k in range(i, n):
            print("* ", end="")
        print()


def mountain(n: int) -> None:
    for i in range(n):
        for j in range(i, n):
            print("  ", end="")
        for k in range(i):
            print("* ", end="")
        for l in range(i + 1):
            print("* ", end="")
        print()


def reversed_mountain(n: int) -> None:
    for i in range(n):
        for j in range(i + 1):
            print("  ", end="")
        for k in range(i, n - 1):
            print("* ", end="")
        for l in range(i, n):
            print("* ", end="")
        print()


def diamond(n: int) -> None:
    for i in range(n - 1):
        for j in range(i, n):
            print("  ", end="")
        for k in range(i):
            print("* ", end="")
        for l in range(i + 1):
            print("* ", end="")
        print()
    for i in range(n):
        for j in range(i + 1):
            print("  ", end="")
        for k in range(i, n - 1):
            print("* ", end="")
        for l in range(i, n):
            print("* ", end="")
        print()


increasing_triangle(5)
print()
decreasing_triangle(5)
print()
right_triangle(5)
print()
right_sided_triangle(5)
print()
mountain(5)
print()
reversed_mountain(5)
print()
diamond(5)
