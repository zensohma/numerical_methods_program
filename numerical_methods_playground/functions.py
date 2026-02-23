import math

allowed_names = {
    "x": 0,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "exp": math.exp,
    "log": math.log,
    "sqrt": math.sqrt,
    "pi": math.pi,
    "e": math.e
}

def make_function(expr):
    def f(x):
        allowed_names["x"] = x
        return eval(expr, {"__builtins__": {}}, allowed_names)
    return f

def numerical_derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)