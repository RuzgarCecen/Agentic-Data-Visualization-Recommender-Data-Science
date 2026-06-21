# Agentic-Data-Visualization-Recommender-Data-Science
# Agentic Data Visualization Recommender

## Project Description

This project is a simple **agent-like data visualization recommender system** developed with Python. The system analyzes a CSV dataset, detects numerical and categorical columns, recommends suitable visualizations using rule-based logic, generates charts, and explains the reason for each recommendation.

The project is designed as a simple rule-based agent system. It observes the dataset, analyzes its structure, selects an appropriate visualization, creates the graph, and explains its decision.

## Team Member

- Ismail Rüzgar Çeçen

## Tools and Libraries

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

## Features

- CSV file upload
- Dataset preview
- Dataset summary
- Numerical and categorical column detection
- Rule-based visualization recommendation
- Automatic chart generation
- Short explanation for each selected chart

## Visualization Rules

| Data Type / Condition | Recommended Chart |
|---|---|
| One numerical column | Histogram |
| Two numerical columns | Scatter Plot |
| One categorical column | Bar Chart |
| One categorical + one numerical column | Grouped Bar Chart |

## Test Datasets

The system can be tested with:

- Iris Dataset
- Titanic Dataset
- Any different CSV dataset uploaded by the user

## Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

## How to Run

Run the Streamlit application:

```bash
streamlit run app.py
```

Then upload a CSV file from the browser interface.

## Agent-like Workflow

The system works with the following workflow:

1. The user uploads a CSV file.
2. The system reads the dataset using Pandas.
3. The system analyzes data types.
4. The system recommends a graph using simple rules.
5. The system generates the selected graph.
6. The system explains the reason for the selected visualization.

## Conclusion

This project provides a simple and understandable solution for automatic data visualization selection. It is especially useful for beginner users who may not know which chart type is appropriate for a given dataset.

