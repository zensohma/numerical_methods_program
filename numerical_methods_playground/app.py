import streamlit as st
import pandas as pd
from functions import make_function
from methods import bisection, newton
from visualization import plot_function_streamlit

st.title("Numerical Methods Program")

expr = st.text_input("Masukkan fungsi f(x)", "x**3 - x - 2")

a = st.number_input("Interval a", value=1.0)
b = st.number_input("Interval b", value=2.0)
x0 = st.number_input("Initial guess (Newton)", value=1.5)

if st.button("Hitung Akar"):

    try:
        f = make_function(expr)
        f(1.0)
    except Exception as e:
        st.error(f"Fungsi tidak valid: {e}")
        st.stop()

    try:
        root_bis, hist_bis, err_bis = bisection(f, a, b)
        root_newt, hist_newt, err_newt = newton(f, x0)
    except Exception as e:
        st.error(f"Error perhitungan: {e}")
        st.stop()

    st.success(f"Root (Bisection): {root_bis}")
    st.success(f"Root (Newton): {root_newt}")

    df_bis = pd.DataFrame({
        "Iterasi": range(len(hist_bis)),
        "x": hist_bis,
        "Error": err_bis
    })

    df_newt = pd.DataFrame({
        "Iterasi": range(len(hist_newt)),
        "x": hist_newt,
        "Error": err_newt
    })

    st.subheader("📊 Tabel Iterasi Bisection")
    st.dataframe(df_bis)

    st.subheader("📊 Tabel Iterasi Newton")
    st.dataframe(df_newt)

    st.subheader("📈 Plot Fungsi")
    plot_function_streamlit(f)