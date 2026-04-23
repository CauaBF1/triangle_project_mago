# Solução de exercício proposto em Engenharia de Software 2
Grupo composto por Cauã Borges, Lucas Rodrigues e Nicolas Magno

# Objetivo
A atividade proposta foi dividir o grupo em Dev (Nicolas) e Teste(Cauã e Lucas), aonde o grupo de Teste encontra falhas no código e o Dev soluciona.
Exemplo:
    Um triângulo não pode ter como entrada valores booleanos, porém o código original aceitava essa entrada e como resultado de saída tinha como: Equilátero, o grupo de Teste encontrou esse caso, e o Dev solucionou.
Trecho no código:
test_triangle.py:
    # Retorna EQUILATERAL, porém é para retornar INVALID. Possívelmente muda para (1,1,1)
def test_bool_sides_should_be_rejected():
    t = Triangle(True, True, True)
    assert t.type == TriangleType.INVALID
def test_bool_sides_should_be_rejected2():
    t = Triangle(False, False, False)
    assert t.type == TriangleType.INVALID
    
triangle.py:
        if isinstance(a, bool) or isinstance(b, bool) or isinstance(c, bool):
            return TriangleType.INVALID

# Triangle Problem (Python + pytest)

This repository contains a Python implementation of the classic **Triangle Problem**, commonly used in software testing.

## Problem

Given three integers representing the sides of a triangle, the program must classify it as:

- **EQUILATERAL** — all sides equal  
- **ISOSCELES** — two sides equal  
- **SCALENE** — all sides different  
- **INVALID** — does not form a valid triangle  

---

##  Setup

Create a virtual environment and install dependencies:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
pip install pytest


