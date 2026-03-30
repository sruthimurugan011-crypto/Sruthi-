import itertools

# Function to evaluate logical expression
def evaluate_expression(expr, values, variables):
    local_dict = dict(zip(variables, values))
    return eval(expr, {}, local_dict)

# Input from user
expr = input("Enter logical expression (use and, or, not): ")

# Extract variables (A, B, C...)
variables = sorted(set([char for char in expr if char.isalpha()]))

print("\nVariables:", variables)

# Generate combinations (0,1)
combinations = list(itertools.product([0, 1], repeat=len(variables)))

# Print header
print("\nTruth Table:")
print(" | ".join(variables) + " | Output")
print("-" * (len(variables)*4 + 10))

# Generate table
for values in combinations:
    bool_values = [bool(v) for v in values]
    result = evaluate_expression(expr, bool_values, variables)
    
    # Convert True/False to 1/0
    result = int(result)
    row = " | ".join(map(str, values)) + " | " + str(result)
    print(row)
