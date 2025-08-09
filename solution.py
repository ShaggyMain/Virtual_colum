import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # Define the regular expression for valid column labels (only letters and underscores)
    valid_label = re.compile(r"^[a-zA-Z_]+$")

    # Validate the new_column name
    if not valid_label.match(new_column):
        return pd.DataFrame([])

    # Validate all existing column labels in the DataFrame
    for col in df.columns:
        if not valid_label.match(col):
            return pd.DataFrame([])

    # Parse the 'role' string to extract column names and the operator.
    role_parts = re.split(r'\s*([+*-])\s*', role.strip())
    if len(role_parts) != 3:
        return pd.DataFrame([])

    col1, op, col2 = role_parts

    # Validate that the columns mentioned in the role exist in the DataFrame.
    if col1 not in df.columns or col2 not in df.columns:
        return pd.DataFrame([])

    # If all validations pass, perform the calculation.
    df_result = df.copy()

    if op == '+':
        df_result[new_column] = df_result[col1] + df_result[col2]
    elif op == '-':
        df_result[new_column] = df_result[col1] - df_result[col2]
    elif op == '*':
        df_result[new_column] = df_result[col1] * df_result[col2]

    return df_result