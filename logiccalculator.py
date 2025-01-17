from itertools import product
import tkinter as tk
from tkinter import messagebox

class LogicCalculator:
    def __init__(self, expression):
        self.expression = expression
        self.variables = sorted(set(filter(str.isalpha, expression)))

    def evaluate_expression(self, values):
        expr = self.expression
        for var, val in zip(self.variables, values):
            expr = expr.replace(var, str(int(val)))
        # Replace * with and, + with or, and ! with not
        expr = expr.replace('*', ' and ').replace('+', ' or ').replace('!', ' not ')
        return eval(expr)

    def generate_truth_table(self):
        combinations = list(product([0, 1], repeat=len(self.variables)))
        result = "Truth table for expression: " + self.expression + "\n"

        # Define reduced column widths for alignment
        column_width = 2
        expr_width = len(self.expression) + 10  # Adjust width based on the expression length

        # Create header with NOT operation if present
        var_header = " | ".join(f"{var:<{column_width}}" for var in self.variables)
        not_vars = [v for v in self.variables if "!" + v in self.expression]
        header = var_header

        # Add NOT columns if present
        for var in not_vars:
            header += f" | {'!' + var:<{column_width}}"

        # Add final expression column
        header += f" | {self.expression:<{expr_width}}"
        result += header + "\n"
        result += "-" * len(header) + "\n"

        for combination in combinations:
            row_values = [f"{val:<{column_width}}" for val in combination]
            expr = self.expression
            substituted_expr = self.expression  # To dynamically show substitutions

            # Calculate NOT values if present
            for var, val in zip(self.variables, combination):
                if "!" + var in self.expression:
                    not_val = int(not int(val))
                    row_values.append(f"{not_val:<{column_width}}")
                    substituted_expr = substituted_expr.replace(f"!{var}", str(not_val))

            # Replace variables with their values in the substituted expression
            for var, val in zip(self.variables, combination):
                expr = expr.replace(var, str(int(val)))
                substituted_expr = substituted_expr.replace(var, str(int(val)))

            # Evaluate the final result
            eval_expr = expr.replace('*', ' and ').replace('+', ' or ').replace('!', ' not ')
            res = eval(eval_expr)

            # Combine the substituted expression and result
            calculation_with_result = f"{substituted_expr} = {int(res):<{expr_width}}"

            # Add final result
            row_values.append(calculation_with_result)
            row = " | ".join(row_values)
            result += row + "\n"

        return result


def calculate():
    expression = entry.get()
    calculator = LogicCalculator(expression)
    result = calculator.generate_truth_table()
    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, result)  # Insert new result

# GUI setup # Insert new result

# GUI setup
root = tk.Tk()
root.title("Boolean Algebra Calculator")

tk.Label(root, text="Enter a Boolean expression (e.g., (C*A)+!B):").pack()
entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Calculate", command=calculate).pack()

output_text = tk.Text(root, wrap=tk.WORD, width=60, height=20)
output_text.pack()

root.mainloop()