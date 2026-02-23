import pandas as pd
from functions import make_function
from methods import bisection, newton
from visualization import plot_function, plot_convergence

expr = input("Masukkan fungsi f(x): ")

try:
    f = make_function(expr)
    f(1.0)
except Exception as e:
    print("Fungsi tidak valid:", e)
    exit()

root_bis, hist_bis, err_bis = bisection(f, 1, 2)
root_newt, hist_newt, err_newt = newton(f, 1.5)

# 📊 Tabel Bisection
df_bis = pd.DataFrame({
    "Iterasi": range(len(hist_bis)),
    "x": hist_bis,
    "Error": err_bis
})

# 📊 Tabel Newton
df_newt = pd.DataFrame({
    "Iterasi": range(len(hist_newt)),
    "x": hist_newt,
    "Error": err_newt
})

print("\n=== Tabel Iterasi Bisection ===")
print(df_bis)

print("\n=== Tabel Iterasi Newton ===")
print(df_newt)

plot_function(f)
plot_convergence(hist_bis, hist_newt)