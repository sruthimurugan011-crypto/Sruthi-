import itertools

# Function to evaluate logical expression
def evaluate_expression(expr, values, variables):
    local_dict = dict(zip(variables, values))
    return eval(expr, {}, local_dict)

# Input logical expression
expr = input("Enter logical expression (use and, or, not): ")

# Extract variables (like A, B, C)
variables = sorted(set([char for char in expr if char.isalpha()]))

print("\nTruth Table:\n")

# Print header
for var in variables:
    print(var, end=" ")
print("| Result")

# Generate all combinations
for values in itertools.product([0, 1], repeat=len(variables)):
    bool_values = [bool(v) for v in values]
    
    # Evaluate result
    result = evaluate_expression(expr, bool_values, variables)
    
    # Print row
    for v in values:
        print(v, end=" ")
    print("|", int(result))
