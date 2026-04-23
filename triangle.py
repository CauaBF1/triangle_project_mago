"""
Cauã Borges Faria - 834437
Nicolas Magno - 834054
Lucas Rodrigues - 834724
https://github.com/CauaBF1/triangle_project_mago
"""

from dataclasses import dataclass
from enum import Enum, auto


class TriangleType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    INVALID = auto()


@dataclass(frozen=True, slots=True)
class Triangle:
    side1: float
    side2: float
    side3: float

    @property
    def type(self) -> TriangleType:
        a, b, c = self.side1, self.side2, self.side3

        if isinstance(a, bool) or isinstance(b, bool) or isinstance(c, bool):
            return TriangleType.INVALID

        if a <= 0 or b <= 0 or c <= 0:
            return TriangleType.INVALID

        if a >= b + c or b >= a + c or c >= a + b:
            return TriangleType.INVALID

        if a == b == c:
            return TriangleType.EQUILATERAL

        if a == b or a == c or b == c:
            return TriangleType.ISOSCELES

        return TriangleType.SCALENE

    @property
    def is_right(self) -> bool:
        if self.type == TriangleType.INVALID:
            return False

        x, y, z = sorted([self.side1, self.side2, self.side3])
        return abs(x**2 + y**2 - z**2) < 1e-9

    @property
    def message(self) -> str:
        a, b, c = self.side1, self.side2, self.side3

        if isinstance(a, bool):
            return "The triangle is invalid because the first side (X) is a boolean."
        if isinstance(b, bool):
            return "The triangle is invalid because the second side (Y) is a boolean."
        if isinstance(c, bool):
            return "The triangle is invalid because the third side (Z) is a boolean."

        if a <= 0:
            return f"The triangle is invalid because X={a} must be greater than zero."
        if b <= 0:
            return f"The triangle is invalid because Y={b} must be greater than zero."
        if c <= 0:
            return f"The triangle is invalid because Z={c} must be greater than zero."

        if a >= b + c:
            return f"The triangle is invalid because X={a} >= Y+Z={b + c}."
        if b >= a + c:
            return f"The triangle is invalid because Y={b} >= X+Z={a + c}."
        if c >= a + b:
            return f"The triangle is invalid because Z={c} >= X+Y={a + b}."

        x, y, z = sorted([a, b, c])
        is_right = abs(x**2 + y**2 - z**2) < 1e-9

        if a == b == c:
            return f"The triangle is equilateral because X=Y=Z={a}."

        if a == b:
            equal = f"X and Y are equal to {a}"
        elif a == c:
            equal = f"X and Z are equal to {a}"
        elif b == c:
            equal = f"Y and Z are equal to {b}"
        else:
            equal = None

        if equal:
            if is_right:
                return (
                    f"The triangle is right and isosceles because {equal} "
                    f"and {x}² + {y}² = {z}²."
                )
            return f"The triangle is isosceles because {equal}."

        if is_right:
            return (
                f"The triangle is right and scalene because X={a}, Y={b}, Z={c} are all different "
                f"and {x}² + {y}² = {z}²."
            )

        return f"The triangle is scalene because X={a}, Y={b}, Z={c} are all different."


if __name__ == "__main__":
    x = float(input("Enter the first side (X): "))
    y = float(input("Enter the second side (Y): "))
    z = float(input("Enter the third side (Z): "))

    triangle = Triangle(x, y, z)

    print(f"Type: {triangle.type.name}")
    print(triangle.message)
