'''
  _____                                               
_/ ____\____ _______  _____             ____    ____  
\   __\\__  \\_  __ \/     \   ______  /    \  / ___\ 
 |  |   / __ \|  | \/  Y Y  \ /_____/ |   |  \/ /_/  >
 |__|  (____  /__|  |__|_|  /         |___|  /\___  / 
            \/            \/               \//_____/  

Sales Conversion Calculator v2023.02

Creator: Ryan Dinubilo
Created: 4/6/23
Revised: 

Changelog:
v1.0
- Created calculator
'''

import math
from functools import reduce
import streamlit as st

# Convert the input string x to float or return None if it can't be converted
def expr(x):
    try:
        return float(x)
    except ValueError:
        return None

# Calculate the binomial coefficient (combinations) for given n and k
def choose(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    return reduce(lambda c, i: c * (n - i) / (k - i), range(k), 1)

# Main calculation function for the sales probability
def calc(chance_txt, kc, obtained):
    chance = expr(chance_txt)
    if chance is None:
        return 'Looks like there was an error with your input chance, try typing it in again'
    elif chance > 1:
        return "You put your chance at over 1 you absolute madman"
    elif chance <= 0:
        return "You put your chance at 0 or negative, how you gonna get that drop?"

    kc = int(kc)
    if kc == 0:
        return "You don't have any visitors yet"

    obtained = int(obtained) if obtained.isdigit() else 0

    if kc < obtained:
        return 'More sales generated than visitors to the site? How?'

    if choose(kc, obtained) == float('inf'):
        return "Sorry, your visitor and sales obtained combination is too large for this calculator. Try reducing your numbers."

    probability = sum(choose(kc, i) * chance ** i * (1 - chance) ** (kc - i) for i in range(obtained + 1))

    return f"You have spent ${spent} for {kc} site visitors with a {chance_txt} ({100 * chance:.6f}%) sales conversion rate. You had a:\n* {100 * probability:.4f}% chance of getting {obtained} sales or fewer\n* {100 * (1 - probability):.4f}% chance of getting more than {obtained} sales."


# Streamlit interface
#Load sidebar logo and disclaimer
logo = st.sidebar.image("https://cdn.shopify.com/s/files/1/0624/6072/3426/files/logoincircle_100x.png?v=1662346828")
st.sidebar.title("Website Sales Probability Calculator")

# Sidebar input fields for the conversion rate, visitors, sales obtained, and ad spending
chance_txt = st.sidebar.text_input("Sales Conversion Rate (default=0.05%)", value="0.0005")
kc = st.sidebar.text_input("Vistors from ads", value="")
obtained = st.sidebar.text_input("Sales obtained from ads", value="")
spent = st.sidebar.text_input("Total $ spent on ads")

# Calculate the probability and display the result when the "Calculate" button is clicked
if st.sidebar.button("Calculate"):
    if chance_txt and kc and obtained:
        result = calc(chance_txt, kc, obtained)
        st.header("Expected Sales Probability")
        st.write(result)
    else:
        st.write("Please fill in all fields.")
