import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def plot_function_streamlit(f):
    x_vals = np.linspace(-5, 5, 400)
    y_vals = [f(x) for x in x_vals]

    fig, ax = plt.subplots()
    ax.axhline(0)
    ax.plot(x_vals, y_vals)

    st.pyplot(fig)