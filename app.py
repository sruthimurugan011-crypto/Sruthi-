import streamlit as st
import itertools

st.set_page_config(page_title="Truth Table Generator")

st.title("🧠 Truth Table Generator")

# Input from user
expr = st.text_input("Enter logical expression (use and, or, not):", "A and B")

# Function to evaluate expression
def evaluate_expression(expr, values, variables):
    local_dict = dict(zip(variables, values))
    return eval(expr, {}, local_dict)

if expr:
    # Extract variables
    variables = sorted(set([char for char in expr if char.isalpha()]))

    st.write("### Variables:", variables)

    # Generate truth table
    table = []
    for values in itertools.product([0, 1], repeat=len(variables)):
        bool_values = [bool(v) for v in values]
        result = evaluate_expression(expr, bool_values, variables)
        table.append(list(values) + [int(result)])

    # Display table
    st.write("### Truth Table")

    headers = variables + ["Result"]
    st.table([headers] + table)
