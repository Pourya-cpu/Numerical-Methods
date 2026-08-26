import numpy as np

print("This first the numerical method")
print("="*50)

def newton_method(f, df, x0, tol=1e-8, max_iterate=100):

    x = x0

    for i in range(max_iterate):
        fx = f(x)
        dfx = df(x)
        x_new = x - fx / dfx
        print(f"{i+1} iterate: {x_new}")


        if abs(x_new - x)<tol:
            return x_new
    
        x = x_new

    print("Max iteration reached.")
    return x


def f(x):
    return np.sin(x) - x


def df(x):
    return np.cos(x) - 1


root = newton_method(f, df, x0=1.0)

print(f"Root = {root:.10f}")