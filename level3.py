import sympy as sy
c=float(input("请输入系数c :").strip())
b=float(input("请输入系数b :").strip())
a=float(input("请输入系数a :").strip())
x = sy.symbols("x")
y = sy.Function("y")
equation = c*y(x).diff(x,2)+b*y(x).diff(x,1)+a*y(x)
print(sy.dsolve(equation, y(x)))
sy.pprint(sy.dsolve(equation, y(x)))

