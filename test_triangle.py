from triangle import Triangle, TriangleType

# a + b > c
# a + c > b
# b + c > a


def test_equilateral():
    t = Triangle(7, 7, 7)
    assert t.type == TriangleType.EQUILATERAL


def test_isosceles():
    t = Triangle(7, 7, 5)
    assert t.type == TriangleType.ISOSCELES


def test_scalene():
    t = Triangle(7, 5, 3)
    assert t.type == TriangleType.SCALENE


# Lado negativo
def test_invalid_negative_number():
    t = Triangle(7, 5, -1)
    assert t.type == TriangleType.INVALID


# a + b < c
def test_invalid_triangle_inequality():
    t = Triangle(1, 2, 10)
    assert t.type == TriangleType.INVALID


# 0 0 0 não formam triângulo
def test_zero_side():
    t = Triangle(0, 0, 0)
    assert t.type == TriangleType.INVALID


# Lados a + b < c, mesmo sendo isóceles
def test_isosceles_invalid():
    t = Triangle(1, 1, 3)
    assert t.type == TriangleType.INVALID


# Lados grandes
def test_big_number():
    t = Triangle(1000000, 1000000, 1000000)
    assert t.type == TriangleType.EQUILATERAL


# Reformular código, triangulos podém ter lados decimais, porém está voltando inválido.
def test_float_sides_should_be_rejected():
    t = Triangle(3.5, 3.5, 3.5)
    assert t.type == TriangleType.EQUILATERAL


# Retorna EQUILATERAL, porém é para retornar INVALID. Possívelmente muda para (1,1,1)
def test_bool_sides_should_be_rejected():
    t = Triangle(True, True, True)
    assert t.type == TriangleType.INVALID


def test_bool_sides_should_be_rejected2():
    t = Triangle(False, False, False)
    assert t.type == TriangleType.INVALID

