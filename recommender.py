"""
Agentic Data Visualization Recommender
Rule-based helper functions for dataset analysis and visualization recommendation.
"""

import pandas as pd


def detect_column_types(df: pd.DataFrame) -> dict:
    """
    Detect numerical and categorical columns in the dataset.

    Parameters:
        df (pd.DataFrame): Input dataset.

    Returns:
        dict: Dictionary containing numerical and categorical column names.
    """
    numerical_columns = df.select_dtypes(include=["int64", "float64", "int32", "float32"]).columns.tolist()
    categorical_columns = df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()

    return {
        "numerical": numerical_columns,
        "categorical": categorical_columns,
    }


def dataset_summary(df: pd.DataFrame) -> dict:
    """
    Create a simple summary of the dataset.
    """
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": int(df.isnull().sum().sum()),
        "duplicated_rows": int(df.duplicated().sum()),
    }


def recommend_visualizations(df: pd.DataFrame) -> list:
    """
    Recommend visualizations using simple rule-based logic.

    Rules:
    - One numerical column -> Histogram
    - Two numerical columns -> Scatter plot
    - One categorical column -> Bar chart
    - One categorical and one numerical column -> Bar chart
    """
    column_types = detect_column_types(df)
    numerical_columns = column_types["numerical"]
    categorical_columns = column_types["categorical"]

    recommendations = []

    # Rule 1: Single numerical column -> histogram
    for col in numerical_columns:
        recommendations.append({
            "chart_type": "Histogram",
            "columns": [col],
            "reason": f"'{col}' is a numerical column. A histogram is suitable for showing the distribution of numerical values."
        })

    # Rule 2: Two numerical columns -> scatter plot
    if len(numerical_columns) >= 2:
        for i in range(len(numerical_columns)):
            for j in range(i + 1, len(numerical_columns)):
                recommendations.append({
                    "chart_type": "Scatter Plot",
                    "columns": [numerical_columns[i], numerical_columns[j]],
                    "reason": f"'{numerical_columns[i]}' and '{numerical_columns[j]}' are numerical columns. A scatter plot is suitable for showing the relationship between two numerical variables."
                })

    # Rule 3: Single categorical column -> bar chart
    for col in categorical_columns:
        recommendations.append({
            "chart_type": "Bar Chart",
            "columns": [col],
            "reason": f"'{col}' is a categorical column. A bar chart is suitable for comparing category frequencies."
        })

    # Rule 4: Categorical + numerical -> bar chart with average values
    if len(categorical_columns) >= 1 and len(numerical_columns) >= 1:
        for cat_col in categorical_columns:
            for num_col in numerical_columns:
                recommendations.append({
                    "chart_type": "Grouped Bar Chart",
                    "columns": [cat_col, num_col],
                    "reason": f"'{cat_col}' is categorical and '{num_col}' is numerical. A grouped bar chart can compare the average numerical value across categories."
                })

    return recommendations
