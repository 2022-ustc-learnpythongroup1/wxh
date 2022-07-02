import sympy as sy

x = sy.symbols("x") # 标出x和ω为自变量并用符号'x'和'w'表示之
omega = sy.symbols("w")
f = sy.Function("f") # 函数因变量f(x)，用f表示

equation = f(x).diff(x,2) + omega**2*f(x) # 化成g(f(x),x) = 0的形式，diff是求导函数

print(sy.dsolve(equation,f(x)))
sy.pprint(sy.dsolve(equation,f(x)))