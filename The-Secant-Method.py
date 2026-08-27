#                                                                      f(x) = x^2 - 2
def secant_method(f, x0, x1, tol=1e-8, max_iter=100):
    for i in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)
        
        if abs(f1 - f0) < 1e-15:
            return x1
        
        x_new = x1 - f1 * (x1 - x0) / (f1 - f0)
        print(f"{i+1}: {x_new}")
        
        if abs(x_new - x1) < tol:
            return x_new
        
        x0, x1 = x1, x_new  # Shift: old x1 becomes x0, new becomes x1
    
    return x1

def f(x):
    return x**2 - 2


root = secant_method(f, -1, 2)
print(f"Root = {root:.10f}")