from sympy import Symbol, solve
x = Symbol('x')
y = Symbol('y')

pt1 = 2*x + 3*y - 12
pt2 = 3*x - 2*y - 5

nghiem = solve((pt1, pt2), dict=True)
print(nghiem)

# Kiểm tra nghiệm
pt1_val = pt1.subs({x: nghiem[0][x], y: nghiem[0][y]})
pt2_val = pt2.subs({x: nghiem[0][x], y: nghiem[0][y]})
print(pt1_val)  # 0
print(pt2_val)  # 0