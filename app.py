import streamlit as st
from option_pricing import black_scholes, calculate_greeks

# App title
st.title("Option Pricing Tool")

# Sidebar for user input
st.sidebar.header("Input Parameters")
S = st.sidebar.number_input("Current Stock Price (S)", value=100.0, step=1.0)
K = st.sidebar.number_input("Strike Price (K)", value=100.0, step=1.0)
T = st.sidebar.number_input("Time to Expiration (T, in years)", value=1.0, step=0.1)
r = st.sidebar.number_input("Risk-Free Rate (r, in %)", value=5.0, step=0.1) / 100
sigma = st.sidebar.number_input("Volatility (σ, in %)", value=20.0, step=0.1) / 100
option_type = st.sidebar.selectbox("Option Type", options=["call", "put"])

# Calculate option price
price = black_scholes(S, K, T, r, sigma, option_type)
st.write(f"### {option_type.capitalize()} Option Price: ${price:.2f}")

# Calculate Greeks
greeks = calculate_greeks(S, K, T, r, sigma)
st.write("### Option Greeks")
st.write(greeks)

# Visualization (Optional)
import matplotlib.pyplot as plt
import numpy as np

S_values = np.linspace(0.5 * S, 1.5 * S, 100)
prices = [black_scholes(s, K, T, r, sigma, option_type) for s in S_values]

plt.figure(figsize=(10, 5))
plt.plot(S_values, prices, label=f"{option_type.capitalize()} Option Price")
plt.xlabel("Stock Price (S)")
plt.ylabel("Option Price")
plt.title("Option Price vs Stock Price")
plt.legend()
st.pyplot(plt)
