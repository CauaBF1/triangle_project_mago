from triangle import Triangle, TriangleType

# a + b > c
# a + c > b
# b + c > a


def test_equilateral():
    t = Triangle(7, 7, 7)
    assert t.type == TriangleType.EQUILATERAL
    assert t.message == "The triangle is equilateral because X=Y=Z=7."


def test_isosceles():
    t = Triangle(7, 7, 5)
    assert t.type == TriangleType.ISOSCELES
    assert t.message == "The triangle is isosceles because X and Y are equal to 7."


def test_scalene():
    t = Triangle(7, 5, 3)
    assert t.type == TriangleType.SCALENE
    assert (
        t.message == "The triangle is scalene because X=7, Y=5, Z=3 are all different."
    )


def test_scalene2():
    t = Triangle(5, 7, 3)
    assert t.type == TriangleType.SCALENE
    assert (
        t.message == "The triangle is scalene because X=5, Y=7, Z=3 are all different."
    )


# Lado negativo
def test_invalid_negative_number():
    t = Triangle(7, 5, -1)
    assert t.type == TriangleType.INVALID
    assert (
        t.message == "The triangle is invalid because Z=-1 must be greater than zero."
    )


# a + b < c
def test_invalid_triangle_inequality():
    t = Triangle(1, 2, 10)
    assert t.type == TriangleType.INVALID
    assert t.message == "The triangle is invalid because Z=10 >= X+Y=3."


# a + b = c
def test_invalid_triangle_inequality2():
    t = Triangle(1, 2, 3)
    assert t.type == TriangleType.INVALID
    assert t.message == "The triangle is invalid because Z=3 >= X+Y=3."


# 0 0 0 não formam triângulo
def test_zero_side():
    t = Triangle(0, 0, 0)
    assert t.type == TriangleType.INVALID
    assert t.message == "The triangle is invalid because X=0 must be greater than zero."


# Lados a + b < c, mesmo sendo isósceles
def test_isosceles_invalid():
    t = Triangle(1, 1, 3)
    assert t.type == TriangleType.INVALID
    assert t.message == "The triangle is invalid because Z=3 >= X+Y=2."


# Lados grandes
def test_big_number():
    t = Triangle(1000000, 1000000, 1000000)
    assert t.type == TriangleType.EQUILATERAL
    assert t.message == "The triangle is equilateral because X=Y=Z=1000000."


# Triângulos podem ter lados decimais
def test_float_sides_should_be_accepted():
    t = Triangle(3.5, 3.5, 3.5)
    assert t.type == TriangleType.EQUILATERAL
    assert t.message == "The triangle is equilateral because X=Y=Z=3.5."


def test_bool_sides_should_be_rejected():
    t = Triangle(True, True, True)
    assert t.type == TriangleType.INVALID
    assert (
        t.message == "The triangle is invalid because the first side (X) is a boolean."
    )


def test_bool_sides_should_be_rejected2():
    t = Triangle(False, False, False)
    assert t.type == TriangleType.INVALID
    assert (
        t.message == "The triangle is invalid because the first side (X) is a boolean."
    )


def test_right_triangle():
    t = Triangle(3, 4, 5)
    assert t.type == TriangleType.SCALENE
    assert t.is_right is True
    assert t.message == (
        "The triangle is right and scalene because X=3, Y=4, Z=5 are all different "
        "and 3² + 4² = 5²."
    )


def test_right_triangle2():
    t = Triangle(4, 3, 5)
    assert t.type == TriangleType.SCALENE
    assert t.is_right is True
    assert t.message == (
        "The triangle is right and scalene because X=4, Y=3, Z=5 are all different "
        "and 3² + 4² = 5²."
    )


def test_right_triangle3():
    t = Triangle(6, 8, 10)
    assert t.type == TriangleType.SCALENE
    assert t.is_right is True
    assert t.message == (
        "The triangle is right and scalene because X=6, Y=8, Z=10 are all different "
        "and 6² + 8² = 10²."
    )


def test_right_isosceles_triangle():
    t = Triangle(1, 1, 2**0.5)
    assert t.type == TriangleType.ISOSCELES
    assert t.is_right is True
    assert t.message == (
        "The triangle is right and isosceles because X and Y are equal to 1 "
        "and 1² + 1² = 1.4142135623730951²."
    )


def test_right_isosceles_triangle2():
    t = Triangle(3, 3, 3 * (2**0.5))
    assert t.type == TriangleType.ISOSCELES
    assert t.is_right is True
    assert t.message == (
        "The triangle is right and isosceles because X and Y are equal to 3 "
        "and 3² + 3² = 4.242640687119286²."
    )
