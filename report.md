# Agentic Data Visualization Recommender - Project Report

## 1. Introduction

Data visualization is an important part of data analysis. However, selecting the correct visualization type can be difficult, especially for beginners. A wrong chart can make the data harder to understand and may lead to incorrect interpretations.

This project aims to develop a simple agent-like system that analyzes a dataset and recommends suitable visualizations automatically.

## 2. Project Objective

The objective of this project is to build a Python-based system that:

- Accepts CSV files from the user
- Reads the dataset using Pandas
- Detects numerical and categorical columns
- Selects an appropriate visualization using simple rules
- Generates the graph using Matplotlib and Seaborn
- Explains why the visualization was selected

## 3. Methodology

The project uses a rule-based approach. The system does not use a complex machine learning model. Instead, it behaves like a simple agent by following these steps:

1. Observing the dataset
2. Analyzing column types
3. Making a visualization decision
4. Generating a chart
5. Explaining the decision

## 4. Visualization Rules

The following rules are used in the system:

| Condition | Visualization |
|---|---|
| One numerical column | Histogram |
| Two numerical columns | Scatter Plot |
| One categorical column | Bar Chart |
| One categorical and one numerical column | Grouped Bar Chart |

## 5. Tools Used

The project uses the following tools and libraries:

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit

## 6. Testing

The project is planned to be tested using the Iris Dataset and Titanic Dataset. The system is also designed to work with different CSV datasets uploaded by the user.

## 7. Conclusion

The developed system provides a simple solution for automatic visualization recommendation. It reduces manual effort and helps users select suitable charts for their datasets. Although the system is rule-based and simple, it demonstrates the basic idea of an agent-like workflow in data analysis.
