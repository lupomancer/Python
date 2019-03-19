# coding: utf-8
def triangleArea(sideA, sideB, sideC):
    s = int((sideA + sideB + sideC) / 2)
    import math
    area = math.sqrt((s * (s - sideA) * (s - sideB) * (s - sideC)))
    print("Triangle Side A:", sideA, "Side B:", sideB, "Side C:", sideC, "Area:", area)
    return
triangleArea(3, 4, 5)
triangleArea(7, 5, 10)
triangleArea(6, 7, 8)
