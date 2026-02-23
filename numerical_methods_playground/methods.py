from functions import numerical_derivative

def bisection(f, a, b, tol=1e-6, max_iter=100):
    history = []
    errors = []

    c_old = None

    for i in range(max_iter):
        c = (a + b) / 2
        history.append(c)

        if c_old is None:
            errors.append(0)
        else:
            errors.append(abs(c - c_old))

        if abs(f(c)) < tol:
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c

    return c, history, errors


def newton(f, x0, tol=1e-6, max_iter=100):
    history = []
    errors = []

    x = x0
    x_old = None

    for i in range(max_iter):
        history.append(x)

        if x_old is None:
            errors.append(0)
        else:
            errors.append(abs(x - x_old))

        dfx = numerical_derivative(f, x)

        if abs(dfx) < 1e-10:
            raise ValueError("Turunan terlalu kecil!")

        x_new = x - f(x) / dfx

        if abs(f(x_new)) < tol:
            break

        x_old = x
        x = x_new

    return x, history, errors