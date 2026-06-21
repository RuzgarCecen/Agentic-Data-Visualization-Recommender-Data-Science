"""
Agentic Data Visualization Recommender

A simple rule-based agent-like system that analyzes a CSV dataset,
recommends suitable visualizations, creates charts, and explains decisions.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from recommender import detect_column_types, dataset_summary, recommend_visualizations


st.set_page_config(
    page_title="Agentic Data Visualization Recommender",
    page_icon="📊",
    layout="wide"
)


st.title("📊 Agentic Data Visualization Recommender")
st.write(
    "This project is a simple rule-based agent-like system. "
    "It analyzes a CSV dataset, recommends suitable visualizations, "
    "generates charts, and explains its decision."
)


uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        st.success("Dataset uploaded successfully!")

        st.subheader("1. Dataset Preview")
        st.dataframe(df.head())

        st.subheader("2. Dataset Summary")
        summary = dataset_summary(df)

        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Rows", summary["rows"])
        col2.metric("Columns", summary["columns"])
        col3.metric("Missing Values", summary["missing_values"])
        col4.metric("Duplicated Rows", summary["duplicated_rows"])

        st.subheader("3. Column Type Analysis")
        column_types = detect_column_types(df)

        col_a, col_b = st.columns(2)
        with col_a:
            st.write("Numerical Columns")
            st.write(column_types["numerical"] if column_types["numerical"] else "No numerical columns found.")
        with col_b:
            st.write("Categorical Columns")
            st.write(column_types["categorical"] if column_types["categorical"] else "No categorical columns found.")

        st.subheader("4. Recommended Visualizations")
        recommendations = recommend_visualizations(df)

        if len(recommendations) == 0:
            st.warning("No suitable visualization could be recommended for this dataset.")
        else:
            # Limit displayed recommendations to keep the app simple and readable
            max_recommendations = min(len(recommendations), 20)
            recommendation_labels = [
                f"{i + 1}. {rec['chart_type']} - {', '.join(rec['columns'])}"
                for i, rec in enumerate(recommendations[:max_recommendations])
            ]

            selected_label = st.selectbox("Select a recommended visualization", recommendation_labels)
            selected_index = recommendation_labels.index(selected_label)
            selected_recommendation = recommendations[selected_index]

            st.info(selected_recommendation["reason"])

            st.subheader("5. Generated Visualization")

            chart_type = selected_recommendation["chart_type"]
            selected_columns = selected_recommendation["columns"]

            fig, ax = plt.subplots(figsize=(8, 5))

            if chart_type == "Histogram":
                sns.histplot(df[selected_columns[0]].dropna(), kde=True, ax=ax)
                ax.set_title(f"Histogram of {selected_columns[0]}")
                ax.set_xlabel(selected_columns[0])
                ax.set_ylabel("Frequency")

            elif chart_type == "Scatter Plot":
                sns.scatterplot(data=df, x=selected_columns[0], y=selected_columns[1], ax=ax)
                ax.set_title(f"Scatter Plot: {selected_columns[0]} vs {selected_columns[1]}")
                ax.set_xlabel(selected_columns[0])
                ax.set_ylabel(selected_columns[1])

            elif chart_type == "Bar Chart":
                value_counts = df[selected_columns[0]].value_counts().head(10)
                sns.barplot(x=value_counts.index.astype(str), y=value_counts.values, ax=ax)
                ax.set_title(f"Bar Chart of {selected_columns[0]}")
                ax.set_xlabel(selected_columns[0])
                ax.set_ylabel("Count")
                plt.xticks(rotation=45)

            elif chart_type == "Grouped Bar Chart":
                cat_col = selected_columns[0]
                num_col = selected_columns[1]
                grouped_data = df.groupby(cat_col)[num_col].mean().sort_values(ascending=False).head(10)
                sns.barplot(x=grouped_data.index.astype(str), y=grouped_data.values, ax=ax)
                ax.set_title(f"Average {num_col} by {cat_col}")
                ax.set_xlabel(cat_col)
                ax.set_ylabel(f"Average {num_col}")
                plt.xticks(rotation=45)

            st.pyplot(fig)

            st.subheader("6. Agent Decision Explanation")
            st.write("The system followed this simple agent-like workflow:")
            st.write("1. It observed the dataset uploaded by the user.")
            st.write("2. It analyzed column data types using Pandas.")
            st.write("3. It selected a visualization using predefined rules.")
            st.write("4. It generated the chart using Matplotlib and Seaborn.")
            st.write("5. It explained why the selected visualization is appropriate.")

    except Exception as e:
        st.error(f"An error occurred while reading or processing the file: {e}")

else:
    st.warning("Please upload a CSV file to start the analysis.")
    st.write("Suggested test datasets: Iris Dataset and Titanic Dataset.")
